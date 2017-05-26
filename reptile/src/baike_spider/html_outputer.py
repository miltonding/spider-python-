class OutPuter(object):
    def __init__(self):
        self.datas = []

    def collect(self, new_datas):
        if (new_datas is None or len(new_datas) == 0):
            return

        for data in new_datas:
            self.datas.append(data)

    def collect_goods(self, new_datas):
        self.datas.append(new_datas)

    def output_html(self):
        datas = []
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write("<html>")

        fout.write("  <head>")
        fout.write("  </head>")

        fout.write("  <body>")
        fout.write("    <table>")

        entry_id = 84
        count = 1
        for data in self.datas:
            #print(data.get_src().encode('utf-8'))
            #.encode('utf-8').decode('gbk', 'ignore')
            fout.write("  <tr>")
            template = """
                INSERT INTO `goods`(productid, brand, entryid, chinese_name, english_name,
                     goods_describe, goods_advantage, unit_cost,
                     list_price, in_sale, is_delete,
                     attr_one, attr_two, attr_three, weight)
                VALUES (6, null, %d, '%s', null, 
                      '%s', '%s', null, 
                      %d, 1, 0, 
                      null, null, null, null 
                      );
            """
            sql = template % (entry_id, data.get_chinese_name(),
                               data.get_describe(), data.get_advantage(),
                               data.get_list_price())
            fout.write("    <td>%s</td>" % sql)
            fout.write("  <tr>")
            datas.append(data.get_img_src())
            #fout.write("    <td>%s</td>" % data.get_img_src())
            fout.write("  </tr>")
            count = count + 1
            entry_id = entry_id + 1

        fout.write("    </table>")
        fout.write("  </body>")

        fout.write("</html>")
        fout.close()
        return datas
