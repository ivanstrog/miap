import requests
import re
from bs4 import BeautifulSoup
from parsers.constants import SEARCH_KEYWORDS
from parsers.company_getters.universal_company_link_getter import UniversalCompanyLinkGetter


def orensau_page_maker(page_number, keyword):
    link = f"https://orensau.ru/ru/poisk?searchword={keyword}&limit=0"
    return requests.get(link)


def orensau_stop_checker(page_number, keyword, request_res):
    return page_number < 2


def orensau_link_finder(request_res):
    parser_soup = BeautifulSoup(request_res.text, "html.parser")
    for tag in parser_soup.find_all("div", "contentheading"):
        if tag.a["href"][1:11] == "ru/novosty":
            yield "https://orensau.ru" + tag.a["href"]


orensau_link_getter = UniversalCompanyLinkGetter(orensau_page_maker,
                                                 orensau_stop_checker,
                                                 orensau_link_finder)
