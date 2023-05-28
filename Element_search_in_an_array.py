n=int(input())
ls=list(map(int,input().split()))
se=int(input())
for i in ls:
    if i==se:
        print('True')
        break
else:
    print('False')