# Inteligent Wordlist Generator
#
# By: Online Hacking [SUMAN MONDAL]
# Goblin Wordlist Generator
# Version: 2.0
#
#
##################

import itertools


ban = '''

                                                    '''

print('''\033[91m

██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║   
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║   
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║   
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝   
          OnlineHacking (SUMAN) 
''')
print('''\033[91m

   ____        _ _              _    _            _    _             
  / __ \      | (_)            | |  | |          | |  (_)            
 | |  | |_ __ | |_ _ __   ___  | |__| | __ _  ___| | ___ _ __   __ _ 
 | |  | | '_ \| | | '_ \ / _ \ |  __  |/ _` |/ __| |/ / | '_ \ / _` |
 | |__| | | | | | | | | |  __/ | |  | | (_| | (__|   <| | | | | (_| |
  \____/|_| |_|_|_|_| |_|\___| |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |
                                                                __/ |
                                                               |___/ 
    
''')
print('''\033[91m

\e[1m          \e[1;91m [\e[1;96m*\e[1;91m] \e[1;97mYouTube  \e[1;91m= \e[5m \e[1;97mOnline Hacking  

\e[5m         \e[25m \e[1;91m [\e[1;96m*\e[1;91m] \e[1;97mWebsite  \e[1;91m=  \e[4m\e[1;97mwww.OnlineHacking-net.com\e[24m   

\e[1m          \e[1;91m [\e[1;96m*\e[1;91m] \e[1;97mTelegram \e[5m\e[1;91m=  \e[1;97m@OnlineHacking   \e[93m   


''')

scale = input('\033[36m[!] provide a size scale [eg: "1 to 8" = 1:8] : ')
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])

use_nouse = str(input("\n\033[36m[?] Do you want to enter personal data ? [y/N]: "))
if use_nouse == 'y':
	first_name = str(input("\n\033[36m[*] Fist Name: "))
	last_name = str(input("\n\033[36m[*] Last Name: "))
	birthday = str(input("\n\033[36m[*] Birthday: "))
	month = str(input("\n\033[36m[*] Month: "))
	year = str(input("\n\033[36m[*] Year: "))
	chrs = first_name + last_name + birthday + month + year
else:
	chrs = 'abcdefghijklmnopqrstuvwxyz'
	pass

chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numerics = '1234567890'

file_name = input('\n\033[36m[!] Insert a name for your wordlist file: ')
arq = open(file_name, 'w')
if input('\n\033[36m[?] Do you want to use uppercase characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_up])
if input('\n\033[36m[?] Do you want to use special characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_specials])
if input('\n\033[36m[?] Do you want to use numeric characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_numerics])

for i in range(start, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()
