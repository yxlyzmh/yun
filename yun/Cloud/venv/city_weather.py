import  requests


class HeFeng():

    def __init__(self):
        self.url="https://cdn.heweather.com/china-city-list.txt"
        self.encoding='utf8'
        self.pre_request="https://free-api.heweather.net/s6/weather/now?location="
        self.sub_request="&key=30bfb68c37bb4ca78601591050e65ef0"

    def today_weather(self,city_code):
        dict=self.get_weather(city_code)
        print(dict["HeWeather6"][0]['now'])

    def get_weather(self,city_code):
        url=self.pre_request+city_code+self.sub_request
        #url="https://free-api.heweather.net/s6/weather/now?location="+city_code+"&key=30bfb68c37bb4ca78601591050e65ef0"
        info=requests.get(url)
        info.encoding=self.encoding
        return info.json()
        #print(info.text)

    def get_city_code(self):
        cities=self.get_citys()
        for each in cities:
            yield each[2:13]

    def get_citys(self):
        html = requests.get(self.url)
        html.encoding = 'utf8'
        cities=html.text.split('\n')
        return cities[6:]


if __name__ == '__main__':
    hefeng = HeFeng()
    #hefeng.get_city_code()
    #for each in hefeng.get_citys():
    codes=hefeng.get_city_code()
    for i in range(10):
        #dict=hefeng.get_weather(codes.__next__())
        hefeng.today_weather(codes.__next__())