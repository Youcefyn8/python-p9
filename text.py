from curses import keyname
import random


firstname = "toto"
lastname = "pop"
number = "2"


email = firstname + '.' + lastname + number + '@example.com'
print(email)

new_emails = random.randint(0, 3)

if new_emails == 0:
    print("vous n'avez pas de nouveaux mails")
elif new_emails == 1:
    print("vous avez reçu un nouveau mail")
else:
    print("Vous avez reçu <strong>" + str(new_emails) + "</strong> nouveaux mails")

stock = random.randint(0, 15)

if stock == 0:
    print("Stock épuisé")
elif stock == 1:
    print("Il reste une piéce")
elif 1 < stock < 5:
    print("Stock en tension : {stock}pieces")
elif 5 < stock < 10:
    print("Stock en tension : {stock}pieces")
elif 1 < stock:
    print("Stock en tension : {stock}pieces")

temperature = 10.1 + 0.1 +0.1
print(temperature)
print(f"la temperature actuelle est de {temperature:.2f})°C")

eletriciter = True

#ne pas faire d'interpolation de variable booleene si votre appli n'est pas en anglais 
if eletriciter:
    print ('electriciter : vrai')
else:
    print('electriciter: faux')

    # @todo affiche age a partir de l'année de naissance

    print (f"le nombre tiré au hasard est : {random.randint(0, 10)}")

    texte = "foo bar baz"
    # len == length == longueur 
    print(len(texte))

    print(texte.find("baz"))
    print(texte.find("banana"))

texte = "bonjour toto"

#rédiger un bloc if qui indique si le keyword est present ou nom dans la chaine de caracteres
#afficher "trouvé" si le keyword est présent 
#sinon affichez "non trouvé"
keyword = "toto"

#rédiger un bloc if qui indique si le keyword est present ou nom dans la chaine de caracteres
#afficher "trouvé" si le keyword est présent 
#sinon affichez "non trouvé"
keyword = "titi"

texte = "bnjour toto"
texte.replace('bnjour', 'bonjour')
texte = texte.replace('','')
texte = texte.replace('toto', 'titi')
print(texte)

texte = "Bonjour Toto"

keyword = "Toto"
if texte.find(keyword) >= 0:
    print(f"On as trouvé {keyword}")
else :
    print(f"On as pas retrouvé {keyword}")


keyword = "Titi"


if texte.find(keyword) >= 0:
    print(f"On as trouvé {keyword}")
else : 
    print(f"On as pas retrouvé {keyword}")
