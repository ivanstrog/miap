from bs4 import BeautifulSoup
import requests


def orensau_page_parser(link):
    request_res = requests.get(link)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = parse_soup.find("td", "table_cell_positioned").h3.text.strip()
    text = parse_soup.find(valign="top").get_text().strip()
    date = None
    try:
        date = parse_soup.find("div", "news_date").text.strip()
    except:
        date = None
    return header, text, date
