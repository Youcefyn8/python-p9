#la liste qui contiendra nos réponse
resultat = []
# carres de chiffre : 4 a 9
carres_2_chiffres = []

for i in range (4, 10):
    carres_2_chiffres.append(i ** 2)

# carres de chiffre : 32 a 100
carres_4_chiffres = []

for i in range (32, 100):
    carres_4_chiffres.append(i ** 2)

print(carres_4_chiffres)

# construsons des nombres à 4 chiffres
for i in carres_4_chiffres:
    for j in carres_4_chiffres:
        nombre = i * 100 + j

        if nombre in carres_4_chiffres:
            resultat.append(nombre)
