def numCapitals(s):
    c = 0
    for letter in s:
        if letter == letter.upper() and letter.isalpha():
            c += 1
    return c

numCapitals("Julia is THE most beautiful woman in existence!")