import requests
import re
from bs4 import BeautifulSoup
from constants import SEARCH_KEYWORDS
from news_getters.universal_news_link_getter import UniversalNewsLinkGetter


def orenburgcci_page_maker(page_number, company):
    link = f"https://orenburg-cci.ru/page/{page_number}/?s={company}"
    return requests.get(link)


def orenburgcci_stop_checker(page_number, company, request_res):
    return re.search("Страница не найдена", request_res.text) is None


def orenburgcci_link_finder(request_res):
    parser_soup = BeautifulSoup(request_res.text, "html.parser")
    for tag in parser_soup.find_all("h2", "entry-title"):
        yield tag.a["href"]


orenburgcci_link_getter = UniversalNewsLinkGetter(orenburgcci_page_maker,
                                                  orenburgcci_stop_checker,
                                                  orenburgcci_link_finder)
