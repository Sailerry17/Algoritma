def KomperSuhu(suhu, dari="C", ke="R"):
    if (dari == "C" and ke == "R"):
        return 4/5 * suhu
    elif (dari == "R" and ke == "C"):
        return 5/4 * suhu
    elif (dari == "F" and ke == "R"):
        return 4/9 * (suhu - 32)
    elif (dari == "R" and ke == "F"):
        return 9/4 * suhu + 32
    elif (dari == "F" and ke == "C"):
        return 5/9 * (suhu -32)
    elif (dari == "C" and ke == "F"):
        return 9/5 * suhu - 32
    elif (dari == "R" and ke == "K"):
        return suhu + 273
    elif (dari == "K" and ke == "R"):
        return suhu - 273
    elif (dari == "C" and ke == "K"):
        return suhu + 273
    elif (dari == "K" and ke == "C"):
        return suhu - 273
    elif (dari == "F" and ke == "K"):
        return 5/9 * (suhu -32) + 273
    elif (dari == "K" and ke == "F"):
        return 9/5 * (suhu -273) + 32
    elif (dari == "R" and ke == "R"):
        return suhu
    elif (dari == "C" and ke == "C"):
        return suhu
    elif (dari == "F" and ke == "F"):
        return suhu
    elif (dari == "K" and ke == "K"):
        return suhu

print(KomperSuhu(100,"C","F"))
print(KomperSuhu(100,"F","C"))
print(KomperSuhu(100,"C","K"))
print(KomperSuhu(100,"K","C"))
print(KomperSuhu(100,"F","K"))
print(KomperSuhu(100,"K","F"))
print(KomperSuhu(100,"R","C"))
print(KomperSuhu(100,"C","R"))
print(KomperSuhu(100,"R","F"))
print(KomperSuhu(100,"F","R"))
print(KomperSuhu(100,"R","K"))
print(KomperSuhu(100,"K","R"))