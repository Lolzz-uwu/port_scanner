import socket
import os
import platform 
common_ports = [20,21,22,23,25 ,50,51,53,67,68,69,80,110,119,123,135,139,143,161,16,389,449,989,990,3389,443,554,1723]

def clearing():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
def scan(ip,port):
    try:
        sex = socket.socket()
        sex.settimeout(0.1)
        sex.connect((ip,port))
        print(f"{port} is open")
    except Exception:
        pass
    

def main():
    clearing()
    while True:
        print('''                  _                                          
                 | |                                         
 _ __   ___  _ __| |_   ___  ___ __ _ _ __  _ __   ___ _ __  
| '_ \ / _ \| '__| __| / __|/ __/ _` | '_ \| '_ \ / _ \ '__| 
| |_) | (_) | |  | |_  \__ \ (_| (_| | | | | | | |  __/ |    
| .__/ \___/|_|   \__| |___/\___\__,_|_| |_|_| |_|\___|_|    
| |                                                          
|_|      ''')
        print('1)scan for the most used ports(fast,sexy)\n2)scan for all 65535 ports(slow but scans for all ports)')
        m = input('[+]:')
        if m == '1':
            clearing()
            ip_addr = input('enter the ip of the target\n:')
            for word in common_ports:
                scan(ip_addr,word)


        elif m == '2':
            clearing()
            ip_addrs = input('enter the ip of the target\n:')
            for i in range(0,65535):
                scan(ip_addrs,i)
if __name__ == '__main__':           
    main()

            
