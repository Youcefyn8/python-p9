# nombre = 123 #nombre entier 
# print(nombre)

# nombre = 3.14 #nombre flotent 
# print(nombre)

# nombre = "foo bar baz"
# print(nombre) 

# text = "lorem ipsum"
# print(text)

# is_day = True
# print(is_day)

# has_accepted_ula= False
# print(has_accepted_ula)

# has_accepted_ula= None
# print(has_accepted_ula)

# html_code = '<h1>titre de mon blog </h1>'
# print(html_code)

# nickname = 'john \"Dead\" doe'
# nickname = 'john O\'Connor'
# print(nickname)

# multiline_text = "\\foo\nbar\nbaz"
# print (multiline_text)

# multiline_text = """'foo'
# "bar"
# baz"""
# print(multiline_text)

# nombre = -123
# print(nombre)
# print (type(nombre))

# nombre = -123.0
# print(nombre)
# print (type(nombre))

# nombre = -3.14
# print(nombre)
# print (type(nombre))
# nombre = int(nombre)
# print(nombre)
# print(type(nombre))

# nombre = 3.14 
# print(nombre)
# nombre = int(nombre)
# print(nombre)
# print (type(nombre))

# texte = str(nombre)
# print(texte)
# print(type(texte))

# my_var = 0
# my_var = bool(my_var)
# print(my_var)

# my_var = 123
# my_var = bool(my_var)
# print(my_var)

# my_var = -123
# my_var = bool(my_var)
# print(my_var)

# my_var = ""
# my_var = bool(my_var)
# print(my_var)

# my_var = "0"
# my_var = bool(my_var)
# print(my_var)

# my_var = "123"
# my_var = bool(my_var)
# print(my_var)

# my_var = "-123"
# my_var = bool(my_var)
# print(my_var)

# my_var =[123, "abc" , False]
# my_var = bool(my_var)
# print(my_var)

# interchanger les valeurs (faites un swap)
a = 42 
b = 123

#interdit
# a = 123
# b = 42

if a == 123 and b ==42:
    print("Vous avez réussi à inverser les valeur des variable")
#arrondi

# méthode classique 
c = a
a = b
b = c

#méthode arithmétique
a = a + b # a = 42 + 123
b = a - b # b = (42 +123) -123 = 42
a = a - b # a = (42+123)- 42 = 123

#detructured assignment
# avec python, js mais pas php 
a , b = b , a

#arrondi
import decimal
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

print(Decimal("0.5").quantize(Decimal(1)))
print(Decimal("1.5").quantize(Decimal(1)))