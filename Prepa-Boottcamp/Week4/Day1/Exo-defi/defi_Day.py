from random import shuffle
word = input("Veuillez entrer une chaine caractère:")
while len(word) != 10:
    if len(word) <10:
        print("chaine pas assez longue")
    if len(word) >10:
        print("chaine trop longue")
    word = input("Veuillez enter une chaine caractère:") 
print(f"la première letttre est:'{word[0]}' et la dernière lettre est:'{word[-1]}'")

mots = ""
for element in word:
    mots = mots + element
    print(mots)
print("ici c'est la partie bonus.")
n=list(word)
shuffle(n)
print(n)
new=""
new=new.join(n)
print("le mots mellangé est:",new)



