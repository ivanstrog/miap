import requests
import re
from bs4 import BeautifulSoup
from parser.constants import SEARCH_KEYWORDS
from parser.news_getters.universal_news_link_getter import UniversalNewsLinkGetter


def orenburgmedia_page_maker(page_number, company):
    link = f"https://orenburg.media/?paged={page_number}&s={company}"
    return requests.get(link)


def orenburgmedia_stop_checker(page_number, company, request_res):
    return re.search("Страница не найдена", request_res.text) is None


def orenburgmedia_link_finder(request_res):
    parser_soup = BeautifulSoup(request_res.text, "html.parser")
    for tag in parser_soup.find_all("h2", "post-title"):
        yield tag.a["href"]


orenburgmedia_link_getter = UniversalNewsLinkGetter(orenburgmedia_page_maker,
                                                    orenburgmedia_stop_checker,
                                                    orenburgmedia_link_finder)
