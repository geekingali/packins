from funcs import install

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
            'yay (recommended)' : [['lss -S firefox-nightly']],
            'git' : [
                ['sudo pacman -S --needed git'],
                ['git clone https://aur.archlinux.org/firefox-nightly.git'],
                ['cd firefox-nightly'],
                ['makepkg -si']
                ]
        },
        'other' : {
            '.tar.xz' : [['las -ltrha']]
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