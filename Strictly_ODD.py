n=int(input())
ls=list(map(int,input().split()))
s=0
for i in range(len(ls)):
    if i%2!=0:
        if ls[i]%2!=0:
            pass
        else:
            s=1
            break
if s==0:
    print('True')
else:
    print('False')