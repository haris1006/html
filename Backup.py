#!/usr/bin/python
import os, httplib
import colorama
from colorama import Fore, init
colorama.init()

cls = "cls"
os.system(cls)

class fg:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'
    
def banner():
    print(Fore.RED + "            .---.        .---.                                                 " + Fore.RESET)
    print(Fore.RED + "           /     \  __  /     \                                                " + Fore.RESET)
    print(Fore.RED + "          / /     \(  )/    \  \             Backup Finder            " + Fore.RESET)
    print(Fore.RED + "         //////   ' \/ `   \\\\\\\\\\\\            Made By BIBIL_0DAY" + Fore.RESET)
    print(Fore.RED + "        //// / // :    : \\\\ \ \\\\\\\\           Telegram T.me/spamworldpro           " + Fore.RESET)
    print(Fore.RED + "       // /   /  /`    '\  \   \ \\\\                                          " + Fore.RESET)
    print(Fore.RED + "      //          //..\\\\          \\\\                                       " + Fore.RESET)
    print(Fore.YELLOW + "             ====UU====UU====                                               " + Fore.RESET)
    print(Fore.YELLOW + "                 '//||\`                                                    " + Fore.RESET)
    print(Fore.YELLOW + "                   ''``                                                     " + Fore.RESET)
     
def clearing():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
banner()
website = raw_input('\n Enter Website >>>  ')
shells = ['/yedek.zip','/yedek.rar','/yedek.tar','/bak.zip','/bak.rar','/bak.tar','/backup.zip','/backup.rar','/backup.tar']
BIBILZX = []

for shell in shells:
    site = website.replace('http://','')
    host = site + shell
    conn = httplib.HTTPConnection(site)
    conn.connect()
    request = conn.request('GET',shell)
    response = conn.getresponse()
    if response.status == 200:
        print '\n\t[+] Backup found %s \n' %host
        BIBILZX.append(host)
    else:
        print '[-] Not Found %s ' %host
fpth = os.getcwd()
fpth2 = fpth + '/found.txt'
fob = open(fpth2,'w')
fob.close()
fob = open(fpth2,'a')
fob.writelines(BIBILZX)
exit()
