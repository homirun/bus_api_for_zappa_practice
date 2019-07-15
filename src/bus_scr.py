# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
from collections import deque
import collections


def get_timetable(place):
    html = urllib.request.urlopen("http://www.teu.ac.jp/campus/access/2019_0408_1bus.html")
    soup = BeautifulSoup(html, "lxml")
    res = ''
    if place == "hm":
        res = soup.find("table").find("tbody").findAll("tr")
    elif place == "h":
        res = soup("table")[1].find("tbody").findAll("tr")
    elif place == "gk":
        res = soup("table")[2].find("tbody").findAll("tr")
    array = []
    bus = []
    counter = 0

    for i in res:
        array.append(i.get_text())

    queue = deque(array)
    queue.popleft()

    array = []  # array再初期化

    for i in range(len(queue)):
        array.append(queue[i].replace('\n',''))

    for i in array:
        counter += 1
        data = collections.OrderedDict()
        if i[:1] != "～":
            data["Campus"] = i[0:5]
            data["Station"] = i[5:10]
            data["CampusEnd"] = i[10:15]
        else:   # シャトル運行時
            data["Campus"] = "Shuttle"
            data["Station"] = "Shuttle"
            data["CampusEnd"] = "Shuttle"

        bus.append(data)

    counter = 0
    final = collections.OrderedDict()
    final["Bus"] = bus
    return final


if __name__ == "__main__":
    print(get_timetable("hm"))
