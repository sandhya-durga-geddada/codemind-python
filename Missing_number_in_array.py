t=int(input())
for i in range(t):
    n=int(input())
    ls=(map(int,input().split()))
    s=0
    s1=0
    for i in ls:
        s+=i
    for j in range(n+1):
        s1+=j
    print(s1-s)