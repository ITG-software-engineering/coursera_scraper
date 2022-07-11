from typing import Dict, List
from bs4 import BeautifulSoup
import requests
import csv
import json
import re
import pandas as pd


class CourseraScraper:
    ROOT_URL = "https://www.coursera.org"

    courses_column_names = ["Name", "Url", "Rating", "Tags", "Description"]

    def __init__(self, export_file_name: str) -> None:
        self.export_file_name = export_file_name

    def scrape_courses(self, search_keyword: str, max_count: int = 10, export_to_csv: bool = True):
        all_courses_data = []
        page_num = 1
        while len(all_courses_data) < max_count:
            html_content = self._get_html(search_keyword, page_num)
            page_courses = self._parse_courses(html_content)
            all_courses_data.extend(page_courses)
            page_num = page_num + 1
        coursed_df = pd.DataFrame(
            all_courses_data[:max_count], columns=self.courses_column_names
        )
        if export_to_csv:
            coursed_df.to_csv(self.export_file_name)
        return coursed_df

    def _get_html(self, search_keyword: str, page_num: int = 1):
        search_query_param = (
            f"query={search_keyword}" if search_keyword is not None else ""
        )
        page_num_query_param = f"page={page_num}"
        query_params = "&".join([search_query_param, page_num_query_param])
        url = f"{self.ROOT_URL}/search?{query_params}"
        headers = self._get_headers()
        return requests.get(url, headers=headers).text

    def _get_headers(self):
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "//www.udemy.com/courses/search/?p=1&q=python",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }
        return headers

    def _parse_courses(self, html: str) -> List[Dict]:
        courses_data = []
        soup = BeautifulSoup(html, "html.parser")
        mydivs = (
            soup.find("body")
            .find("script")
            .text.split('{"context"')[1]
            .split(',"plugins":{}};')[0][1::]
        )
        json_object = json.loads(mydivs)
        courses = json_object["dispatcher"]["stores"]["AlgoliaResultsStateStore"][
            "resultsState"
        ][2]["content"]["hits"]
        for obj in courses:
            name = obj["name"]
            url = self.ROOT_URL + obj["objectUrl"]
            tag = ", ".join(obj["skills"])
            Rating = round(float(obj["avgProductRating"]), 1)
            description = obj["_snippetResult"]["description"]["value"]
            course_details = {
                "Name": name,
                "Url": url,
                "Rating": Rating,
                "Tags": tag,
                "Description": description,
            }
            courses_data.append(course_details)

        return courses_data
