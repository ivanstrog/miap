import requests
import re
from bs4 import BeautifulSoup
from constants import SEARCH_KEYWORDS
from news_getters.universal_news_link_getter import UniversalNewsLinkGetter


def minpromenergoorb_page_maker(page_number, company):
    link = f"https://minpromenergo.orb.ru//search/?q={company}&nav-search=page-{page_number}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36'}
    return requests.get(link, headers=headers)


def minpromenergoorb_stop_checker(page_number, company, request_res):
    return re.search("на ваш поисковый запрос ничего не найдено", request_res.text) is None


def minpromenergoorb_link_finder(request_res):
    parser_soup = BeautifulSoup(request_res.text, "html.parser")
    for tag in parser_soup.find_all("h2", "news__title"):
        if tag.a["href"][1:17] == "presscenter/news":
            yield "https://minpromenergo.orb.ru" + tag.a["href"]


minpromenergoorb_link_getter = UniversalNewsLinkGetter(minpromenergoorb_page_maker,
                                                       minpromenergoorb_stop_checker,
                                                       minpromenergoorb_link_finder)
