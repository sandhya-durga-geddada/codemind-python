n=int(input())
ls=list(map(int,input().split()))
k=int(input())
ns=[]
for i in ls:
    if ls.count(i)==k:
        if i not in ns:
            ns.append(i)
if ns!=[]:
    print(*ns)
else:
    print(-1)