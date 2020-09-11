import time

class statistics:
    naam = ' Player-Name: Sem Hiel\n'
    power = 'SuperPower: Insane Strenght\n'
    strengt = 1000
    lives = 21
    level = 1000
    height = 1.92
    print('Welkom bij de player statistics')
    time.sleep(1)
    playerstat = input('Wil je de speler statistiscs zien? (ja/nee): ').lower()
    if playerstat == "ja":
        print(naam, power, "Strenght level:", strengt, "\n" " Amount of lives:", lives,"\n" " Level:", level, "\n" " Groote:", height)
