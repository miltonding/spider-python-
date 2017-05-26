from bs4 import BeautifulSoup
import re
from baike_spider import img_node

html_doc = """
<html>
  <head>
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    <link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索"> 
    <link rel="icon" sizes="any" mask="" href="//www.baidu.com/img/baidu.svg">
    <link rel="dns-prefetch" href="//s1.bdstatic.com"></link>
    <link rel="dns-prefetch" href="//t1.baidu.com">
    <link rel="dns-prefetch" href="//t2.baidu.com">
    <link rel="dns-prefetch" href="//t3.baidu.com">
    <link rel="dns-prefetch" href="//t10.baidu.com">
    <link rel="dns-prefetch" href="//t11.baidu.com">
    <link rel="dns-prefetch" href="//t12.baidu.com">
    <link rel="dns-prefetch" href="//b1.bdstatic.com">
    <title>百度一下，你就知道</title>
  </head>
  <body>
    <img src="1" title="123"/>
    <img src="2"/>
    <img />
  </body>
</html>
"""

soup = BeautifulSoup(
                    html_doc,   #HTML文档字符串
                    'html.parser',    #HTML解析器,
                    from_encoding='utf-8'   #HTML文档的编码,
                    ) 
imgs = soup.find_all('img');

count = 0
datas = []
for img in imgs:
    src = img.get("src")
    img = img_node.ImgNode()
    img.set_src(src)
    datas.append(img)

for img in datas:
    print (img.get_src())
    # 正则表达式
#node = soup.find_all('a', href=re.compile(r"baidu"));
#print ("正则表达式")
#print (node)