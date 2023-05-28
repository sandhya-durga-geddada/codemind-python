n=int(input())
ls=list(map(int,input().split()))
a=[]
b=[]
for i in ls:
    if i%2!=0:
        a.append(i)
    else:
        b.append(i)
c=b+a
print(*c)