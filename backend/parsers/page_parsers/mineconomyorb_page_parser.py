from bs4 import BeautifulSoup
import requests
from parsers.constants import TZ, MONTHS_FR
from datetime import datetime

def mineconomyorb_page_parser(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36'}
    request_res = requests.get(link, headers=headers)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = parse_soup.find("h1", "news-detail__title").text.strip()
    text = parse_soup.find("div", "news-detail__text").get_text().strip()
    date = " ".join(parse_soup.find("div", "news__info").text.strip().split()[:3])
    try:
        d,m,y = date.split()
        d = int(d)
        m = MONTHS_FR.index(m.lower()) + 1
        y = int(y)
        date = datetime(y, m, d, tzinfo=TZ).timestamp()
    except:
        date = None
    return header, text, date
