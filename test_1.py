import requests
import datetime
import pytz

def av_value():
    timezone = pytz.timezone('Etc/GMT-3')
    date_time = int(datetime.datetime.now(timezone).timestamp() * 1000)
    response = requests.get('https://yandex.com/time/sync.json?geo=213')

    if response.status_code == 200:
        delta_time = int(response.json()["time"]) - date_time
        print(delta_time)
        return delta_time
    else:
        print(f"Ошибка: {response.status_code}")

timezone = pytz.timezone('Etc/GMT-3')
date_time = int(datetime.datetime.now(timezone).timestamp() * 1000)

response = requests.get('https://yandex.com/time/sync.json?geo=213')

if response.status_code == 200:
    delta_time = int(response.json()["time"]) - date_time
    print(f"Дельта мс: {delta_time}")

    print(response.text)
    times = datetime.timedelta(milliseconds=int(response.json()["time"]) + int(response.json()["clocks"]["213"]["offset"]))
    print(f"Время: {times.seconds // 3600:02}:{(times.seconds % 3600) // 60:02}")
    print("Временная зона: " + str(response.json()["clocks"]["213"]["name"]) + " " + str(response.json()["clocks"]["213"]["offsetString"]))

    sum = 0
    for i in range(0,5):
        sum += int(av_value())
    print(f"Средняя дельта мс:  {sum / 5}")

else:
    print(f"Ошибка: {response.status_code}")