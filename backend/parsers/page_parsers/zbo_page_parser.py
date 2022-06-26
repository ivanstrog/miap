from bs4 import BeautifulSoup
import requests
from parsers.constants import TZ, MONTHS_FR
from datetime import datetime


def zbo_page_parser(link):
    request_res = requests.get(link)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = None
    try:
        header = parse_soup.find("h1", "pagetitle").text.strip()
    except AttributeError:
        try:
            header = parse_soup.find("div", "introtext norder").get_text().strip()
        except:
            header = None
    text = parse_soup.find("div", "detail news fixed_wrapper").get_text().strip()
    date = None
    try:
        date = parse_soup.find("span", "date").text.strip()
        d,m,y = date.split()
        d = int(d)
        m = MONTHS_FR.index(m.lower()) + 1
        y = int(y)
        date = datetime(y, m, d, tzinfo=TZ).timestamp()
    except:
        date = None
    if header is None:
        text = ""
    return header, text, date
