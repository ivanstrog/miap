import requests
import re
from bs4 import BeautifulSoup
from constants import SEARCH_KEYWORDS
from news_getters.universal_news_link_getter import UniversalNewsLinkGetter


def orenburggov_page_maker(page_number, company):
    link = f"https://orenburg-gov.ru/search/?q={company}&nav-search=page-{page_number}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36'}
    return requests.get(link, headers=headers)


def orenburggov_stop_checker(page_number, company, request_res):
    return re.search("По вашему запросу ничего не найдено", request_res.text) is None


def orenburggov_link_finder(request_res):
    parser_soup = BeautifulSoup(request_res.text, "html.parser")
    for tag in parser_soup.find_all("div", "list__item-body-content"):
        if tag.a["href"][1:5] == "news":
            yield "https://orenburg-gov.ru" + tag.a["href"]


orenburggov_link_getter = UniversalNewsLinkGetter(orenburggov_page_maker,
                                                  orenburggov_stop_checker,
                                                  orenburggov_link_finder)
