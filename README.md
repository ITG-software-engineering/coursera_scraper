### Coursera courses Scraper

This is a scraper script and pipline to import courses from cousera and save them in CSV file.

Python version used: ```3.8.9```
main.py is the starting point, and it takes 2 input arguments:
- ```--query``` for search by string option
- ```--max_count``` to limit number of coursed to scrap, it **defaults to 10**

tests were written under tests folder using ```pytest```

##### Commands:
If you don't have python installed, install from <a href="https://www.python.org/downloads/release/python-3101/">here</a>

run following command to make sure pip is updated ```pip install --upgrade pip```

Install dependancies: ```pip install -r requirements.txt```

To run the main.py: `python main.py --query google --max_cound 20`
<p>To run unit tests: `pytest src`.</p>


### Argo WorkFlows:
<p>`coursera_courses_pipeline.yaml` file has configuration of 4 tasks workflow with consideration of dependencies. each task is responsible of one action</p>
<p>The workflow scheduled to be run in weekly basis</p>