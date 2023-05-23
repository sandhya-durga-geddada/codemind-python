n=int(input())
a=list(map(int,input().split()))
sum=0
count=0
for i in range(n):
    sum+=a[i]
avg=sum//n
for i in range(n):
    if a[i]<=avg:
        count+=1
print(count)