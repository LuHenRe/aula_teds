n = int(input())
codigo = {
    "A" : 0 or -26,
    "B" : 1 or -25,
    "C" : 2 or -24,
    "D" : 3 or -23,
    "E" : 4 or -22,
    "F" : 5 or -21,
    "G" : 6 or -20,
    "H" : 7 or -19,
    "I" : 8 or -18,
    "J" : 9 or -17,
    "K" : 10 or -16,
    "L" : 11 or -15,
    "M" : 12 or -14,
    "N" : 13 or -13,
    "O" : 14 or -12,
    "P" : 15 or -11,
    "Q" : 16 or -10,
    "R" : 17 or -9,
    "S" : 18 or -8,
    "T" : 19 or -7,
    "U" : 20 or -6,
    "V" : 21 or -5,
    "W" : 22 or -4,
    "X" : 23 or -3,
    "Y" : 24 or -2,
    "Z" : 25 or -1
}

for _ in range(n):
    palavra = input().upper()
    x = int(input())
    for letra in palavra:
        codigo[letra] -= x
        print(codigo[letra])
