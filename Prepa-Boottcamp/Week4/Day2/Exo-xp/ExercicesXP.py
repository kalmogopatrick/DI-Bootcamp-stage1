#Exercice1#
"""my_fav_numbers = {"78515809", "55256957","53293929","45256958","08562359"}

my_fav_numbers.add("40000003")
my_fav_numbers.add("23408798")

my_fav_numbers.remove("23408798")

friend_fav_numbers = {"99999999","44444444","33333333"}

my_fav_numbersfriend_fav_numbers = my_fav_numbers | friend_fav_numbers
print(my_fav_numbersfriend_fav_numbers)"""


#Exercice2#
"""Les tuples sont des listes immuables, 
ce qui signifie que les éléments 
ne peuvent pas être modifiés.
par consequent, il est impossible 
d'ajouter plus d'entiers au tuple."""

#Exercice3#

"""basket = ["Banana", "Apples", "oranes", "Blueberries"]

basket.remove("Banana")

basket.remove("Blueberries")

basket.append("Kiwi")

basket.insert(0, "Apples")

rep = basket.count("Apples")
print("Le nombre de pommes est:",rep)

basket.clear()
print("Voici le panier vidé:",basket)"""


#Exercice4
"""1) int() : permet de modifier une variable en entier. 
float() : permet la transformation en flottant(nombre à virgule)

2)Oui, cela consiste à convertir la valeur en chaîne avec une précision absolue, 
puis à tout supprimer du nombre de caractères souhaité.

3)ma_liste = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]"""


#Exercice5
"""for i in range(1, 21):
    print(i)

for n in range(1,21):
    if n%2 != 0 and n != 1:
        indice = n
        print(indice)"""

#Exercice6
"""name = input("please!,your name:")
while name != "patrick":
    name = input("please!,your name:")
print("merci!")"""

#Exercice7
"""print("Separer les fruis avec un seul espace.\n Ex: mango apple cherry...")
fruits = input("Entrer vos fruits préferés:")
liste =fruits.split()
print(liste)
mes_fruits = input("entrer un fruit:")
for fruit in liste: 
    if fruit==mes_fruits:
        print("Vous avez choisi l'un de vos fruits préféré.")
        break
    elif fruit !=mes_fruits:
        fruit += fruit
    if fruit==mes_fruits:
        print("Vous avez choisi l'un de vos fruits préféré.")
    else:
        print("Vous avez choisi un nouveau fruit. j'espère que vous apprécierez")"""
        
        
    

#Exercice8

"""ganiture = input("Entrer une ganiture de pizza:")
liste = []
prix = 0
while ganiture != "quitter":
    liste.append(ganiture)
    prix = prix + 10+2.5
    print("Vous avez ajouter cette graniture à votre pizza")
    ganiture = input("Entrer une ganiture de pizza:")
print(f"Les garnitures ajoutées sont:{liste}.\nLe prix total est:{prix}")"""


#Exercice9
"""age = int(input("svp! Tapez '-1' si vous finissez.\nage:"))
liste = []
p1 = 0
p2 = 0
p3 = 0
while age != -1:
    liste.append(age)
    if age < 3:
        p1 = p1 + 0 
    elif age >= 3 and age <= 12:
        p2 = p2 + 10
    else:
        p3 = p3 + 15
    age = int(input("age:"))
    prixTotal = p1 + p2 + p3 
print(f"Les âges de votre famille sont:{liste}\nLe prix total = {prixTotal}$")"""

#question4
"""print ("tapez non='fin' et age='-1' pour arreter.")
nom = input("nom:")
age = int (input("age:"))
liste = []
while nom != "fin" and age != -1:
    liste.append(nom)
    if age < 16:
        liste.remove(nom)
    elif age > 22:
        liste.remove(nom)
    nom = input("nom:")
    age = int (input("age:"))
print(liste)"""


#Exercice10
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwich = []
finish = input("sandwich préparé.")
for sandwich in sandwich_orders:
    if sandwich == finish:
        finished_sandwich.append(sandwich)
    finish = input("sandwich préparé.")
sandwich += sandwich
print(finished_sandwich)

#Exercice11
"""sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwich = []
finish = input("sandwich préparé.")
while finish != "Pastrami sandwich":
 
    for sandwich in sandwich_orders:
        if sandwich == finish:
            finished_sandwich.append(sandwich)
    finish = input("sandwich préparé.")
    sandwich += sandwich
print(finished_sandwich)
print("Pastrami sandwich est en court de préparation")"""








    
     







    







