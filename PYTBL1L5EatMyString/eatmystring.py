str = "Hallo ik ben een string en ik wordt opgegeten"

def destroyString():
    newStr = str[0:len(str)-1]
    print(str)
    destroyString()


destroyString()
