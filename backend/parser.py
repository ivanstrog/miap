import datetime
import time

from parsers.news_source_parsers.universal_news_parser import UniversalNewsParser
from parsers.news_source_parsers.callable_pairs import CALLABLE_PAIRS
from parsers.company_source_parsers.company_setups import COMPANY_SETUPS
from parsers.company_source_parsers.universal_company_parser import UniversalCompanyParser


from  database_adapter.post_adapter import PostDatabaseAdapter

from  database_adapter.models import BasePost
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

    index  = 0
    print(datetime.datetime.now())
    for res in parser.get_news():
        print(res)
        print(datetime.datetime.now())
        print(time.time())
        index += 1


        post = BasePost(
            company_name=res['company'],
            date= time.time() ,
            resource=res['link'],
            title=res['header'],
            link=res['link'],
            category=res['category'],
            doc='html'
        )

        try:
            post_id =  PostDatabaseAdapter.create_post(post_model=post)
            print(f'добавлен в базу, id = {post_id}')
        except Exception as e:
            print(e)
