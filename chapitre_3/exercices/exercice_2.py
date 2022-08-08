# Cet exercice est adopté du livre "Python for Everybody" écris par Dr. Charles R. Severance et traduit en Français et modifié par Zarifou Djibril (https://medium.com/@zarifoud). Lien: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf


# Exercice 2 : écrivez un programme pour demander à l'utilisateur le nombre d'heures qu'il travail par semaine et le payement par heure pour calculer son salaire mensuel.

# Entrez le nombre d'heures : 35
# Entrez le payement par heure : 2.75
# Payement mensuel : 96.25

# Réponse :

heures = input("Entrez le nombre d'heures : ")
payement = input('Entrez le payement par heure : ')
heures_num = float(heures)
payement_num = float(payement)
salaire = 4 * heures_num * payement_num
print(salaire)
