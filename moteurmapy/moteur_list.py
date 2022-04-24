
from moteurmapy.helpers import sanitize
from moteurmapy.static_crawler import StaticCrawler
import fuckit


class MoteurList( StaticCrawler ):
    
    def __init__(self):
        super().__init__()
    
    @sanitize
    @fuckit
    def parse(self, html):
        d = {}
        d['url'] = html.find(class_="slide", href=True).get('href')
        d['title'] = html.find(class_="title_mark_model").text
        d['price'] = html.find(class_="price").text
        d['model_year'] = html.find(class_="icon-normal-calendar-month").parent.text
        d['city'] = html.find(class_="icon-normal-pointer").parent.text
        d['fuel'] = html.find(class_="icon-fuel").parent.text
        return d
    
    def run(self, url):
        html = self.get_html(url)
        items = html.find_all(class_="row-item")
        data = list(map( self.parse, items))
        return data