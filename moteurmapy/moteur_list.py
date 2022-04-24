
from moteurmapy.helpers import sanitize
from moteurmapy.static_crawler import StaticCrawler
import fuckit
from urllib.parse import urlparse
from urllib.parse import parse_qs


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
    
    @fuckit
    def get_page_count(self, html):
        d = {}
        # get total page count
        page_count = html.find('div', {'id': 'label-recherche-auto'}).find('span').text.split('sur')[-1].strip().split(' ')[0]
        d['page_count'] = int(page_count)

        # get next page number
        pages = html.find(class_="pagination").find_all('a')
        next_page = list(filter( lambda x: x.text.strip() == 'Suivante', pages))[0]
        parsed = urlparse(next_page.get('href'))
        captured_value = parse_qs(parsed.query)['per_page'][0]
        d['next_page'] = 1+int(captured_value)//15
        return d
    
    
    def run(self, url):
        html = self.get_html(url)
        page_count = self.get_page_count(html)
        items = html.find_all(class_="row-item")
        data = list(map( self.parse, items))
        return data, page_count
    