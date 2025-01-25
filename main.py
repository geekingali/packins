from config import menu_main
from funcs import menu_render, logo, inpt

last_menu = menu_main
is_option = False
while True:
    logo()
    if type(last_menu) == dict: print(menu_render(last_menu.keys()))
    if type(last_menu) == str: print('last_menu')
    option = inpt()
    if option == 99: break
    if type(last_menu) == dict:
        last_menu = last_menu[list(last_menu.keys())[option]]
    if type(last_menu) != dict:
        last_menu()
        break
