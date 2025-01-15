def decimal(num):
    roman = ''
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    for value, numeral in roman_numerals:
        while num >= value:
            roman += numeral
            num -= value
    return roman

decimaln = int(input("Enter a number: "))
print (decimal(decimaln))