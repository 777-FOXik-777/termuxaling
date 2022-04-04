import os, time, webbrowser

from colorama import Fore, Style, Back

print ('\n')
def res():
    print(Style.RESET_ALL)

os.system('cd')
os.system('clear')
print(' ')
print('Welcome to Termux!')
print(' ')
print('Community forum: https://termux.com/community')
print('Gitter chat:     https://gitter.im/termux/termux')
print('IRC channel:     #termux on libera.chat')
print(' ')
print('Working with packages:')
print(' ')
print(' * Search packages:   pkg search <query>')
print(' * Install a package: pkg install <package>')
print(' * Upgrade packages:  pkg upgrade')
print(' ')
print('Subscribing to additional repositories:')
print('\n')
print(' * Root:     pkg install root-repo')
print(' * X11:      pkg install x11-repo')
print(' ')
print('Report issues at https://termux.com/issues')
print(' ')


while True:
    tsu = input('$ ')
    if tsu == '':
        os.system
    else:
        print('No command '+tsu+' found, did you mean:')
        print('Command '+tsu+'lik in package sypex')
        print('Command d'+tsu+'s in package hak')
        print('Command '+tsu+'h in package garem')
