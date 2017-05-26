import urllib.request
import os
class HtmlDownloader(object):

    def get_html(self, url):
        if (url is None or len(url) == 0):
            return None

        request = urllib.request.Request(url)
        # 添加头部信息
        #request.add_header("user-agent", "Mozilla/5.0")
        response = urllib.request.urlopen(request)
        if (response.getcode() != 200):
            return None
        html_content = response.read()
        response.close()
        return html_content

    def download_image(self, datas):
        if (datas is None or len(datas) == 0):
            return
        count = 0
        for data in datas:
            url = data.get_src()
            if (len(url) > 0):
                # Get file name
                #filename = os.path.basename(url)
                # Download
                print("正在下载第%d张" % count)
                # 使用绝对路径
                folder_path = "G:/spider_img"
                urllib.request.urlretrieve(url, '%s/%s.jpg' % (folder_path, count))
                count = count+ 1

        print("全部下载成功到%s！" % folder_path)

    def download_gooods_image(self, datas):
        if (datas is None or len(datas) == 0):
            return
        count = 1
        for data in datas:
            url = data;
            if (len(url) > 0):
                # Get file name
                #filename = os.path.basename(url)
                # Download
                print("正在下载第%d张" % count)
                # 使用绝对路径
                folder_path = "G:/goods"
                urllib.request.urlretrieve(url, '%s/%s.jpg' % (folder_path, count))
                count = count+ 1

        print("全部下载成功到%s！" % folder_path)