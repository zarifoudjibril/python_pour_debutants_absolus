# ======================================================
# Cet exercice est adopté du livre "Python for Everybody" http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
# écris par Dr. Charles R. Severance et traduit en Français et modifié par Zarifou Djibril. 
# ======================================================

# Exercice 2: 
# Réécrivez votre programme de calcul de salaire qui permet de payer à l'employé 
# 1,5 fois le payement horaire pour les heures travaillées au-delà de 40 heures.

# exemple:
# Entrez le nombre d'heures : 45
# Entrez le payement par heure : 10
# Payer : 1900

# Réponse:
heures = input("Entrez le nombre d'heures : ")
payement = input('Entrez le payement par heure : ')
heures_num = float(heures)
payement_num = float(payement)
if heures_num > 40:
    salaire_n = 40 * payement_num
    salaire_s = (heures_num - 40) * 1.5 * payement_num
    salaire = 4 * (salaire_n + salaire_s)
    print(salaire)
else:
    salaire = 4 * heures_num * payement_num
    print(salaire)

