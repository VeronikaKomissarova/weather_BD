import requests

class weather:

    def __init__(self, url, appid, city):
        self.url = url
        self.appid = appid
        self.city = city

    def get_data(self):
        r = requests.get(self.url, params={'q': self.city, 'appid': self.appid,
                                           'units': 'metric', 'lang': 'ru'})
        data = r.json()

        if data['cod'] == '200':
            print(data['city']['name'])
            data_sheet = []
            for i in data['list']:
                data_sheet.append([str(i['dt_txt']), str(i['main']['temp']), str(i['weather'][0]['description'])])
            return list(map(list, zip(*data_sheet)))
        else:
            return "Error" + data['cod']





