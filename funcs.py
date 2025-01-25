import distro
from colorama import init,Fore,Style
from os import system, chdir
from subprocess import run, Popen, PIPE, call
import subprocess
import select
import sys

get_distro = lambda :(distro.like())

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

def runc(command:list,log=True):
    if log:

        process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)

        try:
            is_error = False

            while True:
                ready_to_read, _, _ = select.select([process.stdout, process.stderr], [], [])

                for stream in ready_to_read:
                    if stream == process.stdout:
                        output = stream.readline()
                        if output:
                            print("Output:", output.strip())

                    elif stream == process.stderr:
                        error = stream.readline()
                        if error:
                            print("Error:", error.strip(), file=sys.stderr)
                            is_error = True

                if process.poll() is not None:
                    break

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        return_code = process.returncode
        return return_code


def runs(command):

    process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)

    try:
        while True:
            # خواندن خط به خط خروجی
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output, end="")  # نمایش خروجی
                sys.stdout.flush()  # اطمینان از چاپ فوری

        # بررسی خطاها
        stderr = process.stderr.read()
        if stderr:
            print("Error:", stderr, file=sys.stderr)

    except Exception as e:
        print(f'Error: {str(e)}')

    return process.returncode

def rund(cmd):
    print(cmd)
    c = call(cmd, shell=True)
    return c
    

def install(commands:dict):
    logo()
    logs_code = []
    is_cnt = True
    print(menu_render([f'install with {i}' for i in commands[get_distro()].keys()]))
    option = inpt()
    print(Fore.RESET)
    cmds = (commands[get_distro()][list(commands[get_distro()].keys())[option]])
    system('clear')
    print(Fore.MAGENTA + 'start installing ...' + Fore.RESET)
    for cmd in cmds:
        # if 'cd' in cmd:
        #     chdir(cmd[1])
        #     print(Fore.GREEN + f'installing {cmds.index(cmd) + 1}/{len(cmds) + 1} ...' + Fore.RESET)
        #     continue
        r = rund(cmd)
        if r == 0:
            print(Fore.GREEN + f'installed {cmds.index(cmd) + 1}/{len(cmds) + 1} ...' + Fore.RESET)
            print(Fore.BLUE + f'installing {cmds.index(cmd) + 2}/{len(cmds) + 1} ...' + Fore.RESET)
        else:
            ec = input(Fore.RED + 'is eror, continue or exit?[E/c] ==>')
            if ec == 'c' or ec == 'C':
                print(ec)
                is_cnt = True
            else:
                is_cnt = False
        logs_code.append(r)
        if is_cnt == True: pass
        else: break
    if any(log_code != 0 for log_code in logs_code):print(Fore.RED + 'eror in install')
    else:print(Fore.MAGENTA + 'completed install')

