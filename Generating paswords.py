#Generating paswords
import random as rd
import string as st
list1=['damage','breakdown','chrono','eraserhead']
x=input('How strong do you want your password : type (weak) or (strong)')
pwd=""
listt=st.ascii_letters
if x.lower()=='weak':
   print('We suggest this password :',rd.choice(list1))
elif x.lower=='strong':
   l=rd.randint(8,15)
   for i in range(l):
        theset=(str(rd.randint(0,9)),rd.choice(listt),rd.choice(st.punctuation))
        r=rd.choice(theset)
        pwd+=r
   print (f"We suggest this password:{pwd}")   
else:
        print('Are you blind? we said (weak) or (strong)!!')
           