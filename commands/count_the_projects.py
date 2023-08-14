import components.urls as url
import components.frog as api

count = 0
status_count = {}
currents = []

circles = api.call(url.circles())['circles']
for circle in circles:
    api.print_circle(circle)
    projects = api.call(url.projects().format(circle_id = circle['id']))['projects']
    for project in projects:
        count += 1
        api.print_project(count, project)
        if project['status'] in status_count: 
            status_count[project['status']] += 1
        else:
            status_count[project['status']] = 1

print(status_count)
#api.print_oldest_projects(currents)
