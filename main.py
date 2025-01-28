from funcs import menu_render, logo, inpt, inpterr, install, menu_main, execv, executable, argv

def main():
    last_menu = menu_main
    is_option = False
    noterr = True
    ismainmenu = True
    while True:
        if noterr:
            logo()
            ex = True
            try:
                if type(last_menu) == dict: print(menu_render(last_menu.keys(),ismainmenu))
                if type(last_menu) == list: print(menu_render(last_menu,ismainmenu))
                option = inpt()
            except Exception as e:
                option = inpterr()
                if option == 99: break
                if option == 98:execv(executable,['python'] + argv)
            if option == 99: break
            if option == 98:execv(executable,['python'] + argv)
        if type(last_menu) == dict:
            try:
                last_menu = last_menu[list(last_menu.keys())[option]]
            except Exception as e:
                option = inpterr()
                if option == 99: break
                if option == 98:execv(executable,['python'] + argv)
                noterr = False
            else: noterr = True
        if type(last_menu) == list:
            logo()
            print(menu_render(last_menu,ismainmenu))
            option = inpt()
            if option == 99: break
            if option == 98:execv(executable,['python'] + argv)
            try:
                install(last_menu[option])
            except KeyboardInterrupt: exit(0)
            except Exception as e:
                # option = inpterr()
                if option == 99: exit(0)
                if option == 98:execv(executable,['python'] + argv)
                noterr = False
            else: noterr == True
        ismainmenu = False

if __name__ == '__main__': main()