import requests


def send_get(url="https://ya.ru"):
    r = requests.get(url=url)
    data = r.json()
    code = r.status_code
    print(f"по адресу {url} получили код {code} с json = {data}")

url = "https://ostrovok.ru/api/site/multicomplete.json?query=Таганрог&locale=ru"
send_get(url)
send_get()