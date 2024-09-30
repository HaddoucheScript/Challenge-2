import random
cpt1=0
cpt2=0
y=10
st=str(y)
x=random.randint(0,9)
while(x!=y)and(st!='exit'):
    y=input('please guess a number from 0 to 9   ')
    r=y-x
    st=str(y)
    print(st)
    if r==0:
        print(' Congratulations! You win ')
    elif r<0:
        print(' You guessed too low, try again ')
        cpt1+=1
    else:
        print(' You guessed too high, try again ')
        cpt2+=1
if cpt1+cpt2==0:
    print(f"you tried {cpt1+cpt2+1} time")
else:
    print(f"you tried {cpt1+cpt2+1} times")

