n=int(input())
ls=list(map(int,input().split()))
ns=[]
for i in ls:
    if i%2==0:
        ns.append(i)
for i in ls:
    if i%2!=0:
        ns.append(i)
print(*ns)