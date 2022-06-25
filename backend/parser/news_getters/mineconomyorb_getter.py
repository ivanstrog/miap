import requests
import re
from bs4 import BeautifulSoup
from parser.constants import SEARCH_KEYWORDS
from parser.news_getters.universal_news_link_getter import UniversalNewsLinkGetter


def mineconomyorb_page_maker(page_number, company):
    link = f"https://mineconomy.orb.ru//search/?q={company}&nav-search=page-{page_number}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36'}
    return requests.get(link, headers=headers)


def mineconomyorb_stop_checker(page_number, company, request_res):
    return re.search("на ваш поисковый запрос ничего не найдено", request_res.text) is None


def mineconomyorb_link_finder(request_res):
    parser_soup = BeautifulSoup(request_res.text, "html.parser")
    for tag in parser_soup.find_all("h2", "news__title"):
        if tag.a["href"][1:17] == "presscenter/news":
            yield "https://mineconomy.orb.ru" + tag.a["href"]


mineconomyorb_link_getter = UniversalNewsLinkGetter(mineconomyorb_page_maker,
                                                    mineconomyorb_stop_checker,
                                                    mineconomyorb_link_finder)
