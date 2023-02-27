import string

def to_Morse_Code(str):
    newStr =  ""
    for c in str:
        c.lower()
        if c == "a":
            newStr+= "._ "
        elif c == "b":
            newStr+= "_... "
        elif c == "c":
            newStr+= "_._. "
        elif c == "d":
            newStr+= "_.. "
        elif c == "e":
            newStr+= ". "
        elif c == "f":
            newStr+= ".._. "
        elif c == "g":
            newStr+= "__. "
        elif c == "h":
            newStr+= ".... "
        elif c == "i":
            newStr+= ".. "
        elif c == "j":
            newStr+= ".___ "
        elif c == "k":
            newStr+= "_._ "
        elif c == "l":
            newStr+= "._.. "
        elif c == "m":
            newStr+= "__ "
        elif c == "n":
            newStr+= "_. "
        elif c == "o":
            newStr+= "___ "
        elif c == "p":
            newStr+= ".__. "
        elif c == "q":
            newStr+= "__._ "
        elif c == "r":
            newStr+= "._. "
        elif c == "s":
            newStr+= "... "
        elif c == "t":
            newStr+= "_ "
        elif c == "u":
            newStr+= ".._ "
        elif c == "v":
            newStr+= "..._ "
        elif c == "w":
            newStr+= ".__ "
        elif c == "x":
            newStr+= "_.._ "
        elif c == "y":
            newStr+= "_.__ "
        elif c == "z":
            newStr+= "__.. "
        elif c == " ":
            newStr+= "/"
        elif c == "\n":
            return newStr
    return newStr

str = input("Please enter a string" + '\n')
print(to_Morse_Code(str))
