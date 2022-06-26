from bs4 import BeautifulSoup
import requests
from parsers.constants import TZ
from datetime import datetime


def orenburgcci_page_parser(link):
    request_res = requests.get(link)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = parse_soup.find("span", "news-title").text.strip()
    text = parse_soup.find("div", "article-condition").get_text().strip()
    date = parse_soup.find("span", "news-date").text.strip()
    try:
        d, m, y, = date.split(".")
        d = int(d)
        m = int(m)
        y = int(y)
        date = datetime(y, m, d, tzinfo=TZ).timestamp()
    except:
        date = None
    return header, text, date
