import datetime
from news_source_parsers.universal_news_parser import UniversalNewsParser
from news_source_parsers.callable_pairs import CALLABLE_PAIRS
from company_source_parsers.company_setups import COMPANY_SETUPS
from company_source_parsers.universal_company_parser import UniversalCompanyParser

'''
for get_links, parse_page in CALLABLE_PAIRS:
    parser = UniversalNewsParser(get_links, parse_page)

    print(datetime.datetime.now())
    for res in parser.get_news():
        print(res)
        print(datetime.datetime.now())
'''

for company, get_links, parse_page in COMPANY_SETUPS:
    parser = UniversalCompanyParser(company, get_links, parse_page)

    print(datetime.datetime.now())
    for res in parser.get_news():
        print(res)
        print(datetime.datetime.now())
