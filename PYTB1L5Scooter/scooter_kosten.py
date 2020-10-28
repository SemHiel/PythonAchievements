verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2

km_per_maand = input("Hoeveel kilometer rij jij per maand?\n")

def bereken_maandkosten(km_per_maand):

    try:
        km_per_maand = float(km_per_maand)
        maandkosten = ((km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand)
        print("Maandelijkse Kosten:", maandkosten)
        return km_per_maand

    except ValueError:
        print("Input is not valid.")
        km_per_maand = input("Hoe veel KM rij je per maand?\n")
        bereken_maandkosten(km_per_maand)

bereken_maandkosten(km_per_maand)
