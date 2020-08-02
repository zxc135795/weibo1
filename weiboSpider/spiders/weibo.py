import scrapy
from ..items import WeibospiderItem


class WeiboSpider(scrapy.Spider):
    key = input('z')
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = ['https://s.weibo.com/weibo?q={}&wvr=6&b=1&Refer=SWeibo_box'.format(key)]

    # 'https://s.weibo.com/weibo?q=%E7%BB%93%E6%9E%84%E5%8C%96%E9%9D%A2%E8%AF%95&wvr=6&b=1&Refer=SWeibo_box'
    def __init__(self):
        self.page = 0
        self.str_url = 'https://s.weibo.com/weibo?q={}&wvr=6&b=1&Refer=SWeibo_box&page={}'

    def get_url(self):
        return self.str_url.format(str(self.key), str(self.page))

    def start_requests(self):

        # cookies = 'login_sid_t=4c31c076bd364b1f7630222da84d27a1; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=9279943841377.037.1596256386770; SINAGLOBAL=9279943841377.037.1596256386770; ULV=1596256386794:1:1:1:9279943841377.037.1596256386770:; SUB=_2A25yIICwDeRhGeBL41QS8i7PwzmIHXVRV_V4rDV8PUNbmtANLVXjkW9NRt_LtIRth3qxFPs4qSq3Yh4IqvqY8b3L; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5-gORlmZoBIJLejPViRpxO5JpX5KzhUgL.Foqf1hq0eo501h-2dJLoIEXLxK-LB.qL1heLxK.L1-zLBKnLxKML1-eL12zLxKqL1KMLBK5LxK-LBo5L1Knt; SUHB=0A0JZ3nRsjmrmU; ALF=1627792479; SSOLoginState=1596256480; wvr=6; webim_unReadCount=%7B%22time%22%3A1596256495244%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A52%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined'
        cookies = 'SINAGLOBAL=9279943841377.037.1596256386770; _s_tentry=login.sina.com.cn; Apache=6195615720843.501.1596286452700; ULV=1596286452758:2:2:2:6195615720843.501.1596286452700:1596256386794; login_sid_t=725573570fda23696aeeeef2d9e6a2f3; cross_origin_proto=SSL; WBtopGlobal_register_version=87ad3767ffe59c8e; SCF=AmHUigRGb9naby8ygf7OdYUjIwY0ds3wQBE8BNcmAjF3sMNTGaeAZiubrznzGfatF_pjeBvquCY65_Ka1GIWc4g.; SUB=_2A25yIkCWDeRhGeBK4lQY-CbFzTmIHXVRVjVerDV8PUNbmtANLVDjkW9NRt_KJysCs66RH092EqO5OxE83kPM1p20; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56JCc_.f1SvTKD-.jHqXAX5JpX5KzhUgL.FoqX1Kq41hn4So-2dJLoIEzLxK-LBKBLBKzLxK.L1-2LBKnLxK-LB.qL1hSc9K-RSo.7; SUHB=0nl-xdnktzFg6c; ALF=1627874372; SSOLoginState=1596338374; wvr=6; UOR=,,graph.qq.com; webim_unReadCount=%7B%22time%22%3A1596338379674%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined'
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        # print(response.text)
        pages = response.xpath('.//ul[@class="s-scroll"]/li')
        print(pages)
        div = response.xpath('.//div[@class="card-wrap"]')
        print(len(div))
        num = 1
        item = WeibospiderItem()
        for v in div:
            # detail_url = v.xpath('.//div[@class="content"]/p[@class="txt"]/text()')
            detail_urls = v.xpath('.//div[@class="content"]/p')
            pinglun = v.xpath('.//div[@class="card-act"]/ul/li')
            # print(detail_urls)
            # sheet.write(num, 0, num)
            if len(detail_urls) == 2:
                text = detail_urls[0].xpath('./text()|./em/text()|./a/text()').extract()
                text = ''.join(text).strip()
                print(text)
                item['text'] = text
                # sheet.write(num, 1, text)
            elif len(detail_urls) > 2:
                text = detail_urls[1].xpath('./text()|./em/text()|./a/text()').extract()
                text = ''.join(text).strip()
                print(text)
                item['text'] = text
                # sheet.write(num, 1, text)
            if len(pinglun) == 4:
                shoucang = pinglun[0].xpath('./a/text()').extract()
                shoucang = ''.join(shoucang)
                print(shoucang)
                # sheet.write(num, 2, shoucang)
                zhuanfa = pinglun[1].xpath('./a/text()').extract()
                zhuanfa = ''.join(zhuanfa)
                print(zhuanfa)
                # sheet.write(num, 3, zhuanfa)
                pingl = pinglun[2].xpath('./a/text()').extract()
                pingl = ''.join(pingl)
                print(pingl)
                # sheet.write(num, 4, pingl)
                zan = pinglun[3].xpath('./a/@title|./a/em/text()').extract()
                zan = ''.join(zan)
                # sheet.write(num, 5, zan)
                print(zan)
                item['shoucang'] = shoucang
                item['pinglun'] = pingl
                item['zhuanfa'] = zhuanfa
                item['zan'] = zan
                item['id'] = num
                yield item
            num += 1

        self.page += 1
        if len(pages) > 0 and self.page <= len(pages):
            url = self.get_url()
            req = scrapy.Request(url, callback=self.parse)
            yield req
