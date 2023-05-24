n=int(input())
ls=list(map(int,input().split()))
c=0
ns=[]
for i in ls:
    if ls.count(i)==i:
        if i not in ns:
            ns.append(i)
            c+=1
print(c)