n=int(input())
ls=list(map(int,input().split()))
s=0
for i in ls:
    if i==0 or i==1:
        pass
    else:
        s=1
if s==1:
    print('False')
else:
    print('True')