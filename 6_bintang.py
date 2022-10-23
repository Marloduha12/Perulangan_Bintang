print('##  Program Python Segitiga Bintang  ##')
print('=======================================')
print(' Code By : Marlo Duha')
 
tinggi_segitiga = int(input('Input tinggi segitiga: '))
print()
 
a = tinggi_segitiga
s = 2 * a - 2 # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ',end='')
    s -= 2
    for j in range(0, i + 1):
        print('* ', end='')
    print('')
