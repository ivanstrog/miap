from bs4 import BeautifulSoup
import requests


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
    return header, text, date
