import os, time, webbrowser

from colorama import Fore, Style, Back

print ('\n')
def res():
    print(Style.RESET_ALL)

os.system('clear')

print('Welcome to Termux!')
print('\n')
print('Community forum: https://termux.com/community')
print('Gitter chat:     https://gitter.im/termux/termux')
print('IRC channel:     #termux on libera.chat')
print('\n')
print('Working with packages:')
print('\n')
print(' * Search packages:   pkg search <query>')
print(' * Install a package: pkg install <package>')
print(' * Upgrade packages:  pkg upgrade')
print('\n')
print('Subscribing to additional repositories:')
print('\n')
print(' * Root:     pkg install root-repo')
print(' * X11:      pkg install x11-repo')
print('\n')
print('Report issues at https://termux.com/issues')
print('\n')
while True:
    tsu = input('$ ')
    if tsu == '':
        os.system
