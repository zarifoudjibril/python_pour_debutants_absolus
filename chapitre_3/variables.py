# Ceci est un commentaire

# valeur
# 3
# 98 98 98 98
# Traversy
# 450 $

# variable

note = 3
client = 'Traversy'
pi = 3.14

# print()
print('Bonjour le monde')
print(note)
print(client)
print(pi)

# types de variables

# integer
note = 3

# float 
pi = 3.14

# string
client = 'Traversy'
nom = "Zaricademy"

# type()

print(type(note))
print(type(client))
print(type(nom))
print(type(pi))

# Nommage des variables et les mots réservés en Python

# 1. Pas d'espace
nom_de_famille = 'Traversy'


# 2. Le nom d'une variable ne peut pas débuter avec un chiffre ni le caractère _.
12eleves = 12
_eleve = 'Ami'

# 3. le nom d'une variable ne doit pas contenir un caractère illégaux (/, @, ?, ....)
nom? = 'Zaricademy'

# 4. Le nom d'une variable ne peut pas être un mot reservé de Python.
await = 1.2

# Les mots réservés en python

# 
# and       del       from
# as        elif      global
# assert    else      if
# break     except    import
# class     False     in
# continue  finally   is
# def       for       lambda
# None      True
# nonlocal  try
# not       while
# or        with
# pass      yield
# raise     async
# return    await 

nom de famille = 'Traversy'
print(nom de famille)

12eleves = 12
print(12eleves)

assert  = 'Rue'
print(assert)


# # Note: Sensibilité de case en python
# nom = / Nom = / NOM
nom = 'Zaricademy'
print(Nom)


# Opération numérique (integer et flaot)

# opérateurs : +, -, *, /, **(puissance), //(le quotien), % (modulo)___ reste

# '''Puissance 2 asterix'''
12**2
# '''quotien, 2 //'''
9//2
# '''reste, le modulo % '''
9 % 2

# Incrémention

m = 2
n = 4
# print(m+n)
# print(m-n)

m += 1
print(m)

#  -=, /=, *=

n *= 2
print(n)


# Opération sur les string

# Nous avons droit à seulement deux types d'opérations: ADDITION ET LA MULTIPLICATION

nom = 'Zaricademy'
print(nom)

print(nom + ' sur Facebook')

print('Bonjour'+' le monde'+ ' sur Zaricademy')

print(3*nom)

print('Bonjour' + '5')
print(3.5*nom)


# Conversion de type() et les fonctions int(), str() et float()

# int / str
# str / int
# float / int

# int(), str() et float()

numero = 7
print(type(numero))
numero_str = str(numero)
print(numero_str)
print(type(numero_str))

# input()

# ecris = input()
nom = input('Entrez votre nom: ')
print(nom)

note = input('Entrez votre note: ')
note_num = int(note)
note_final = note_num + 5
print(note_final)

# Erreurs Possibles

#1- SYNTAX ERROR
prix final = 230

#2- NAME ERROR
'''Si vous essayez d'utiliser une variable avant sa déclaration '''
note = 12
devoir = 14
composition = 7.5
print(note + devoir + composition)
