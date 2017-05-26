from baike_spider import url_manager
from baike_spider import html_downloader
from baike_spider import html_parser
from baike_spider import html_outputer

class SpiderMain(object):
    def __init__(self):
        # url管理器 
        self.urls = url_manager.UrlManager()
        # 下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 解析器
        self.parser = html_parser.HtmlParser()
        # 输出器
        self.outputer = html_outputer.OutPuter()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print ('craw %d : %s' % (count, new_url))
                #  Get html
                html_cont = self.downloader.get_html(new_url)

                # DOM Tree parse
                new_urls, new_datas = self.parser.parse(new_url, html_cont)
                print ("new_urls %s" % len(new_urls))
                print ("new_datas %s" % new_datas)

                # 添加新的url
                self.urls.add_new_urls(new_urls)

                # 收集数据
                self.outputer.collect_goods(new_urls)
    
                count = count + 1
            except:
                print ("craw failed")

        # 最后输出所有数据
        datas = self.outputer.output_html()

        # 下载图片
        self.downloader.download_image(datas)


# _name_为内置属性 没有import的_name_为main
if __name__ == "__main__":
    root_url = "https://search.jd.com/Search?keyword=%E6%98%BE%E7%A4%BA%E5%B1%8F&enc=utf-8&wq=%E5%B9%B3%E6%9D%BF&pvid=1ddee0f5fc6e4439a43407cc1a5acf59"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)