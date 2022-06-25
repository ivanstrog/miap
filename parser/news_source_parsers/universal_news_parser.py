import re
import pymorphy2
from constants import SEARCH_KEYWORDS

morph = pymorphy2.MorphAnalyzer()


class UniversalNewsParser:
    def __init__(self, get_links, parse_page):
        self.get_links = get_links
        self.parse_page = parse_page

    def get_news(self):
        for link, company in self.get_links():
            useful_link = False
            header, text, date = None, None, None
            try:
                header, text, date = self.parse_page(link)
            except:
                header, text, date = "", "", ""
            if (re.search(company, text) is None) and (re.search(company, header)) is None:
                continue
            for keyword in SEARCH_KEYWORDS:
                for form in (morph.parse(word=keyword)[0]).lexeme:
                    if re.search(form.word, text.lower()) is not None:
                        useful_link = True
                        yield {"link": link, "header": header,
                                       "date": date, "company": company,
                                       "category": keyword}
                    break
                if useful_link:
                    break
