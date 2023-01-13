#Exercice1
"""
class cat():
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1 = cat(cat_name ="dodo", cat_age= 5)
cat2 = cat(cat_name="mouche", cat_age=2)
cat3 = cat(cat_name="julon", cat_age=6)
cats = [cat1, cat2, cat3]
def animal():
    cat = cats[0]
    for cate in range(len(cats)):
        if cats[cate].age > cat.age:
            cat = cats[cate]
    print(f"Le chat le plus âgé est {cat.name},\net son âge est {cat.age}")
animal()"""


"""
#Exercice2

class dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print("goes woof! ",self.name)

    def jump(self):
        print(f"a une hauteur de {self.height}cm\n")

davids_dog = dog("Rex", 50)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = dog("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump()
if davids_dog.height > sarahs_dog.height:
    print(f"le plus gros chien est {davids_dog.name}")
else:
    print(f"{sarahs_dog.name} est le plus grand")"""

#Exercice3

class song():
    def __init__(self, sing, lyrics):
        self.sing = sing
        self.lyrics =  lyrics
    
    def sing_me_a_songlyrics(self):
        print(self.sing,)
        print("all that glitters is gold\n", self.lyrics)
stairway = song("There’s a lady who's sure", "and she’s buying a stairway to heaven")
stairway.sing_me_a_songlyrics()  









    



