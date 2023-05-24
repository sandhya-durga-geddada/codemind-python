n=int(input())
ls=list(map(int,input().split()))
ns=[]
for i in ls:
    if ls.count(i)==i:
        if i not in ns:
            ns.append(i)
if ns!=[]:
    l=len(ns)
    s=sum(ns)
    avg=s/l
    print("%0.2f"%avg)
else:
    print(-1)