def family():
    print("Welkom bij het family programma!")
    print("Wat is jou naam?")
    naam = input()
    print("Aangenaam,", naam, "Zullen we beginnen? Ja/Nee")
    doorgaan = input().lower()
    if doorgaan == "nee":
        exit()
    if doorgaan == "ja":
        print("hoeveel leden heeft jou familie?")
        leden = input()
        print("Wie is het oudste in jou familie?")
        oudste = input()
        print("Wie is het jongste in je familie?")
        jongste = input()
        print("Hoe oud ben jij?")
        leeftijd = input()
        print("Waar woon jij?")
        woonplaats = input()
        print("Mijn naam is", naam, "Ik ben", leeftijd, "jaar oud en", "ik woon in", woonplaats, ". Mijn familie heeft", leden, "leden.", "De oudste in mijn familie is", oudste, ", de jongste in mijn familie is", jongste)
        print("Wil je het programma herhalen? ja/nee")
        herhalen = input()
        if herhalen == "ja":
            return family()
        if herhalen == "nee":
            exit()


family()
