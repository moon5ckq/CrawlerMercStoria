from pyquery import PyQuery as pq
import urllib

base_url = u'http://xn--cckza4aydug8bd3l.gamerch.com'

ele_urls = [
    'http://xn--cckza4aydug8bd3l.gamerch.com/%E7%82%8E',
    'http://xn--cckza4aydug8bd3l.gamerch.com/%E6%B0%B4',
    'http://xn--cckza4aydug8bd3l.gamerch.com/%E9%A2%A8',
    'http://xn--cckza4aydug8bd3l.gamerch.com/%E5%85%89',
    'http://xn--cckza4aydug8bd3l.gamerch.com/%E9%97%87'
]

for url in ele_urls:
    d = pq(url = url)
    for tb in d('[id^=ui_wikidb_table]'):
        for tr in d(tb)('tr')[1:]:
            name = d(tr)('td:nth-child(2) a').attr('href')
            print base_url + '/' + urllib.urlencode({'':name[1:].encode('utf-8')})[1:]
