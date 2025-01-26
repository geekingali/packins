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

inpt = lambda:int(input(Fore.YELLOW + '[enter number] ===> '))

menu_render = lambda menu: ''.join(f'{Fore.GREEN}[{i}] : {m}\n' for i, m in enumerate(menu)) + Fore.CYAN + '[99] : Exit \n'

def rund(cmd):
    c = call(cmd, shell=True)
    return c
    
def install(commands:dict):
    logo()
    logs_code = []
    is_cnt = True
    print(menu_render([f'install with {i}' for i in commands[like()()].keys()]))
    option = inpt()
    print(Fore.RESET)
    cmds = (commands[like()()][list(commands[like()()].keys())[option]])
    system('clear')
    print(Fore.MAGENTA + 'start installing ...' + Fore.RESET)
    for cmd in cmds:
        if 'cd' in str(cmd):
            chdir(str(cmd[0].split(' ')[1:])[2:-2].replace(',','').replace('\'','').replace('"',''))
            print(Fore.GREEN + f'installing {cmds.index(cmd) + 1}/{len(cmds) + 1} ...' + Fore.RESET)
            continue
        r = rund(cmd)
        if r == 0:
            print(Fore.GREEN + f'installed {cmds.index(cmd) + 1}/{len(cmds) + 1} ...' + Fore.RESET)
            print(Fore.BLUE + f'installing {cmds.index(cmd) + 2}/{len(cmds) + 1} ...' + Fore.RESET)
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

