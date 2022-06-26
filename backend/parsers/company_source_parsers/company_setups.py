from parsers.company_getters.orenmin_getter import orenmin_link_getter
from parsers.company_getters.zbo_getter import zbo_link_getter
from parsers.company_getters.gm56_getter import gm56_link_getter
#from company_getters.bacoren_getter import bacoren_link_getter
from parsers.company_getters.orensau_getter import orensau_link_getter
from parsers.page_parsers.orenmin_page_parser import orenmin_page_parser
from parsers.page_parsers.zbo_page_parser import zbo_page_parser
from parsers.page_parsers.gm56_page_parser import gm56_page_parser
#from page_parsers.bacoren_page_parser import bacoren_page_parser
from parsers.page_parsers.orensau_page_parser import orensau_page_parser


COMPANY_SETUPS = [
    ("ОРЕНБУРГСКИЙ ГОСУДАРСТВЕННЫЙ АГРАРНЫЙ УНИВЕРСИТЕТ", orensau_link_getter.get_links, orensau_page_parser),
    #("Бакорен", bacoren_link_getter.get_links, bacoren_page_parser), - доделать парсер страницы со статьёй
    ("Глобал Мониторинг", gm56_link_getter.get_links, gm56_page_parser),
    ("Завод бурового оборудования", zbo_link_getter.get_links, zbo_page_parser),
    ("Оренбургские минералы", orenmin_link_getter.get_links, orenmin_page_parser)
]
