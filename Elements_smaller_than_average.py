n=int(input())
ls=list(map(int,input().split()))
avg=sum(ls)//n
c=0
for i in ls:
    if i<=avg:
        c+=1
print(c)