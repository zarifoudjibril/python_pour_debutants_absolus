nom = input('Entrer le nom du fichier: ')
gestionaire = open(nom, 'r')
compteur = dict()

for ligne in gestionaire:
    mots = ligne.split()
    for mot in mots:
        compteur[mot] = compteur.get(mot, 0) + 1

nombrefois = None
motplusrep = None
for mot, nombre in list(compteur.items()):
    if nombrefois is None or nombre > nombrefois:
        motplusrep = mot
        nombrefois = nombre

print(motplusrep, nombrefois)
