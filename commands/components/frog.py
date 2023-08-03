import os
import urllib3
import json

http = urllib3.PoolManager()
def call(url):
    r = http.request( 'GET', url, headers={ 'Content-Type': 'application/json', 'X-Auth-Token': os.environ['GLASS_FLOG_TOKEN'] })
    return json.loads(r.data.decode('utf-8'))
