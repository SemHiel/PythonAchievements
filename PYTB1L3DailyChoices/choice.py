import time


def dailychoices():
    print('Welkom, wat is jou naam?')
    naam = input()
    print('Welkom,', naam, 'Laten we beginnen.')
    time.sleep(1)
    print("(1) Als je alarm gaat, ga je dan gelijk je bed uit of niet? ja/nee")
    choice = input().lower()
    if choice == 'ja':
        print("Top, vroege vogel dus.")
    elif choice == 'nee':
        print("Daar herken ik mezelf in!")
    else:
        print(choice, " Is geen keuze.")
    print('(2) Ga je eerst douchen of eten?')
    choice2 = input().lower()
    if choice2 == ('douchen'):
        print('Top! Dat doe ik ook.')
    elif choice2 == ('eten'):
        print('Lekker toch.')
    else:
        print(choice2, " is geen keuze.")
    print('(3) Heb je je tas al in de avond ingepakt of niet? ja/nee')
    choice3 = input().lower()
    if choice3 == ('ja'):
        print('Top! Ik ook.')
    elif choice3 == ('nee'):
        print('Kost wel tijd in de ochtend.')
    else:
        print(choice3, " is geen keuze.")
    print("Wil je het programma herhalen? ja/nee")
    keuze = input().lower()
    if keuze == 'ja':
        return dailychoices()
    elif keuze == 'nee':
        print('Het programma word afgesloten.')
    else:
        print('Het programma word afgesloten.')

dailychoices()
