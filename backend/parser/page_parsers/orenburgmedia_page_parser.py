from bs4 import BeautifulSoup
import requests


def orenburgmedia_page_parser(link):
    request_res = requests.get(link)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = parse_soup.find("h1", "post-title").text.strip()
    text = parse_soup.find("div", "post-content").get_text().strip()
    date = parse_soup.find("div", "post-byline").text.strip().split()[1]
    return header, text, date
