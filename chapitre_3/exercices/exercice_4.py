# Cet exercice est adopté du livre "Python for Everybody" écris par Dr. Charles R. Severance et traduit en Français et modifié par Zarifou Djibril (https://medium.com/@zarifoud). Lien: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf

# Exercice 4 : Écrivez un programme qui demande à l'utilisateur une température en Celsius, convertit la température en Fahrenheit et imprime la température convertie.

# Réponse :

temp = input('Entrez la temperature en Celsus : ')
temp_num = float(temp)
temp_fah = temp_num * (9/5) + 32
print('La temperature en Fahrenheit est de :', temp_fah)
