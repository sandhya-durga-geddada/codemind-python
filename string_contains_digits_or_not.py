t=int(input())
for i in range(t):
    s=input()
    c=0
    for i in s:
        if i.isdigit():
            c+=1
    if c==0:
        print('No')
    else:
        print('Yes')