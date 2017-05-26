# 网页下载器
# from urllib.request import urlopen
import urllib.request
import os

url = "https://www.baidu.com";

# 第一种方法
#response = urllib.request.urlopen(url)
#print (response.getcode())
#html = response.read()
#print (html)
#print (len(html))

# 第二种方法
request = urllib.request.Request(url)
# 添加头部信息
#request.add_header("user-agent", "Mozilla/5.0")
response = urllib.request.urlopen(request)  
the_page = response.read()
print (the_page)
#urllib.request.urlretrieve("https://imgsa.baidu.com/forum/w%3D580/sign=911e2ce4db00baa1ba2c47b37710b9b1/0ae6baa1cd11728b49336d2ac2fcc3cec2fd2c86.jpg",
                           #'%s.jpg' % "1")
filename = os.path.basename("https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&quality=80&size=b150_150&subsize=20480&cut_x=0&cut_w=0&cut_y=0&cut_h=0&sec=1369815402&srctrace&di=84043b37bab12c50faff5f3a0cc8b529&wh_rate=null&src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2Faec379310a55b319380291c141a98226cefc178e.jpg")
filename = filename.replace("%", "").replace("?", "").replace("&", "").replace("=", "")
print(filename)
if (len(filename) > 24):
    print (filename[-24:])
    
url1 = 'https://gss0.bdstatic.com/6LZ1dD3d1sgCo2Kml5_Y_D3/sys/portrait/item/6d846b6f6d41545355e6b7a1e5ae9a894b'
file_suffix = os.path.splitext(url1)[1]
print (file_suffix)
