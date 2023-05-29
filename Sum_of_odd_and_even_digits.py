n=int(input())
ls=list(map(int,input().split()))
es=0
os=0
for i in range(len(ls)):
    if i%2==0:
        es+=ls[i]
    else:
        os+=ls[i]
if os-es==0:
    print('YES')
else:
    print('NO')