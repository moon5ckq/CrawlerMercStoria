# -*- coding: utf-8 -*-  
from pyquery import PyQuery as pq
import urllib
import sys, os
import json

#KB 体力*耐久*0.005

def save_file(path, url):
    filepath = os.path.join(path, url.strip().split('/')[-1])
    urllib.urlretrieve(url, filepath)
    return filepath

def parse_int(s):
    if s.isdigit():
        return int(s)
    return -1

with open(sys.argv[1]) as f:
    for url in f:
        d = pq(url = url.strip())
        
        name = d('#js_wikidb_main_name').text()
        norm = map(lambda x:d(x).text().split(' ')[-1], d('.ui_wikidb_top_area p'))
        attr = map(lambda x: d(x).text().split(' ')[-1], d('.ui_wikidb_middle_area p'))
        correction = map(lambda x: parse_int(x.strip().split()[-1]), \
            d('.ui_wiki_db_bottom_wrapper  .db_other_text:first').text().strip('%').split('%'))
        q_avatar = save_file( 'q_avatar', d('.db_other_text a').attr('href') )
        m_avatar = save_file( 'm_avatar', d('.ui_wiki_db_main_img_area a').attr('href') )
        fr = {
            'name' : name,
            'country' : norm[0],
            'rarity' : int(norm[1][1]),
            'type' : norm[2],
            'dev_type' : norm[3],
            'weapon' : norm[4],
            'atk_type' : norm[5],
            'atk_nums' : int(norm[6][0]),
            'attr' : {
                'hp' : int(attr[0]),
                'speed' : int(attr[3]),
                'range' : int(attr[4]),
                'atk' : int(attr[8]),
                'cd' : float(attr[11]),
                'toughness' : int(attr[12])
            },
            'correction' : correction,
            'q_avatar' : q_avatar,
            'm_avatar' : m_avatar
        }
        print json.dumps(fr)
