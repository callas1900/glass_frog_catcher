import components.urls as url
import components.frog as api

count = 0
currents = []
dones = []
waitings = []
futures = []

circles = api.call(url.circles())['circles']
for circle in circles:
    api.print_circle(circle)
    projects = api.call(url.projects().format(circle_id = circle['id']))['projects']
    for project in projects:
        count += 1
        api.print_project(count, project)
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
api.print_oldest_projects(currents)
