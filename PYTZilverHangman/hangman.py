import random
import time

name = input("Welkom, wat is jou naam?: ")
print("Welkom " + name + "! Veel geluk!")
time.sleep(2)
print("Het spel begint nu...\n")
time.sleep(2)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_again
    secret_word = ["voetbal", "aardig", "vrienden", "sporten", "uitgaan", "drinken", "viezerik"]
    word = random.choice(secret_word)
    length = len(word)
    count = 0
    display = '*' * length
    already_guessed = []
    play_again = ""


def again_play():
    global play_again
    play_again = input("Wil je het spel opnieuw spelen?? ja of nee?\n").lower()
    if play_again == "ja":
        main()
    elif play_again == "nee":
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_again
    limit = 3
    guess = input("Dit is het woord " + display + " Gok maar!: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("1 letter tegelijk en geen nummers!\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "*" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Je hebt deze letter al geprobeerd, probeer een ander!\n")

    else:
        count += 1

        if count == 1:
            print("Fout! " + str(limit - count) + " kansen\n")
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif count == 2:
            print("Fout! " + str(limit - count) + " kansen\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif count == 3:
            print("Fout! Je hebt verloren\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            again_play()

    if word == '*' * length:
        print("Gefeliciteerd! Je hebt het geraden.")
        again_play()

    elif count != limit:
        hangman()


main()


hangman()
