# Exercice1
"""keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionnaire = {key:value for key,value in zip(keys,values) }
print(dictionnaire)"""

#Exercice2
"""
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8,}
for key, value in family.items():
    if value >=12:
        print(f"{key} doit payer 15$")
    elif value <= 3:  
        print(f"{key} doit payer 0$")
    else:
        print(f"{key} doit payer 10$")
s = 0
for value in family.values():
    if value >= 12:
        s = s + 15
    elif value <= 3:
        s = s + 0
    else:
        s = s + 10
print(f"Le cout total por la fille est:{s}$")"""


"""
#Bonus
nombre = int (input("Entrer le nombre de personne de la famille:"))
name = input("Entrer le nom:")
age = int(input("Entrer l'âge:"))
name1 =[]
age1 = []
num = 0
new_dict = {}

while  num != nombre :
    name1.append(name)
    age1.append(age)
    num= len(age1)
    print( "le nombre de personnes entrer est:",num)
    for x in name1:
        x = x
        for y in age1:
            if y>=12:
                y =15
            elif y<=3:
                y =0
            else:
                y =10
    new_dict.update({x:y})
    if num == nombre:
        break    
    name = input("Entrer le nom:")
    age = int(input("Entrer l'âge:"))
print("familyfamily=",new_dict)"""


#Exercice3

#creation de dictionnaire
dict = {"name":"Zara", "creation_date": 1975, "creator_name":"Amancio Ortega Gaona ", "type_of_clothes":"men", "type_of_clotes":"women", "type_of_cloths":"children", "type_of_clothe":"home", "international_competitors":"Gap", "international_competitors":"H&M", "international_competitors":"Benetton","number_stores": 7000, "major_color_France":"blue", "major_color_Spain":"red", "majo_color_US":"pink", "majr_color_US":"green" }
# Changez le nombre de magasins à 2.
dict["number_stores"] = 2
print(dict)
#les clients de Zaras
print("Les clients sont",dict["type_of_clothes"], dict["type_of_clotes"], dict["type_of_cloths"], dict["type_of_clothe"])
#insert = {"magasin2":1990}
dict.update({"magasin2":1990})
# la couleur insert
dict.update({"major_color_US":"jaune"})
print(dict)
# les dates de creations
print("les dates de creations sont:", dict["creation_date"],"et", dict["magasin2"])
print("Le dernier concurant international est:",dict["international_competitors"])
print("Les couleurs aux usa:", dict["majo_color_US"], dict["majr_color_US"], dict["major_color_US"] )
print("Les élments du dictionnaires sont:",len(dict))
for value in dict.values():
    print(value)
new_dict = {"creation_date": 1975,"number_stores": 10000}
dict.update(new_dict)
#print(dict)
for key in dict.keys():
    print(key)

#commentaires: on constate qu'il est impossible d'utiliser une clé pour insérer des valeurs. Une clé si elle existe, elle donc unique. 





    


        