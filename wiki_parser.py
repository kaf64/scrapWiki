"""
Class WikiParser
Provides parsing english Wikipedia main page.
"""
from bs4 import BeautifulSoup


class WikiParser:
    def collect_data(self, url_content: str) -> dict:
        result = dict()
        soup = BeautifulSoup(url_content, from_encoding="utf-8", features="html.parser")
        result['otd'] = soup.find(id='mp-otd').find('ul').getText()
        result['featured_article'] = soup.find(id='mp-tfa').find('p').getText()
        # replacing html new line character to string new line
        result['otd'] = result['otd'].replace('<br/>', '\n')
        result['otd'] = result['otd'].replace('<br />', '\n')
        result['featured_article'] = result['featured_article'].replace('<br/>', '\n')
        result['featured_article'] = result['featured_article'].replace('<br />', '\n')
        return result
