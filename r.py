# Source Generated with Decompyle++
# File: codeboy1877_reverse.pyc (Python 3.8)

from urllib3.util.retry import Retry
import requests
from requests.adapters import HTTPAdapter
import sys
import random
import requests
import threading
import os
import os.path as os
import threading
import json
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init, Style
import os
import requests
import threading
from multiprocessing.dummy import Pool, Lock
from bs4 import BeautifulSoup
import time
import smtplib
import sys
import ctypes
from time import sleep
from random import choice
from colorama import Fore
from colorama import Style
from colorama import init
import re
import requests
import subprocess
import hashlib
import os
import re
import requests
import ctypes
from colorama import Fore, init
from multiprocessing.dummy import Pool
from random import choice

def removed():
    os.system('')
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    removed()

def nothing():
    import datetime
    dat = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    sp = dat.split('/')[1]
    if sp == '09':
        exit()
    else:
        removed()

init(True, **('autoreset',))
os.system('cls' if os.name == 'nt' else 'clear')
hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
config = '$'.join(hwid)
id = hashlib.md5(config.encode('utf')).hexdigest()
id = str(id)
print('Your ID Has Been Activated\nMy Telegram Account : @CodeBoy1877')
print(id)
print('\n\n\n   /$$    /$$$$$$  /$$$$$$$$ /$$$$$$$$       /$$$$$$$$                               \n /$$$$   /$$__  $$|_____ $$/|_____ $$/      |__  $$__/                               \n|_  $$  | $$  \\ $$     /$$/      /$$/          | $$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$ \n  | $$  |  $$$$$$/    /$$/      /$$/           | $$ /$$__  $$ |____  $$| $$_  $$_  $$\n  | $$   >$$__  $$   /$$/      /$$/            | $$| $$$$$$$$  /$$$$$$$| $$ \\ $$ \\ $$\n  | $$  | $$  \\ $$  /$$/      /$$/             | $$| $$_____/ /$$__  $$| $$ | $$ | $$\n /$$$$$$|  $$$$$$/ /$$/      /$$/              | $$|  $$$$$$$|  $$$$$$$| $$ | $$ | $$\n|______/ \\______/ |__/      |__/               |__/ \\_______/ \\_______/|__/ |__/ |__/\n                                                                                                                                                                                                                                         \nBy : CodeBoy1877 // My Telegram Channel : @CodeBoy1877x // 1877 Team Channel : @x1877x\n\n1.IP To Domain\n')
select = input('Just Write Number 1 >> : ')
if select == '1':
    
    def cut(text, leng = ('', False)):
        if leng == False:
            ret = text
        else:
            length_string = len(text)
            if length_string > leng:
                ret = text[0:leng]
            else:
                neko = leng - length_string
                ret = text + ' ' * neko
        return str(ret)

    
    def revip(target):
        pass
    # WARNING: Decompyle incomplete

    print('{}Reverse IP Choiced'.format(Fore.GREEN))
    print('')
    target = open(input(Fore.WHITE + 'IP File.txt >> : '), 'r').read().replace('http://', '').replace('https://', '').splitlines()
    Thread = input(Fore.WHITE + 'Thread >> : ')
    pool = ThreadPool(int(Thread))
    pool.map(revip, target)
    pool.close()
    pool.join()
    print('===============================')
    count_result = len(open('Domains.txt').readlines())
    print('Result >> : ' + str(count_result))
removed()
