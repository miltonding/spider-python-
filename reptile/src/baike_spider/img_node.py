'''
Created on 2017年5月17日

@author: milton.ding
'''
class ImgNode(object):
    def __init__(self):
        pass

    def set_title(self, title):
        self.title = title

    def get_title(self):
        if (self.title is None or len(self.title) == 0):
            return ""
        return self.title

    def set_src(self, src):
        self.src = src

    def get_src(self):
        if (self.src is None or len(self.src) == 0):
            return ""
        return self.src
    
    def set_alt(self, alt):
        self.alt = alt

    def get_alt(self):
        if (self.alt is None or len(self.alt) == 0):
            return ""
        return self.alt
