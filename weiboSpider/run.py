# ProjectName:Ltest001
# FileName:run
# author:asus
# datetime:2020/8/2 10:02
# software: PyCharm
from scrapy import cmdline
name = 'weibo'
cmd = 'srcapy crawl {0}'.format(name)

cmdline.execute(cmd.split())
