from bs4 import BeautifulSoup
import requests


def zbo_page_parser(link):
    request_res = requests.get(link)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = parse_soup.find("h1", "pagetitle").text.strip()
    text = parse_soup.find("div", "detail news fixed_wrapper").get_text().strip()
    date = parse_soup.find("span", "date").text.strip()
    return header, text, date
