# Opérateurs de comparaison
# a == b  => a est égal à b
# a != b  => a n'est pas égal à b
# a > b  => a est supérieur à b
# a < b  => a est inférieur à b
# a >= b  => a est supérieur ou égal à b
# a <= b  => a est inférieur ou égal à b
# a is b  => a est identique à b
# a is not b  => a n'est pas identique à b

# Expression Boolean
# True, False
print(2 == 2)
print(2 != 2)
print(7 is '7')

# Opérateurs logiques
# and, or, not
x = 4
print(x > 3 and x < 8)
print(x > 4 or x < 8)
print(not x > 7)

# type boolean
print(type(True))
print(type(False))
print(type(3 == 4))

# Exécutions conditionnelles
# #if
x = 9
if x == 9:
    print("c'est vrai")
    print('ok ok')

if x > 12:
    print("c'est vrai")

# multiple if
z = 6
if z == 4:
    print('egal')
if z > 4:
    print('sup')
if z < 4:
    print('inf')

# elif

z = 3
if z == 4:
    print('egal')
elif z > 4:
    print('sup')
elif z != '5':
    print('ok')
elif z < 4:
    print('inf')
else:
    print("c'est la fin")

# conditions imbriquées
d = 1
if d == 3:
    print('nombre identique')
else:
    if d > 3:
        print('nombre sup')
    else:
        print('nombre inf')

# try, except

temp = input('Entrez la temperature en Celsus : ')
try:
    temp_num = float(temp)
    temp_fah = temp_num * (9/5) + 32
    print('La temperature en Fahrenheit est de :', temp_fah)
except:
    print('Entrez seulement les nombres!')
