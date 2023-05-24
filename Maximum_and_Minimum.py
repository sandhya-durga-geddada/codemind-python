n=int(input())
ls=list(map(int,input().split()))
ns=[]
for i in ls:
    if ls.count(i)==i:
        ns.append(i)
if ns!=[]:
    print(min(ns),end=' ')
    print(max(ns))
else:
    print(-1)