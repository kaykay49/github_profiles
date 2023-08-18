import requests
from requests.exceptions import HTTPError
from django.contrib.auth.models import User
from django.utils import timezone

def Fetch(user):
	try:
		response1=requests.get('https://api.github.com/users/'+str(user.username)).json()
		response2=requests.get(f'https://api.github.com/users/{user.username}/repos').json()
	except:
		print('An error ocuured while fetching user data!')
	else:
		return {'profile':response1,'repos':response2}

def Store(user):
	data=Fetch(user)
	user.Profile.followers=data['profile']['followers'] 
	user.Profile.last_updated=timezone.now()
	user.Profile.save()
	for repo in data['repos']:
		user.Profile.repository_set.create(name=repo['name'],stars=repo['stargazers_count'])

def update(user):
	for repo in user.Profile.repository_set.all():
		repo.delete()
	Store(user)