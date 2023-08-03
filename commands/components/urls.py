URL_API = 'https://api.glassfrog.com/api/v3/'
def circles():
    return URL_API + 'circles'
def projects():
    return circles() + '/{circle_id}/projects'
