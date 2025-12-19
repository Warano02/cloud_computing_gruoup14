n = input("entrer votre mot" "\n")

mot=n.lower().replace(" ", "")# éliminer les espaces et les majuscules dans le mot

tab = list(mot)
est_palin = True 

for i in range(len(tab) // 2): #diviser le mot en deux pour ne pas comparer la même chose
    if tab[i] != tab[-(i+1)]:# comparer les éléments du tableau 
        est_palin = False 
        break
       
if est_palin :
    print("le mot que vous avez entré est bel et bien un palindrome") 
 
else:
    print("\033[31m le mot n'est pas un palindrome\033[0m désolé pour vous !! ") 
    
    
        