stutterlist = ''

def stutter():
    print("Welkom bij het stutter programm!")
    print("Zullen we beginnen? ja/nee")
    beginnen = input()
    if beginnen == "ja":
        s = input("Type een random zin. \n")
        stutterlist.append(s)


stutter()
