n=int(input())
ls=list(map(int,input().split()))
c=0
for i in ls:
    if ls.count(i)>c and ls.count(i)>n//2:
        c=i
print(c)