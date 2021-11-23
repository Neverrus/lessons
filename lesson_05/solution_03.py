"""
Написать функцию, которая используя модуль requests скачивает файл сохраняет его на файловой системе, функция имеет два параметра: ссылка на файл и имя на файловой системе. В качестве примера ссылки на файл можно использовать лицензию из ГитХаба из вашего репозитория:
"""

import requests

def req_func(savefile, linkfile):

    f=open(savefile,"wb")

    ufr = requests.get(linkfile)

    f.write(ufr.content)

    f.close()

req_func(savefile="/home/never/Trash/LICENSE.txt", linkfile="https://raw.githubusercontent.com/Neverrus/lessons/master/LICENSE2.txt")
