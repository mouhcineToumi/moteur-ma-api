
import requests
from moteurmapy.helpers import string_to_soup

class StaticCrawler:
    
    def __init__(self):
        pass
    
    def get_html(self, url):
        r = requests.get(url)
        return string_to_soup(r.content)