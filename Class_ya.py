import requests
import Class_vk
import json


class yandex:
    base_host = 'https://cloud-api.yandex.net/'
    name_d = []

    def __init__(self, token: str):
        self.token = token

    def _hea(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def check_path_2(self):
        uri = 'v1/disk/resources?'
        path = "path=DZ_9"
        request_url = self.base_host + uri + path
        response = ((requests.get(request_url, headers=self._hea()))).ok
        if response is True:
            return
        else:
            uri = 'v1/disk/resources?'
            path = "path=DZ_9"
            request_url = self.base_host + uri + path
            response_2 = requests.put(request_url, headers=self._hea())

    def check_2(self):
        tt = Class_vk.vk.file_info['date']
        uur = str(Class_vk.vk.file_info['like'])
        nam_list = []
        uri = 'v1/disk/resources?'
        path = "path=DZ_9"
        request_url = self.base_host + uri + path
        response = (requests.get(request_url, headers=self._hea())).json()
        x = response['_embedded']['items']
        for i in x:
            nam_list.append(i["name"])
        name_path = nam_list
        if uur in name_path:
            name = (f"like- {uur}  ") + (f'upload date- {tt}')
            yandex.name_d.append(name)

        else:
            name = Class_vk.vk.file_info['like']
            yandex.name_d.append(name)

    def zag_2(self):
        name = str(yandex.name_d[0])
        uri = 'v1/disk/resources/upload/'
        path = 'DZ_9/' + name
        request_url = self.base_host + uri
        url = Class_vk.vk.file_info['file']
        params = {'path': path, 'url': url}
        respons = requests.post(request_url, params=params, headers=self._hea())
        Class_vk.vk.file_information["file_name"] = name
        j = json.dumps(Class_vk.vk.file_information)
        print(j)
