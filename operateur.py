# + - * /
from re import T


result = 123 + 4.14
print(result)

#()
result =(1 + 2) *3
print(result)

# // % **
result = 1 // 3
print(result)

# modulo
result = 10 % 3
print(result)

#verifie
result = 7849643 % 7
print(result)

#puissance
#dans certains langage c'est : ^, pow()
result = 3 ** 2 
print(result)


#racine carrée
result = 3 ** (1 / 2)
print(result)

result = True and True # True
result = False and True # False
result = True and False # False
result = False and False # False

# s'il n'y a aps que des "and" , l'ordre n'est pas important
result = False and True and True and False # False

# operateur booléen "or"
result = True or True # True
result = False or True # True
result = True or False # True
result = False or False # False


# s'il n'y a aps que des "or" , l'ordre n'est pas important
result = False or True or True or False # True

# operation booléen "xor", le ou exclusive
result = True ^ True # false
result = False ^ True # True
result = True ^ False # True
result = False ^ False # False

# pérateurs composés
# c++ <=> c = c + 1 

number = 42 
# number = number + 1 
number += 1

