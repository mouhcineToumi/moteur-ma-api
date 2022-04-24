
from pymoteurma.helpers import sanitize
from pymoteurma.static_crawler import StaticCrawler
import fuckit


class MoteurDetails( StaticCrawler ):
    
    def __init__(self):
        super().__init__()
    
    @sanitize
    @fuckit
    def parse(self, html):
        d = {}
        d['title'] = html.find(class_="header_detail").find('h1').text.split('à')[0].strip()
        d['price'] = html.find(class_="header_detail").find(class_="price-block").text
        d['path'] = list( map( lambda x: x.text, html.find(class_="breadcrumb").find_all('li')) )
        
        props = html.find_all(class_="detail_line")
        for prop in props:
            spans = prop.find_all('span')
            d[spans[0].text] = spans[1].text
            
            
        tags = html.find_all(class_="option_ad")
        d['tags'] = list(map( lambda x: x.text.replace('✔  ', ''), tags))
        
        d['description'] = html.find(class_="options").find(class_="col-md-12").text
        
        author_section = html.find('div', {'id': 'overview'})
        d['author_url'] = author_section.find('a', href=True).get('href')
        d['verified_num'] = author_section.find(class_="icon icon-normal-checkbox-checked").parent.text
        d['expired'] = author_section.find(class_="alert alert-warning").text
        return d
    
    def run(self, url):
        html = self.get_html(url)
        return {**self.parse( html ), **{'url': url}}