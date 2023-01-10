#Exercice2

"""def favorite_book(users):
    print(" Un de mes livres préférés est " + users.title())
titres =input("titre du livre:")
favorite_book(titres)"""

#Exercice3
"""
def country(ville,pays):
    print(ville.title(),"est la ville du", pays.title())
vil= input("nom de la ville:")
pay = input("nom du pays:")
country(vil,pay)"""


#Exercice5
"""
def make_shirt(taille,texte):
    print(taille,texte)
tail =("la taille de ma chemise est: 5m")
ecrit =("et l'écriture sur la chemise est: joli")
grand = ("100m de taille , ah! Assez grand,")
message = ("J'aime pyhon")
chemise_grand = ("La taille de ma chemise est 50m,")
defaut = ("taille un peu formidable!")
chemise_moyen = ("La taille de ma chemise est 25m,")
defaut2 =("C'est une taille par defaut")
make_shirt(tail,ecrit)
make_shirt(grand,message)
make_shirt(chemise_grand,defaut)
make_shirt(chemise_moyen,defaut2)"""


#Exercice6
"""
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    for name in magician_names:
        print(name)
show_magicians()

def make_great():
    for i in magician_names:
        print("the Great",i)
make_great()
show_magicians()"""

#Exercice7

import random
"""
# fonction renvoyant un entuer en -10 et 40
def get_random_temp():
    number = random.randrange(-10,41)
    return number
get_random_temp()"""
#fonction main
"""
def main():
    n=get_random_temp()
    print("La tempéture actuelle est",n,"degrés Celsius")
    if n < 0:
        print("Brrr, c’est glacial!\nPortez des couches supplémentaires aujourd’hui ")
    elif n>=0 and n<16:
        print("Assez froid!\n N’oublie pas ton manteau")
    elif n >= 16 and n < 23:
        print("trop de fraîcheur!\n faites beaucoup attention")
    elif n >= 23 and n < 32:
        print("Il ya un de chaleur aujord'hui\n allummer le climb")
    else:
        print("trop de chaleur aujord'hui\n allummer tous les climb.") 
main()"""

#ajout de paramètre saison
"""def get_random_temp():
    liste = ["hiver", "printemps", "été", "automne"]
    random.shuffle(liste)
    saisons = liste
    print(saisons)
    saison = random.choice(saisons)
    print(saison)
    if saison == "hiver":
        print("La température est entre -10 et 16")
    elif saison == "printemps":
        print("La température est entre 16 et 32")
    elif saison == "été":
        print("La température est entre 32 et 36")
    else:
        print("La température est entre 36 et 40")  
get_random_temp()"""

#appelle de fonction par l'utilisateur
def get_random_temp():
    saison = input("Entrer la saison:")
    print(saison)
    if saison == "hiver":
        print("La température est entre -10 et 16")
    elif saison == "printemps":
        print("La température est entre 16 et 32")
    elif saison == "été":
        print("La température est entre 32 et 36")
    elif saison == "automne":
        print("La température est entre 36 et 40")
    else:
        print("Cette saison n'existe pas.")  
get_random_temp()
