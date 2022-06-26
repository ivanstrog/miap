from bs4 import BeautifulSoup
import requests
from parsers.constants import TZ, MONTHS_FR
from datetime import datetime


def orensau_page_parser(link):
    request_res = requests.get(link)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = parse_soup.find("td", "table_cell_positioned").h3.text.strip()
    text = parse_soup.find(valign="top").get_text().strip()
    date = None
    try:
        date = parse_soup.find("div", "news_date").text.strip()
        d,m,y = date.split()
        d = int(d)
        m = MONTHS_FR.index(m.lower()) + 1
        y = int(y)
        date = datetime(y, m, d, tzinfo=TZ).timestamp()
    except:
        date = None
    return header, text, date
