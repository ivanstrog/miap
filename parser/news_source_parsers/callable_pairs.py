from news_getters.orenburgcci_getter import orenburgcci_link_getter
from news_getters.orenburgmedia_getter import orenburgmedia_link_getter
from news_getters.orenburggov_getter import orenburggov_link_getter
from news_getters.minpromenergoorb_getter import minpromenergoorb_link_getter
from news_getters.mineconomyorb_getter import mineconomyorb_link_getter
from page_parsers.orenburgcci_page_parser import orenburgcci_page_parser
from page_parsers.orenburgmedia_page_parser import orenburgmedia_page_parser
from page_parsers.orenburggov_page_parser import orenburggov_page_parser
from page_parsers.minpromenergoorb_page_parser import minpromenergoorb_page_parser
from page_parsers.mineconomyorb_page_parser import mineconomyorb_page_parser


CALLABLE_PAIRS = [
    (mineconomyorb_link_getter.get_links, mineconomyorb_page_parser),
    (orenburggov_link_getter.get_links, orenburggov_page_parser),
    (orenburgcci_link_getter.get_links, orenburgcci_page_parser),
    (orenburgmedia_link_getter.get_links, orenburgmedia_page_parser),
    (minpromenergoorb_link_getter.get_links, minpromenergoorb_page_parser),
]
