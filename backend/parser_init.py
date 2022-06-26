import datetime
import time

from parsers.news_source_parsers.universal_news_parser import UniversalNewsParser
from parsers.news_source_parsers.callable_pairs import CALLABLE_PAIRS
from parsers.company_source_parsers.company_setups import COMPANY_SETUPS
from parsers.company_source_parsers.universal_company_parser import UniversalCompanyParser


from  database_adapter.post_adapter import PostDatabaseAdapter

from  database_adapter.models import BasePost


def add_to_db(res_dict):
    resource = ""
    try:
        resource = res_dict["link"].split('/')[2]
    except:
        resource = res_dict["link"]
    post = BasePost(
        company_name=res_dict['company'],
        date=time.time(),
        resource=resource,
        title=res_dict['header'],
        link=res_dict['link'],
        category=res_dict['category'],
        doc='html',
        archive=False
    )

    try:
        post_id = PostDatabaseAdapter.create_post(post_model=post)
        print(f'добавлен в базу, id = {post_id}')
    except Exception as e:
        print(e)


def update():
    for company, get_links, parse_page in COMPANY_SETUPS:
        parser = UniversalCompanyParser(company, get_links, parse_page)

        index  = 0
        print(datetime.datetime.now())
        for res in parser.get_news():
            print(res)
            print(datetime.datetime.now())
            print(time.time())
            index += 1

            #add_to_db(res)

    for get_links, parse_page in CALLABLE_PAIRS:
        parser = UniversalNewsParser(get_links, parse_page)

        index = 0
        print(datetime.datetime.now())
        for res in parser.get_news():
            print(res)
            print(datetime.datetime.now())
            print(time.time())
            index += 1

            #add_to_db(res)




if __name__ == "__main__":
    update()