import components.urls as url
import components.frog as api

dones = api.call(url.projects('Done'))['projects']
currents = api.call(url.projects('Current'))['projects']
print('======== DONEs : is this archivable?')
api.print_oldest_projects(dones)
print('======== CURRENTs : is this alive?')
api.print_oldest_projects(currents)
