def fakti(sayi):
    if sayi == 1:
        return 1
    else:
        return sayi * fakti(sayi - 1)

print(fakti(5))
