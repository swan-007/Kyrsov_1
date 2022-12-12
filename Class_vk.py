import requests
from datetime import datetime


class vk:
    user_id_1 = []
    file_info = {}
    silka = []
    file_information = {}

    def __init__(self, user_id, token, version='5.131'):
        self.token = token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def user_ids(self):
        url = 'https://api.vk.com/method/users.get'
        para = {'user_ids': self.id
                }
        respons = requests.get(url, params={**self.params, **para})
        x = respons.json()
        y = x['response'][0]['id']
        vk.user_id_1.append(y)

    def _get_pho(self):

        url = 'https://api.vk.com/method/photos.get'
        para = {'owner_id': vk.user_id_1[0],
                'album_id': 'profile',
                'rev': 1,
                'extended': 1,
                'count': 1,
                'photo_sizes': 1
                }
        respons = requests.get(url, params={**self.params, **para})
        x = respons.json()
        f = x['response']['items'][0]['sizes']
        for i in f:
            if i['type'] == 'z':
                vk.silka.append(i['url'])
                vk.file_information["size"] = i['type']
        file = vk.silka[0]
        like = x['response']['items'][0]['likes']['count']
        date = x['response']['items'][0]['date']
        unix = int(date)
        dttime = datetime.utcfromtimestamp(unix).strftime('%d-%m-%Y')

        vk.file_info = {'file': file,
                        'like': like,
                        'date': dttime}
