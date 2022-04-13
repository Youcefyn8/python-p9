import random
# if True:
#     print ("ce message sera toujours affiché")

# if False:
#     print ("ce message sera toujours affiché")

# if True:
#     print ("ce message sera toujours affiché(if true)")
# else:
#     print("ce message ne sera jamais afficher")

# if False:
#     print ("ce message sera toujours affiché(if False)")
# else:
#     print("ce message sera toujours affiché")

# fruits =['banane', 'pommes', 'cherries']

# if 'pommes' in fruits:
#     print("il y a des pommes")
# else:
#     print("il n'y a pas des pommes")

# if 'oranges' in fruits:
#     print("il y a des oranges")
# else:
#     print("il n'y a pas des oranges")

# is_authenticated = True

# if is_authenticated:
#     print("l'utilistateur peut accéder aux backoffice")

# user_password = "123"
# user_password_in_db = "abc"

# if user_password == user_password_in_db:
#     print("l'utilisateur peut accéder aux backoffice")
# else:
#     print("Le login ou le mot de passe est incorrect")

# user_in_db = ['toto', 'titi', "tata", 'tutu']
# tutu_password_in_db = "abc"

# user_name_in_form = 'tutu'
# user_password_in_form = "123"

# if user_name_in_form in user_in_db and user_password_in_form == tutu_password_in_db:
#   print("l'utilisateur peut accéder")
# else:
#     print("l'utilisateur ne peut pas acceder") 

# is_authenticated = True
# user_in_db = ['toto', 'titi', "tata", 'tutu']
# tutu_password_in_db = "abc"

# user_name_in_form = 'tutu'
# user_password_in_form = "abc"

# if True:
#     print("l'utilisateur peut accéder aux backoffice")
# else:
#     print("Le login ou le mot de passe est incorrect")
# rint ('electricity_is_off:', eletricity_is_off)
# print ('water_is_off:', water_is_off)
# print ('gas_is_off:', gas_is_off)

# #vérifier que toutes les sources sont coupées
# #si c'est le cas, affichez le message "Vous pouvez partir en week end"
# #sinon, affichez le message "il reste des sources a couper"

# eletricity_is_on = bool(random.randint(0, 1))
# water_is_on = bool(random.randint(0, 1))
# gas_is_on = bool(random.randint(0, 1))

# print ('electricity_is_on:', eletricity_is_on)
# print ('water_is_on:', water_is_on)
# print ('gas_is_on:', gas_is_on)

# # vérifier que toutes les sources sont coupées
# # si c'est le cas, affichez le message "Vous pouvez partir en week end"
# # sinon, affichez le message "il reste des sources a couper"

# if eletricity_is_on and water_is_on and gas_is_on:
#     print ("vous pouvez partir en we")
# else:
#     print("il reste des sources à couper")

#  vérifier que toutes les sources sont coupées
#  si c'est le cas, affichez le message "Vous pouvez partir en week end"
# sinon, affichez le message "il reste des sources a couper"

# if not eletricity_is_on and not water_is_on and gas_is_on:
#     print ("vous pouvez partir en we")
# else:
#     print("il reste des sources à couper")

#     if eletricity_is_on
#     print("coupez l'electricité")

#     if gas_is_on
#     print("coupez le gaz")

# eletricity_is_off = bool(random.randint(0, 1))
# water_is_off = bool(random.randint(0, 1))
# gas_is_off = bool(random.randint(0, 1))



has_cash = bool(random.randint(0, 1))
has_card = bool(random.randint(0, 1))
has_check = bool(random.randint(0, 1))

print('has_cash:', has_cash)
print('has_card:', has_card)
print('has_check:', has_check)

#vérifier qu'au moins un moyen de paiement est disponible
# si c'est le cas, affichez le message "Vous pouvez partir faire les courses"
# sinon affichez le message "vous n'avez aucun moyen de paiement"

print("has_cash",has_cash) 
print("has_card",has_card) 
print("has_check",has_check) 

if has_check or has_card or has_cash:
    print("vous pouvez payer")
    if has_card:
        print("vous avez une carte")
    if has_cash:
        print("vous avez du cash")
    if has_check:
        print("vous avez un cheque")
else:
    print("vous avez pas de quoi payer")

    age = random.randint(0, 100)

    # 0-5 bébé
    # 6-12 enfant
    # 12-25 jeune adulte
    # 26-59 adulte
    # 60+ senior

    if age <= 5:
        print('bébé')
    elif 6 <= age <= 11:
        print('enfant')
    elif 12 <= age <= 25:
        print('ado, jeune adulte') 
    elif 26 <= age <= 59:
        print('adulte') 

#on peut faire un "else" pour intercepter les cas ou l'age >= 60

    elif age >= 60:
        print('senior') 

    if (123):
        # le message s'affichera car bool(123) == True
        print('Il y a une valeur numérique')

    if (0):
        # le message s'affichera car bool(123) == False
        print ('Il y a une valeur nulle')

