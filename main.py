from menu import menu_main
from funcs import menu_render, logo, inpt, inpterr, install

def main():
    last_menu = menu_main
    is_option = False
    noterr = True
    while True:
        if noterr:
            logo()
            ex = True
            try:
                if type(last_menu) == dict: print(menu_render(last_menu.keys()))
                if type(last_menu) == list: print(menu_render(last_menu))
                option = inpt()
            except Exception as e:
                option = inpterr()
                if option == 99: break
            if option == 99: break
        if type(last_menu) == dict:
            try:
                last_menu = last_menu[list(last_menu.keys())[option]]
            except Exception as e:
                option = inpterr()
                if option == 99: break
                noterr = False
            else: noterr = True
        if type(last_menu) == list:
            logo()
            print(menu_render(last_menu))
            option = inpt()
            if option == 99: break
            try:
                install(last_menu[option])
            except:
                option = inpterr()
                if option == 99: break
                noterr = False
            else: noterr == True

if __name__ == '__main__': main()