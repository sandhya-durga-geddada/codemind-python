n=int(input())
ls=list(map(int,input().split()))
r=0
for i in ls:
    if i%2!=0:
        r=1
if r==1:
    print('False')
else:
    print("True")