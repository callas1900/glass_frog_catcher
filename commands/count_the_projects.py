import datetime 
import dateutil.parser
import components.urls as url
import components.frog as api

def print_circle(circle):
    if len(circle['links']['roles']) > 0: 
        print('='*20)
        print('[', circle['name'], '](', circle['id'], ')')

def print_project(count, project):
    print('*', count, '[projects]',' <----- ' + project['description'], '[(' + project['status'] +'),' + project['created_at'] + ']')


count = 0
currents = []
dones = []
waitings = []
futures = []

circles = api.call(url.circles())['circles']
for circle in circles:
    print_circle(circle)
    projects = api.call(url.projects().format(circle_id = circle['id']))['projects']
    for project in projects:
        count += 1
        print_project(count, project)
        if project['status'] == 'Current':
            currents.append(project)
        if project['status'] == 'Done':
            dones.append(project)
        if project['status'] == 'Waiting':
            waitings.append(project)
        if project['status'] == 'Future':
            futures.append(project)

print('C:', len(currents), 'D:', len(dones), 'W:', len(waitings), 'F:', len(futures))
# rank
currents = sorted(currents, key=lambda d:d['created_at'])
rank_count = 1
for project in currents[:5]:
    timestamp = dateutil.parser.parse(project['created_at'])
    print(rank_count, '[', timestamp.strftime("%Y/%m/%d"), ']', project['description'])
    rank_count += 1



