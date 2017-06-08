import sys
import time

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('hilt', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
cprint(figlet_format('text', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
cprint(figlet_format('adventure', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])

print('Hello. You are about to enter a deep, dark forest called the digital humanities!!!!!!!!')
#you can wait a second - google this
time.sleep(5)
print('Choose your weapon. You may pick one of these things:')
time.sleep(5)
print('1.Tony the cat, 2. A can of lacroix, or 3. Wayne')
#set answers dictionary
#answers1 = {'1': 'Tony the Cat', '2': 'A can of Lacroix', '3': 'Wayne'}
#set initial hitpoints
hp = 30
choice1 = input('Make your choice! 1, 2, or 3? : ')

if choice1 == 1:
    print('You chose Tony the Cat')
elif choice1 == 2:
    print ('you chose a can of lacroix')
else
    print('You are dead'):

#if choice 1==1 something
