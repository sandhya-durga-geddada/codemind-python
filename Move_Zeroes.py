n=int(input())
ls=list(map(int,input().split()))
a=[]
b=[]
for i in ls:
    if i ==0:
        b.append(i)
    else:
        a.append(i)
c=a+b
print(*c)