def facebook():
    print("Hallo, wat is jou naam?")
    naam = input()
    print("Welkom", naam, "!")
    print("Mogen wij jou wat vragen? Ja/Nee")
    vraag = input().lower()
    if vraag == "nee":
        exit()
    if vraag == "ja":
        print("Top! Laten we beginnen.")
        print(naam, "hoe oud ben jij?")
        leeftijd = input()
        print("Oke, je bent dus", leeftijd, "Jaar")
        print("Waar woon jij?")
        woonplaats = input()
        print("Heb jij broers of zussen?")
        enigskind = input()
        print("Wat voor werk doe je?")
        werk = input()
        print("Oke, leuk dat je", werk, "als werk doet!")
        print("Dit was het programma, wil je opnieuw beginnen? ja/nee")
        opnieuw = input().lower()
        if opnieuw == "ja":
            return facebook()
        else:
            exit()

facebook()
