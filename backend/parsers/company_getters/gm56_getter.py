import requests
import re
from bs4 import BeautifulSoup
from parsers.constants import SEARCH_KEYWORDS
from parsers.company_getters.universal_company_link_getter import UniversalCompanyLinkGetter


def gm56_page_maker(page_number, keyword):
    link = f"https://gm56.ru/rezultat-poiska/?simplesearch_offset={10 * (page_number - 1)}&query={keyword}"
    return requests.get(link)


def gm56_stop_checker(page_number, keyword, request_res):
    return re.search("ничего не найдено", request_res.text) is None


def gm56_link_finder(request_res):
    parser_soup = BeautifulSoup(request_res.text, "html.parser")
    for tag in parser_soup.find_all("div", "sisea-result"):
        yield "https://gm56.ru/" + tag.h3.a["href"]


gm56_link_getter = UniversalCompanyLinkGetter(gm56_page_maker,
                                                 gm56_stop_checker,
                                                 gm56_link_finder)
