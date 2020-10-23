from PIL import Image
number = 1000
while number > 0:
    number -= 1
    print(number)
if number == 0:
     afbeelding = Image.open("among-us-3.jpg")
     afbeelding.show()
