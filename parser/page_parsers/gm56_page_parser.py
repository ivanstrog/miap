from bs4 import BeautifulSoup
import requests


def gm56_page_parser(link):
    request_res = requests.get(link)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = parse_soup.find("div", "page__wrap").h1.text.strip()
    text = parse_soup.find("div", "content").get_text().strip()
    date = parse_soup.find("div", "article__date").text.strip()
    return header, text, date
