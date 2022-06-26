from bs4 import BeautifulSoup
import requests


def orgma_page_parser(link):
    request_res = requests.get(link)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = parse_soup.find("div", "itemHeader").h2.text.strip()
    text = parse_soup.find("div", "itemFullText").get_text().strip()
    date = None
    return header, text, date
