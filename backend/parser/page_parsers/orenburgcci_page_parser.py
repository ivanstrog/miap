from bs4 import BeautifulSoup
import requests


def orenburgcci_page_parser(link):
    request_res = requests.get(link)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = parse_soup.find("span", "news-title").text.strip()
    text = parse_soup.find("div", "article-condition").get_text().strip()
    date = parse_soup.find("span", "news-date").text.strip()
    return header, text, date
