n=int(input())
ls=list(map(int,input().split()))
a,b=map(int,input().split())
ns=[]
for i in ls:
    if i<a or i>b:
        ns.append(i)
if ns !=[]:
    print(max(ns))
else:
    print(-1)