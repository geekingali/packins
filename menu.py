from installer import *

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