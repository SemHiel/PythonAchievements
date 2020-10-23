import random
stoel = 0
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)
for w in people:
    stoel += 1
    if w == "Waldo":
        print(people)
        print('Waldo is op stoel', stoel, 'Gevonden!')
        break
