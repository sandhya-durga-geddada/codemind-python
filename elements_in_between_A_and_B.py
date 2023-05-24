n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
ns=[]
for i in l:
    if i>=a and i<=b:
        ns.append(i)
if(ns!=[]):
    print(*ns)
else:
    print(-1)
