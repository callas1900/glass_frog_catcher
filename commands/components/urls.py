URL_API = 'https://api.glassfrog.com/api/v3/'
def circles():
    return URL_API + 'circles'
def projects_circles():
    return circles() + '/{circle_id}/projects'
def projects(status = 'All'):
    url = URL_API + 'projects'
    if 'Done' == status:
        return url + '?status=Done'
    elif 'Current' == status:
        return url + '?status=Current'
    else:
        return url
