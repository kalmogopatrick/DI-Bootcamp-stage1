"""
#Defi 1
word = input("Entrer votre mots:")
words = {}
for i in range(len(word)):
    mots = word[i]
    if mots in words:
        words[mots].append(i)
    else:
        words[mots]=[i]
print(words)"""
#defi2
Articles = {"TV":"$100", "Phone":"$10", "table":"$5", "Water":"$200", "sac":"$1.1", "livre":"$5.2", "vélo":"$800"}
liste =[]
money = float(input("Donnez votre argent:"))
for key in Articles.keys():
    if money >= float(Articles[key][1:]):
        liste.append(key)
if liste:
    liste.sort()
    print("Voici la liste des articles dont vous pouvez payer\n:",liste)
else:
    print("nothing!")




    
