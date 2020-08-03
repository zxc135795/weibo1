# ProjectName:Ltest001
# FileName:run
# author:asus
# datetime:2020/8/2 10:02
# software: PyCharm
from scrapy import cmdline
name = 'weibo'
cmd = 'srcapy crawl {0}'.format(name)

cmdline.execute(cmd.split())
'SINAGLOBAL=9279943841377.037.1596256386770; _s_tentry=login.sina.com.cn; Apache=6195615720843.501.1596286452700; ULV=1596286452758:2:2:2:6195615720843.501.1596286452700:1596256386794; login_sid_t=725573570fda23696aeeeef2d9e6a2f3; cross_origin_proto=SSL; WBtopGlobal_register_version=87ad3767ffe59c8e; SCF=AmHUigRGb9naby8ygf7OdYUjIwY0ds3wQBE8BNcmAjF3sMNTGaeAZiubrznzGfatF_pjeBvquCY65_Ka1GIWc4g.; SUB=_2A25yIkCWDeRhGeBK4lQY-CbFzTmIHXVRVjVerDV8PUNbmtANLVDjkW9NRt_KJysCs66RH092EqO5OxE83kPM1p20; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56JCc_.f1SvTKD-.jHqXAX5JpX5KzhUgL.FoqX1Kq41hn4So-2dJLoIEzLxK-LBKBLBKzLxK.L1-2LBKnLxK-LB.qL1hSc9K-RSo.7; SUHB=0nl-xdnktzFg6c; ALF=1627874372; SSOLoginState=1596338374; wvr=6; UOR=,,graph.qq.com; webim_unReadCount=%7B%22time%22%3A1596338379674%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined'

'SINAGLOBAL=9279943841377.037.1596256386770; _s_tentry=login.sina.com.cn; Apache=6195615720843.501.1596286452700; ULV=1596286452758:2:2:2:6195615720843.501.1596286452700:1596256386794; Ugrow-G0=589da022062e21d675f389ce54f2eae7; login_sid_t=725573570fda23696aeeeef2d9e6a2f3; cross_origin_proto=SSL; SSOLoginState=1596338374; wvr=6; UOR=,,graph.qq.com; WBStorage=42212210b087ca50|undefined; wb_view_log=1920*10801; crossidccode=CODE-yf-1K2r5M-2d9CEU-r4JbM0MJcdyJk1A0edda1; SCF=AmHUigRGb9naby8ygf7OdYUjIwY0ds3wQBE8BNcmAjF36_0AjwdsbQkJN37byldF0Tidb2lnUDXt3CuZOaTVkZc.; SUB=_2A25yI_PZDeRhGeBK4lQY-CbFzTmIHXVRWWIRrDV8PUNbmtANLUWjkW9NRt_KJ2kdkccjzrgRtwgCLxzQ4ejRaAwu; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56JCc_.f1SvTKD-.jHqXAX5JpX5KzhUgL.FoqX1Kq41hn4So-2dJLoIEzLxK-LBKBLBKzLxK.L1-2LBKnLxK-LB.qL1hSc9K-RSo.7; SUHB=0U1ZaNcQpZOjsN; ALF=1627961096; wb_view_log_6496988965=1920*10801; YF-Page-G0=d30fd7265234f674761ebc75febc3a9f|1596425101|1596425101; webim_unReadCount=%7B%22time%22%3A1596425103169%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7'