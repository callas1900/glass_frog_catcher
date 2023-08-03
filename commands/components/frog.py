import os
import urllib3
import json
import datetime 
import dateutil.parser

http = urllib3.PoolManager()
def call(url):
    r = http.request( 'GET', url, headers={ 'Content-Type': 'application/json', 'X-Auth-Token': os.environ['GLASS_FLOG_TOKEN'] })
    return json.loads(r.data.decode('utf-8'))

def print_circle(circle):
    if len(circle['links']['roles']) > 0: 
        print('='*20)
        print('[', circle['name'], '](', circle['id'], ')')

def print_project(count, project):
    print('*', count, '[projects]',' <----- ' + project['description'], '[(' + project['status'] +'),' + project['created_at'] + ']')

def print_oldest_projects(currents):
    currents = sorted(currents, key=lambda d:d['created_at'])
    rank_count = 1
    for project in currents[:5]:
        timestamp = dateutil.parser.parse(project['created_at'])
        print(rank_count, '[', timestamp.strftime("%Y/%m/%d"), ']', project['description'])
        rank_count += 1



