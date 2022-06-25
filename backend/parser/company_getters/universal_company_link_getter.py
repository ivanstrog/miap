import requests
import re
from parser.constants import SEARCH_KEYWORDS, COMPANIES


class UniversalCompanyLinkGetter:
    def __init__(self, search_page_maker, stop_checker, link_finder):
        self.search_page_maker = search_page_maker
        self.stop_checker = stop_checker
        self.link_finder = link_finder

    def get_links(self):
        for keyword in SEARCH_KEYWORDS:
            request_res = None
            page_number = 1
            try:
                request_res = self.search_page_maker(page_number, keyword)
            except:
                request_res = None
            while request_res is not None and self.stop_checker(page_number, keyword, request_res):
                try:
                    for found_link in self.link_finder(request_res):
                        yield found_link
                    page_number += 1
                    request_res = self.search_page_maker(page_number, keyword)
                except:
                    break
