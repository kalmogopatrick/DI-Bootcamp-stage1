print("McDonald's farm\n")

class farm():
    def __init__(self, macdona, animal):
        self.macdona = macdona
        self.animal = animal
    
    def additional(self):
        print(f"{self.macdona} : {self.animal}")

    def farmget(self):
        print("La ferme deMcDonald’s a des",self.macdona)

farm1 = farm("cow",5)
farm1.additional()

farm2 = farm("sheep",2)
farm2.additional()

farm3 = farm("goat", 12)
farm3.additional()

print("\t \n E-I-E-I-0\n")
liste = []
animaux = farm1.macdona, farm2.macdona, farm3.macdona
for anim in animaux:
    liste.append(anim)
print(f"get_animal_typesFarm{liste}\n")

farm4 = farm("cow",5)
farm5 = farm("sheep",2)
farm6 = farm("goat",12)

farm4.farmget()
farm5.farmget()
farm6.farmget()
print(f"\nFarmget_short_infoget_animal_types{liste}")

    


