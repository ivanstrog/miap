from bs4 import BeautifulSoup
import requests


def orenmin_page_parser(link):
    request_res = requests.get(link)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = parse_soup.find("h2", "contentheading").text.strip()
    text = parse_soup.find("div", "item-page clearfix").get_text().strip()
    date = None
    return header, text, date
