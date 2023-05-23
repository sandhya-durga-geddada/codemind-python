t=int(input())
for i in range(t):
    n=int(input())
    ls=list(map(int,input().split()))
    s=n//2
    if n%2==0:
        ns=[]
        for i in range(s):
            ma=max(ls)
            mi=min(ls)
            ns.append(ma)
            ns.append(mi)
            ls.remove(ma)
            ls.remove(mi)
        print(*ns)
    else:
        ns=[]
        for i in range(s):
            ma=max(ls)
            mi=min(ls)
            ns.append(ma)
            ns.append(mi)
            ls.remove(ma)
            ls.remove(mi)
        ns.append(*ls)
        print(*ns)