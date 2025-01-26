from distro import like
from colorama import init,Fore
from os import system, chdir, getcwd
from subprocess import call

def logo():
    system('clear')
    init()
    print(Fore.RED + '''


    ░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓███████▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
                                                                            
                                                                            
    ''')

def getlike():
    if 'debian' in like() or 'ubuntu' in like():
        return 'debian'
    if 'arch' in like():
        return 'arch'

def inpt():
    try:
        return int(input(Fore.YELLOW + '[enter number] ===> '))
    except:
        return int(input(Fore.RED + '[Please enter a whole number][to exit : 99] ===> '))

# inpt = lambda:int(input(Fore.YELLOW + '[enter number] ===> '))

menu_render = lambda menu: ''.join(f'{Fore.GREEN}[{i}] : {m}\n' for i, m in enumerate(menu)) + Fore.CYAN + '[99] : Exit \n'

def run(cmd):
    try:
        c = call(cmd, shell=True)
        return c
    except KeyboardInterrupt:
        ec = input(Fore.MAGENTA + '\n installing canceled, are you redy to reinstall[N/y] ===>')
        print(Fore.RESET)
        if ec == 'y' or ec == 'Y':
            system('clear')
            r = run(cmd)
            return r
        else:
            return 'c'

def install(commands:dict):
    logo()
    logs_code = []
    is_cnt = True
    print(menu_render([f'install with {i}' for i in commands[getlike()].keys()]))
    option = inpt()
    print(Fore.RESET)
    cmds = (commands[getlike()][list(commands[getlike()].keys())[option]])
    system('clear')
    print(Fore.MAGENTA + 'start installing ...' + Fore.RESET)
    for cmd in cmds:
        if 'cd' in str(cmd):
            chdir(str(cmd[0].split(' ')[1:])[2:-2].replace(',','').replace('\'','').replace('"',''))
            print(Fore.GREEN + f'installing {cmds.index(cmd) + 1}/{len(cmds) + 1} ...' + Fore.RESET)
            continue
        r = run(cmd)
        if r == 0:
            print(Fore.GREEN + f'installed {cmds.index(cmd) + 1}/{len(cmds) + 1} ...' + Fore.RESET)
            print(Fore.BLUE + f'installing {cmds.index(cmd) + 2}/{len(cmds) + 1} ...' + Fore.RESET)
        elif r == 'c':
            print(Fore.BLUE + 'installing canceled by user')
            exit(0)
        else:
            ec = input(Fore.RED + 'is eror, continue or exit?[E/c] ==>')
            if ec == 'c' or ec == 'C':
                is_cnt = True
            else:
                is_cnt = False
        logs_code.append(r)
        if is_cnt == True: pass
        else: break
    if any(log_code != 0 for log_code in logs_code):print(Fore.RED + 'eror in install')
    else:print(Fore.MAGENTA + 'completed install')

