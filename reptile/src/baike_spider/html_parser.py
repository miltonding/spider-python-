from bs4 import BeautifulSoup
import re
import urllib.parse
import random
from baike_spider import img_node
from baike_spider import goods

class HtmlParser(object):

    def _handle_path(self, path):
        # 拼接 前后缀
        # full_url = urllib.parse.urljoin(href, page_url)
        # new_urls.add(full_url)

        if (path.startswith("//")):
            path = "https:" + path
        elif (path.startswith("/")):
            urlparse = urllib.parse.urlparse(path)
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse)
            path = domain + path

        return path


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #//item.jd.com/3907423.html
        # 爬取相关的，所以都是以"/"开头的相对地址, /item开头为词条
        #links = soup.find_all('a', href=re.compile(r"/item.jd.com/\w+.html"))
        links = soup.find_all('a', href=re.compile(r"/item.jd.com/\w+.html"))

        if (links is None or len(links) == 0):
            return None

        for link in links:
            href = link.get("href")
            if (href is not None and len(href) > 0):
                href = self._handle_path(href)
                new_urls.add(href)

        print (new_urls)
        return new_urls

    def _get_jdon_datas(self, page_url, soup):
        goods_node = goods.Goods()
        img_src = "https:" + soup.find('img', id="spec-img").get('data-origin').strip()
        chinese_name = soup.find('div', class_="item ellipsis").get_text().strip()
        describe = soup.find('div', class_="sku-name").get_text().strip()
        advantage = describe
        list_price = random.randint(1000,9999)
        goods_node.set_img_src(img_src)
        goods_node.set_chinese_name(chinese_name)
        goods_node.set_describe(describe)
        goods_node.set_advantage(advantage)
        goods_node.set_list_price(list_price)
        goods_node.set_in_sale(1)
        goods_node.set_is_delete(0)
        return goods_node


    def _get_new_datas(self, page_url, soup):
        datas = []
        images = soup.find_all('img')
        if (images is None or len(images) == 0):
            return None

        for image in images:
            node = img_node.ImgNode()
            src = image.get('src')
            if (src is not None):
                src = self._handle_path(src)

            node.set_src(src)
            node.set_title(image.get('title'))
            node.set_alt(image.get('alt'))
            datas.append(node)

        return datas

    def parse(self, page_url, html_cont):
        if (page_url is None or len(page_url) == 0 
            and html_cont is None or len(html_cont) == 0):
            return
        soup = BeautifulSoup(
                    html_cont,   #HTML文档字符串
                    'html.parser',    #HTML解析器,
                    from_encoding='utf-8'   #HTML文档的编码,
                    )
        new_urls = self._get_new_urls(page_url, soup)
        new_datas = None
        #new_datas = self._get_new_datas(page_url, soup)
        return new_urls, new_datas

    def parse_jdon(self, page_url, html_cont):
        if (page_url is None or len(page_url) == 0 
            and html_cont is None or len(html_cont) == 0):
            return
        soup = BeautifulSoup(
                    html_cont,   #HTML文档字符串
                    'html.parser',    #HTML解析器,
                    from_encoding='utf-8'   #HTML文档的编码,
                    )
        goods_node = self._get_jdon_datas(page_url, soup)
        return goods_node


