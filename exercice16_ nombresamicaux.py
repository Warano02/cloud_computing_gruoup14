def somme_div(n): #fonction qui calculé le nombre de diviseur d'un nombre donné 
    c=0
    for i in range (1,n): #compte le nombre de diviseurs
        if n % i == 0 :
            c = c+i 
    return c       
           
a=int(input("entrer le premier nombre : ""\n"))    
b=int(input("entrer le deuxième nombre  : ""\n")) 

u=somme_div(a)   #appel de la fonction somme_div 
v=somme_div(b)  

if u==b and v==a : #comparaison 
    print ("\033[32m les nombres que vous avez entré forment bel et bien une paire amicale ✅ \033[0m") 
else :
    print("\033[33m les nombres que vous avez entré ne forment pas une paire amicale,  désolé ❌ \033[0m")    
            