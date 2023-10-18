#tab=[]
#for i in range(1,10) :
 #   tab.append(i*7)
#print(tab)


#tab1=[]
#tab2=[]
#s=0
#for i in range (0,4) :
 #   tab1.append(int(input("entrer la valeur ")))
#for i in range (0,2) :
   # tab2.append(int(input("entrer la deuxième valeur ")))

#for i in range (0,4):
    #for y in range (0,2) :
        #s=s+tab1[i]*tab2[y]

#print("schtrompf est : ",s)


#tab=[]
#n=int(input('entrer le nombre de cases de tableau : '))
#for i in range (0,n+1) :
   # x=int(input("enter the element number "))
   # tab.append(x)

#print(tab)

#tab1=[]
#n=int(input("entrer le nbr de case : "))
#for z in range(0,n):
    #  x=int(input(f"enter l'element numéro {z+1} : " ))
     # tab1.append(x)
    

#for i in range(0,n):
    #for j in range(i+1,n):
        #if tab1[j]<tab1[i] :
          # temp = tab1[i]
           #tab1[i] = tab1[j]
           #tab1[j] = temp
#print("le tableau après la permutation est : " ,tab1)

#x=0
#mot=input("entrer un mot svp : ")
#for i in (mot):
    #x=x+1
#print("le nombre de lettre est " , x)

#print(len(mot))

#x= 'one , two ,three , wonderful ,wonderful ,WOnderful how good is  he'

#print(x.count('wonderful')+x.count('WO'))






print("exercice 1 : ")
x=0
mot=input("entrer un mot svp : ")
for i in (mot):
    x=x+1
print("le nombre de lettre est " , x)

print(len(mot))
print("exercice 2 : ")
x=input("enter quelque caractère : ")
if x=="" :
    print("la chaine est vide")
else :
    print('chaine non vide')

print('exercice 3 : ')
mot1=input('entrer un mot svp : ')
nbr=len(mot1)

for i in range(nbr-1,-1,-1) : 
    print(mot1[i],end="")
print()


print("exercice 4 : ")
n=input('entrer des chaine de caractère : ')
m=input("enter une lettre : " )
print(n.index(m))
print()
print("exercice 5 : ")
st=input("entre une phrase : ")
g=""
h=" "
x2=st.replace(h,g)
print(st.replace(h,g))
print("exercice 6 : ")
txt=input("entrer un mot svp : ")
len1=len(txt)
s=str("")
for i in range(len1-1,-1,-1) :
    s=s+txt[i]
if s == txt :
    print("cette chaine est palindrome : ")
else :
    print("cette chaine n'est pas palindrome ") 
print("exercice 7 : ")
x1=input("entrer une phrase svp : ")
print(x1.upper())
print()

print("exercice 8 : ")
ph=input("entrer des chaine de caractère svp ")
cara=input("entrer la lettre voulu : ")
print(ph.count(cara))

print("exercice 9 : ")
ph1=str(input("entrer des chaine de caractère svp "))
cara=str(input("entrer la lettre voulu : "))
cara1=str(input("enter un caractère pour changer le premier : "))
b=ph1.replace(cara,cara1)
print(b)




        