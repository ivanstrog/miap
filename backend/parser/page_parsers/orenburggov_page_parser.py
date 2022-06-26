from bs4 import BeautifulSoup
import requests


def orenburggov_page_parser(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36'}
    request_res = requests.get(link, headers=headers)
    parse_soup = BeautifulSoup(request_res.text, "html.parser")
    header = " ".join(parse_soup.find("div", "news-detail__top").text.strip().split()[2:])
    text = parse_soup.find("div", "news-detail__detail").get_text().strip()
    date = " ".join(parse_soup.find("div", "news-detail__date").text.strip().split()[2:])
    return header, text, date
