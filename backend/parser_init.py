import datetime
import os
import time

from requests import get

from parsers.news_source_parsers.universal_news_parser import UniversalNewsParser
from parsers.news_source_parsers.callable_pairs import CALLABLE_PAIRS
from parsers.company_source_parsers.company_setups import COMPANY_SETUPS
from parsers.company_source_parsers.universal_company_parser import UniversalCompanyParser

from database_adapter.post_adapter import PostDatabaseAdapter

from database_adapter.models import BasePost


def add_to_db(res_dict):
    if res_dict["date"] is None:
        res_dict["date"] = 0
    resource = ""
    try:
        resource = res_dict["link"].split('/')[2]
    except:
        resource = res_dict["link"]

    file_name = f"storage/{res_dict['link'].replace('/','').replace(':','')}.html"
    post = BasePost(
        company_name=res_dict['company'],
        date=res_dict["date"],
        resource=resource,
        title=res_dict['header'],
        link=res_dict['link'],
        category=res_dict['category'],
        # doc=f"storage/{res_dict['company']}_{res_dict['date']}_{datetime.d}.txt",
        doc=file_name,
        archive=False
    )


    post_id = PostDatabaseAdapter.create_post(post_model=post)

    print(f'добавлен в базу, id = {post_id}')
    # запись в хранилище

    try:
        os.chdir("backend")
    except Exception as e:
        print(e)

    try:
        doc_file = open(file_name, 'w')
        doc_file.write(get(res_dict["link"], headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/103.0.0.0 Safari/537.36'}, timeout=1).text)
        doc_file.close()
    except Exception as e:
        pass




def update():
    for get_links, parse_page in CALLABLE_PAIRS:
        parser = UniversalNewsParser(get_links, parse_page)

        index = 0
        print(datetime.datetime.now())
        for res in parser.get_news():
            print(res)
            print(datetime.datetime.now())
            print(time.time())
            index += 1
            try:
                add_to_db(res)
            except:
                pass
            
    for company, get_links, parse_page in COMPANY_SETUPS:
        parser = UniversalCompanyParser(company, get_links, parse_page)

        index = 0
        print(datetime.datetime.now())
        for res in parser.get_news():
            print(res)
            print(datetime.datetime.now())
            print(time.time())
            index += 1
            try:
                add_to_db(res)
            except:
                pass


if __name__ == "__main__":
    update()
