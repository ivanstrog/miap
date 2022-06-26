import requests
import re
from bs4 import BeautifulSoup
from parsers.constants import SEARCH_KEYWORDS
from parsers.company_getters.universal_company_link_getter import UniversalCompanyLinkGetter


def orgma_page_maker(page_number, keyword):
    link = f"https://orgma.ru/component/search/?searchword={keyword}&ordering=newest&searchphrase=any&limit=0"
    return requests.get(link)


def orgma_stop_checker(page_number, keyword, request_res):
    return page_number < 2


def orgma_link_finder(request_res):
    parser_soup = BeautifulSoup(request_res.text, "html.parser")
    for tag in parser_soup.find_all("dt", "result-title"):
        yield "https://orgma.ru" + tag.a["href"]


orgma_link_getter = UniversalCompanyLinkGetter(orgma_page_maker,
                                                 orgma_stop_checker,
                                                 orgma_link_finder)
