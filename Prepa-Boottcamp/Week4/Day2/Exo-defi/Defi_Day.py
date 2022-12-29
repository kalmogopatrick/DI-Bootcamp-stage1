#defi1
""""Number = int(input("Entrer le nombre:"))
N = int(input("nombre d'element voulu"))
liste = []
for n in range(1,N+1):
    liste.append(Number*n)

print(liste)"""
#Defi2
liste = []
chaine = input("Entrer la chaine:")
liste.append(chaine[0])
for n in chaine:
    if liste[-1]!= n:
        liste.append(n)
print("".join(liste))        


