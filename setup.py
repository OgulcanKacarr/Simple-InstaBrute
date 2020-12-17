from colorama import Fore, Back, Style
from termcolor import colored, cprint
import colorama
import time
import os


colorama.init()
print(Fore.GREEN)
os.system("python -m pip install --upgrade pip")
print(Fore.RED)
os.system("sudo apt-get install python3-pip")
print(Fore.GREEN)
os.system("pip install selenium && pip3 install selenium")
print(Fore.RED)
os.system("pip install colorama && pip3 install colorama")
print(Fore.GREEN)
os.system("pip install termcolor && pip3 install termcolor")
print(Fore.RED)
os.system("pip install wget && pip3 install wget")
print(Fore.GREEN)
os.system("apt-get install libnss3-dev -y")
os.system("apt-get install libgconf-2-4 -y")
