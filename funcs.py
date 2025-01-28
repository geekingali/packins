from distro import like,info
from colorama import init,Fore
from os import system, chdir, getcwd, execv
from subprocess import call
from sys import executable, argv
from json import load

with open('menu.json') as f:
    menu_main = load(f)


def logo():
    system('clear')
    init()
    print(Fore.LIGHTRED_EX + '''


    ░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓███████▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
                                                                            
                                                                            
    ''')

def inpterr():
    try:
        return int(input(Fore.LIGHTRED_EX + '\n[Please enter a whole number][to exit : 99] ===> '))
    except: return inpterr()

def getlike():
    dis = info()
    dis = dis['id'] + dis['like']
    if 'debian' in dis or 'ubuntu' in dis:
        return 'debian'
    if 'arch' in dis:
        return 'arch'
    else:
        return 'other'

def inpt():
    try:
        return int(input(Fore.LIGHTYELLOW_EX + '[enter number] ===> '))
    except:
        return inpterr()

def menu_render(menu,ismainmenu=False):
    if menu == []: return Fore.LIGHTMAGENTA_EX + '[!] : installation method not found.\n\n' + Fore.LIGHTGREEN_EX + '\n[98] : back to menu.\n' + Fore.LIGHTCYAN_EX + '[99] : Exit \n'
    ismenu = ''
    if not ismainmenu:
        ismenu = Fore.LIGHTMAGENTA_EX + '\n[98] : back to menu.\n'
    return ''.join(f'{Fore.LIGHTGREEN_EX}[{i}] : {m}\n' for i, m in enumerate(menu)) + ismenu + Fore.LIGHTCYAN_EX + '[99] : Exit \n'

def run(cmd):
    try:
        c = call(cmd, shell=True)
        return c
    except KeyboardInterrupt:
        ec = input(Fore.LIGHTMAGENTA_EX + '\n installing canceled,' + Fore.LIGHTCYAN_EX +' are you to reinstall[N/y] ===>')
        print(Fore.RESET)
        if ec == 'y' or ec == 'Y':
            system('clear')
            r = run(cmd)
            return r
        else:
            return 'c'

def install(name:str,option=0,noterr=True):
    try:
        with open('install.json') as f:
            commands = (load(f)[name])
    except:
            print(Fore.LIGHTMAGENTA_EX + '==> installation method not found.\n\n' + Fore.LIGHTMAGENTA_EX + '\n[98] : back to menu.\n' + Fore.LIGHTCYAN_EX + '[99] : Exit \n')
    if noterr:
        logo()
        logs_code = []
        is_cnt = True
        try:
            print(menu_render([f'install with {i}' for i in commands[getlike()].keys()]))
        except:
            print(Fore.LIGHTMAGENTA_EX + '==> installation method not found.\n\n' + Fore.LIGHTMAGENTA_EX + '\n[98] : back to menu.\n' + Fore.LIGHTCYAN_EX + '[99] : Exit \n')
        option = inpt()
        if option == 98:execv(executable,['python'] + argv)
    try:
        cmds = (commands[getlike()][list(commands[getlike()].keys())[option]])
    except:
        if option == 99: exit(0)
        else:
            noterr = False
            option = inpterr()
            if option == 99: exit(0)
            install(name,option,False)
    else: noterr = True
    system('clear')
    print(Fore.LIGHTMAGENTA_EX + 'start installing ...' + Fore.RESET)
    for cmd in cmds:
        if 'cd' in str(cmd):
            chdir(str(cmd[0].split(' ')[1:])[2:-2].replace(',','').replace('\'','').replace('"',''))
            print(Fore.LIGHTGREEN_EX + f'installing {cmds.index(cmd) + 1}/{len(cmds) + 1} ...' + Fore.RESET)
            continue
        r = run(cmd)
        if r == 0:
            print(Fore.LIGHTGREEN_EX + f'installed {cmds.index(cmd) + 1}/{len(cmds) + 1} ...' + Fore.RESET)
            print(Fore.LIGHTBLUE_EX + f'installing {cmds.index(cmd) + 2}/{len(cmds) + 1} ...' + Fore.RESET)
        elif r == 'c':
            print(Fore.LIGHTBLUE_EX + 'installing canceled by user')
            if input(f'\n{Fore.LIGHTYELLOW_EX}Want to back menu(Y/n) : ') in {'n','N'}: exit(0)
            else: execv(executable,['python'] + argv)
        else:
            print(Fore.LIGHTRED_EX + '\neror in install\n')
            if input(f'\n{Fore.LIGHTYELLOW_EX}Want to back menu(Y/n) : ') in {'n','N'}: exit(0)
            else: execv(executable,['python'] + argv)
    else:
        print(Fore.LIGHTMAGENTA_EX + 'completed install')
    if input(f'\n{Fore.LIGHTYELLOW_EX}Want to back menu(Y/n) : ') in {'n','N'}: exit(0)
    else: execv(executable,['python'] + argv)

