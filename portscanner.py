from socket import *
import sys

from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('PORT!', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])

import time
startTime = time.time()

if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)
   
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
print('Time taken:', time.time() - startTime)
