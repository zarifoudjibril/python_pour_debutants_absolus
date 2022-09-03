# Exercice 1: Ecrivez un programme qui calcule les racines
# d'une équation du second degré.
# exemple d'equations: # 2x2 + 9x + 5 = 0, x2 + 2x + 1 = 0 et  x2 - 2x + 7 = 0

# Réponse:
# ax2 + bx + c = 0

from cmath import sqrt

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

d = b**2 -4*a*c
print(d)

if d > 0:
    x1 = (-b-sqrt(d))/(2*a)
    x2 = (-b+sqrt(d))/(2*a)
    print(f'x1 = {x1.real} et x2 = {x2.real}')
elif d == 0:
    x = -b/(2*a)
    print(f'x = {x.real}')
else:
    print('Pas de racine')        












