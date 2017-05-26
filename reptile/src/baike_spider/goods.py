'''
Created on 2017年5月23日

@author: milton.ding
'''
class Goods(object):
    def __init__(self):
        pass

    def set_img_src(self, img_src):
        self.img_src = img_src

    def get_img_src(self):
        if (self.img_src is None or len(self.img_src) == 0):
            return ""
        return self.img_src

    def set_chinese_name(self, chinese_name):
        self.chinese_name = chinese_name

    def get_chinese_name(self):
        if (self.chinese_name is None or len(self.chinese_name) == 0):
            return ""
        return self.chinese_name

    def set_describe(self, describe):
        self.describe = describe

    def get_describe(self):
        if (self.describe is None or len(self.describe) == 0):
            return ""
        return self.describe
    
    def set_advantage(self, advantage):
        self.advantage = advantage

    def get_advantage(self):
        if (self.advantage is None or len(self.advantage) == 0):
            return ""
        return self.advantage

    def set_list_price(self, list_price):
        self.list_price = list_price

    def get_list_price(self):
        return self.list_price

    def set_in_sale(self, in_sale):
        self.in_sale = in_sale

    def get_in_sale(self):
        return self.in_sale
    
    def set_is_delete(self, is_delete):
        self.is_delete = is_delete

    def get_is_delete(self):
        return self.is_delete