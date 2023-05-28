n=int(input())
e=0
o=0
while(n!=0):
    r=n%10
    if r%2==0:
        e+=1
    else:
        o+=1
    n=n//10
if o==0:
    print('Even')
if e==0:
    print('Odd')
if o!=0 and e!=0:
    print('Mixed')