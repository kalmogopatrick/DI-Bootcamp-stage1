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

basket = ["Banana", "Apples", "oranes", "Blueberries"]

basket.remove("Banana")

basket.remove("Blueberries")

basket.append("Kiwi")

basket.insert(0, "Apples")

rep = basket.count("Apples")
print("Le nombre de pommes est:",rep)
basket.clear()
print("Voici la nouvelle liste vide:",basket)
