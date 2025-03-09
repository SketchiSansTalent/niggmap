import nmap
import time
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(rf"""{Fore.MAGENTA}
.______   ____    ____                                              
|   _  \  \   \  /   /                                              
|  |_)  |  \   \/   /                                               
|   _  <    \_    _/                                                
|   |_)  |     |  |                                                  
|______/      |__|                                                  
                                                                    
     _______. __  ___  _______ .___________.  ______  __    __   __ 
    /       ||  |/  / |   ____||           | /      ||  |  |  | |  |
   |   (----`|  '  /  |  |__   `---|  |----`|  ,----'|  |__|  | |  |
    \   \    |    <   |   __|      |  |     |  |     |   __   | |  |
.----)   |   |  .  \  |  |____     |  |     |  `----.|  |  |  | |  |
|_______/    |__|\__\ |_______|    |__|      \______||__|  |__| |__|
            {Style.RESET_ALL}""")
    print(f"{Fore.CYAN}[ + ] If you need help or have a question (add me on discord)-> sketchi_i{Style.RESET_ALL}")

banner()

host = input(f"{Fore.YELLOW}Enter the IP Adress or the Host NAME to scan : {Style.RESET_ALL}")

nm = nmap.PortScanner()

print(f"{Fore.GREEN}Scanning {host}...{Style.RESET_ALL}")
nm.scan(host, '22-80')

print(f"\n{Fore.CYAN}Results of the can for {host}:{Style.RESET_ALL}")
print(f"{Fore.BLUE}Host: {nm[host].hostname()}{Style.RESET_ALL}")
print(f"{Fore.BLUE}State: {nm[host].state()}{Style.RESET_ALL}")
time.sleep(10)

for proto in nm[host].all_protocols():
    print(f"\n{Fore.MAGENTA}Protocol: {proto}{Style.RESET_ALL}")
    lport = nm[host][proto].keys()
    for port in sorted(lport):
        state = nm[host][proto][port]['state']
        color = Fore.GREEN if state == "open" else Fore.RED
        print(f"{Fore.YELLOW}Port: {port}\t{color}State: {state}{Style.RESET_ALL}")