def pal(n):
    r=0
    t=n
    while n>0:
        rem=n%10
        r=r*10+rem
        n=n//10
    return r
a=int(input())
b=int(input())
for i in range(a,b+1):
    r=pal(i)
    if i==r:
        print(i,end=' ')