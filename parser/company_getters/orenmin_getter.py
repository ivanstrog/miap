import requests
import re
from bs4 import BeautifulSoup
from constants import SEARCH_KEYWORDS
from company_getters.universal_company_link_getter import UniversalCompanyLinkGetter


def orenmin_page_maker(page_number, keyword):
    link = f"https://orenmin.ru/component/search/?searchword={keyword}&limit=0"
    return requests.get(link)


def orenmin_stop_checker(page_number, keyword, request_res):
    return page_number < 2


def orenmin_link_finder(request_res):
    parser_soup = BeautifulSoup(request_res.text, "html.parser")
    for tag in parser_soup.find_all("dt", "result-title"):
        if tag.a["href"][1:8] == "novosti":
            yield "https://orenmin.ru" + tag.a["href"]


orenmin_link_getter = UniversalCompanyLinkGetter(orenmin_page_maker,
                                                 orenmin_stop_checker,
                                                 orenmin_link_finder)
