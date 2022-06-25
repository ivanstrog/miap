from company_getters.orenmin_getter import orenmin_link_getter
from company_getters.zbo_getter import zbo_link_getter
from page_parsers.orenmin_page_parser import orenmin_page_parser
from page_parsers.zbo_page_parser import zbo_page_parser


COMPANY_SETUPS = [
    ("Завод бурового оборудования", zbo_link_getter.get_links, zbo_page_parser),
    ("Оренбургские минералы", orenmin_link_getter.get_links, orenmin_page_parser)
]
