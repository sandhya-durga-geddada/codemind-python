n=int(input())
ls=list(map(int,input().split()))
ns=[]
for i in ls:
    if i not in ns:
        ns.append(i)
print(*ns)