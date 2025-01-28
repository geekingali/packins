from distro import like,info
from colorama import init,Fore
from os import system, chdir, getcwd
from subprocess import call

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
    dis = 'solus'
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

# menu_render = lambda menu: ''.join(f'{Fore.LIGHTGREEN_EX}[{i}] : {m}\n' for i, m in enumerate(menu)) + Fore.LIGHTCYAN_EX + '[99] : Exit \n'
def menu_render(menu):
    print(menu)
    return ''.join(f'{Fore.LIGHTGREEN_EX}[{i}] : {m}\n' for i, m in enumerate(menu)) + Fore.LIGHTCYAN_EX + '[99] : Exit \n'

def run(cmd):
    try:
        c = call(cmd, shell=True)
        return c
    except KeyboardInterrupt:
        ec = input(Fore.LIGHTMAGENTA_EX + '\n installing canceled, are you LIGHTRED_EXy to reinstall[N/y] ===>')
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
    try:
        print(menu_render([f'install with {i}' for i in commands[getlike()].keys()]))
    except:
        print(Fore.YELLOW + '[!] : installation method not found.' + Fore.RESET)
        print(menu_render(['back to menu']))
        if inpt() == 0: main()
        else: exit(0)
    option = inpt()
    print(Fore.RESET)
    try:
        cmds = (commands[getlike()][list(commands[getlike()].keys())[option]])
    except :
        if option == 99: exit(0)
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
            exit(0)
        else:
            ec = input(Fore.LIGHTRED_EX + 'is eror, continue or exit?[E/c] ==>')
            if ec == 'c' or ec == 'C':
                is_cnt = True
            else:
                is_cnt = False
        logs_code.append(r)
        if is_cnt == True: pass
        else: break
    if any(log_code != 0 for log_code in logs_code):print(Fore.LIGHTRED_EX + 'eror in install')
    else:print(Fore.LIGHTMAGENTA_EX + 'completed install')


def Edge(): 
    install({
    'arch' : {
        'yay' : [
            ['yay -S aur/microsoft-edge-dev-bin']
            ],
        'git' : [
            ['sudo pacman -S --needed git'],
            ['git clone https://aur.archlinux.org/microsoft-edge-stable-bin.git'],
            ['cd microsoft-edge-stable-bin'],
            ['makepkg -si']
            ]
        }
    })
def FireFox(): 
    install({
        'arch' : {
            'pacman (recommended)' : [['sudo -S firefox']],
            'yay' : [['yay -S firefox']]
        },
        'debian' : {
            'apt' : [['sudo apt install firefox']]
        }
    })
def FirefoxDeveloper():
    install({
        'arch' : {
            'pacman (recommended)' : [['sudo pacman -S firefox-developer-edition']],
            'yay' : [['yay -S firefox-developer-edition']]
        }
    })
def FirefoxNightly():
    install({
        'arch' : {
            'yay (recommended)' : [['yay -S firefox-nightly']],
            'git' : [
                ['sudo pacman -S --needed git'],
                ['git clone https://aur.archlinux.org/firefox-nightly.git'],
                ['cd firefox-nightly'],
                ['makepkg -si']
                ]
        },
        'other' : {
        }
    })
def FirefoxLTS():
    install({
        'arch' : {
            'yay (recommended)' : [['yay -S firefox-esr-bin']],
            'git' : [
                ['sudo pacman -S --needed git'],
                ['git clone https://aur.archlinux.org/firefox-esr-bin.git'],
                ['cd firefox-esr-bin'],
                ['makepkg -si']
                ]
        }
    })
def FireFoxBeta():
    install({
        'arch' : {
            'yay (recommended)' : [['yay -S firefox-esr-bin']],
            'git' : [
                ['sudo pacman -S --needed git'],
                ['git clone https://aur.archlinux.org/firefox-beta-bin.git'],
                ['cd firefox-beta-bin'],
                ['makepkg -si']
                ]
        }
    })
def Chrome():pass
def Oblivion(): pass
def Nekobox(): pass
def Inshot(): pass
def Editor(): pass
def Wave(): pass
def Warp(): pass
def Ranger(): pass
def Kitti(): pass
def Vscode(): pass
def Vscodium(): pass
def Yay() : pass
def Debtap():
    install({
        'arch': {
            'yay (recommended)' : [
                ['yay -S aur/debtap'],
                ['sudo debtap -u']
            ],
            'git' : [
                ['sudo pacman -S git base-devel'],
                ['git clone https://aur.archlinux.org/debtap.git'],
                ['cd debtap'],
                ['makepkg -si'],
                ['sudo debtap -u']
            ]
        }
    })
menu_main = {
    'Network' : {
        'Browsers' : {
            'Edge' : Edge,
            'FireFox' : {
                'Firefox (recommended)' : FireFox,
                'Firefox Developer' : FirefoxDeveloper,
                'Firefox Nightly' : FirefoxNightly,
                'Firefox LTS' : FirefoxLTS,
                'FireFox Beta' : FireFoxBeta
            },
            'Chrome' : Chrome
            },
        'VPN & PROXY' : {
            'Oblivion' : Oblivion,
            'Nekobox' : Nekobox
        }
        },
    'Media' : {
        'Photo' : {
            'Inshot' : Inshot,
            'Editor' : Editor
            }
        },
    'Terminal' : {
        'Wave' : Wave,
        'Warp' : Warp,
        'Ranger' : Ranger,
        'Kitti' : Kitti
        },
    'Development' : {
        'Vscode' : Vscode,
        'Vscodium' : Vscodium
        },
    'softwares' : {
        'Yay' : Yay,
        'Debtap' : Debtap
    }
    }

def main():
    last_menu = menu_main
    is_option = False
    while True:
        logo()
        ex = True
        if type(last_menu) == dict:
            print(menu_render(last_menu.keys()))
        try:
            option = inpt()
        except Exception as e:
            option = inpterr()
            if option == 99: exit(0)
        if option == 99: exit(0)
        if type(last_menu) == dict:
            last_menu = last_menu[list(last_menu.keys())[option]]
        if type(last_menu) != dict:
            last_menu()
            exit(0)

if __name__ == '__main__': main()