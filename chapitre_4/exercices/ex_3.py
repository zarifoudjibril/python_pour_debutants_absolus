# ======================================================
# Cet exercice est adopté du livre "Python for Everybody" http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
# écris par Dr. Charles R. Severance et traduit en Français et modifié par Zarifou Djibril. 
# ======================================================

# Exercice 3: 
# Réécrivez votre programme de calcul de salaire en utilisant try et except afin que votre 
# programme puisse gèrer correctement les entrées non numériques en affichant un message et en
# quittant le programme. 

# exemple:
# Entrez les heures : 20
# Entrez le payement : neuf
# Erreur, veuillez entrer une valeur numérique

# Réponse:

heures = input("Entrez le nombre d'heures : ")
payement = input('Entrez le payement par heure : ')
try:
    heures_num = float(heures)
    payement_num = float(payement)
except:
    print('Erreur, veuillez entrer une valeur numérique')
    quit()
if heures_num > 40:
    salaire_n = 40 * payement_num
    salaire_s = (heures_num - 40) * 1.5 * payement_num
    salaire = 4 * (salaire_n + salaire_s)
    print(salaire)
else:
    salaire = 4 * heures_num * payement_num
    print(salaire)


