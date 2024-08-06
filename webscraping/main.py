import requests
from bs4 import BeautifulSoup as bs

github_user = input('input github user: ')
url = 'https://github.com/'+github_user
r = requests.get(url)

if r.status_code == 200:
    soup = bs(r.content, 'html.parser')
    avatar_img = soup.find('img', {'alt': 'Avatar'})

    if avatar_img:
        profile_image = avatar_img['src']
        print(profile_image)
    else:
        print('profile image not found')
else:
    print(f'Failed to retrieve page with status code:{r.status_code}')
