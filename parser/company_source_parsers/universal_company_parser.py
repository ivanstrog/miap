import re
import pymorphy2
from constants import SEARCH_KEYWORDS

morph = pymorphy2.MorphAnalyzer()


class UniversalCompanyParser:
    def __init__(self, company, get_links, parse_page):
        self.company = company
        self.get_links = get_links
        self.parse_page = parse_page

    def get_news(self):
        for link in self.get_links():
            useful_link = False
            header, text, date = "", "", ""
            try:
                header, text, date = self.parse_page(link)
            except:
                header, text, date = "", "", ""
            for keyword in SEARCH_KEYWORDS:
                for form in (morph.parse(word=keyword)[0]).lexeme:
                    if re.search(form.word, text.lower()) is not None:
                        useful_link = True
                        yield {"link": link, "header": header,
                                       "date": date, "company": self.company,
                                       "category": keyword}
                    break
                if useful_link:
                    break
