This repository was forked from https://code402.com/hello-warc-common-crawl-code-samples

In the `python` directory, `run.py` loops through WARC files that contains paths to web pages from Common Crawl's 2020 archive (which can be found in the `warc_data` directory). `run.py` then calls the search function in crawl.py to access data from each page, with the goal of finding pages that discuss or are relevant to COVID-19's economic impact, along with the month(s) of 2020 in which the page was pulled from.

The list of URLs and months can be found in url.csv in the `python` directory.
