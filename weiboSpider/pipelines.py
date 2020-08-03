# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import Workbook


# class TuniuPipeline(object):
#     def __init__(self):
#         # 创建excel，填写表头
#         self.wb = Workbook()
#         self.ws = self.wb.active
#         self.ws.append(['用户id', 'source', 'raw_txt', 'txt', ])  # 设置表头
#
#     def process_item(self, item, spider):  # 具体内容
#
#         line = [item['id'], item['source'], item['raw_text'], item['text']]  # 把数据中项整理出来
#         self.ws.append(line)  # 将数据需要保存的项以行的形式添加到xlsx中
#         self.wb.save(r'D:\pycharm\爬虫\csv\web.xlsx')  # 保存xlsx文件
#         return item


class WeibospiderPipeline:
    def __init__(self):
        # 创建excel，填写表头
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['用户id', 'text', '转发', '收藏', '评论', '点赞', ])  # 设置表头

    def process_item(self, item, spider):  # 具体内容

        line = [item['id'], item['text'], item['zhuanfa'], item['shoucang'], item['pinglun'], item['zan']]  # 把数据中项整理出来
        self.ws.append(line)  # 将数据需要保存的项以行的形式添加到xlsx中
        self.wb.save(r'F:\pyfiles\pachong\test001\weiboSpider\weiboSpider\{}.xlsx'.format(item['key']))  # 保存xlsx文件
        return item
