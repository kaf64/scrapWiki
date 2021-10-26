"""
Class UrlClient
Provides connection to given URL and save content
"""
import requests


class UrlClient:

    def get_url_source(self, url: str) -> dict:
        result = dict()
        result['isSuccess'] = None
        result['content'] = ''
        try:
            req = requests.get(url)
        except requests.exceptions as e:
            result['isSuccess'] = False
            result['content'] = e
        else:
            result['isSuccess'] = True
            result['content'] = req.content
        return result
