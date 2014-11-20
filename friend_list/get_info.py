from pyquery import PyQuery as pq
import urllib
import sys

with open(sys.argv[1]) as f:
    for url in f:
        print url.strip()
        d = pq(url = url.strip())
        print d('#js_wikidb_main_name').text()
        
        sys.exit(0)