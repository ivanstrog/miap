import requests
import re
from bs4 import BeautifulSoup
from parser.constants import SEARCH_KEYWORDS
from parser.company_getters.universal_company_link_getter import UniversalCompanyLinkGetter


def zbo_page_maker(page_number, keyword):
    link = f"http://zbo.ru/search/?q={keyword}&s=Найти"
    return requests.get(link)


def zbo_stop_checker(page_number, keyword, request_res):
    return page_number < 2


def zbo_link_finder(request_res):
    tails = re.findall('(/info/news/[^"]+)"', request_res.text)
    for tail in tails:
        yield "http://zbo.ru/" + tail


zbo_link_getter = UniversalCompanyLinkGetter(zbo_page_maker,
                                                 zbo_stop_checker,
                                                 zbo_link_finder)
