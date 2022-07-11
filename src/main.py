import argparse
from coursera_scraper import CourseraScraper


def read_parameters():
    """
    reads parameters from command line
    :return: parsed parameters
    """
    parser = argparse.ArgumentParser(
        description="Coursera Scraper parameters Options.", prog="SCRIPT"
    )
    parser.add_argument(
        "--query",
        type=str,
        nargs=1,
        metavar="<Course Name>",
        help="Course search query",
        required=False,
        default=None,
    )
    parser.add_argument(
        "--max_count",
        type=int,
        nargs=1,
        metavar="<Courses max count>",
        help="Max count of courses to scrap",
        required=False,
        default=10,
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    input_params = read_parameters()
    scraper = CourseraScraper("coursera_courses2.csv")
    scraper.scrape_courses(search_keyword=input_params.query[0], max_count=input_params.max_count[0])
    print("__name__")
