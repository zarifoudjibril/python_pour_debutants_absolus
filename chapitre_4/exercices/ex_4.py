# ======================================================
# Cet exercice est adopté du livre "Python for Everybody" http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
# écris par Dr. Charles R. Severance et traduit en Français et modifié par Zarifou Djibril. 
# ======================================================

# Exercice 4: 
# Écrivez un programme pour demander une note comprise entre 0,0 et 1,0. 
# Si la note est hors limites, imprimez un message d'erreur. Si la note
# est comprise entre 0,0 et 1,0, imprimez un message à l'aide du tableau suivant :

# Note       Grade
# >= 0,9     A
# >= 0,8     B
# >= 0,7     C
# >= 0,6     D
# < 0,6      F

#exemple:
# Enter la note: 0.95
# A

# Enter la note: parfait
# Seulement les nombres

# Enter la note: 10.0
# mauvaise valeur

# Enter la note: 0.75
# C

# Enter la note: 0.5
# F

# Réponse:

note = input('Entrez la note: ')
try:
    note_num = float(note)
except:
    print('Seulement les nombres')
    quit()
if 0 > note_num or 1 < note_num:
    print('Mauvaise valeur')
else:
    if note_num >= 0.9:
        print('A')
    elif note_num >= 0.8:
        print('B')
    elif note_num >= 0.7:
        print('c')
    elif note_num >= 0.6:
        print('D')
    elif note_num < 0.6:
        print('F')


