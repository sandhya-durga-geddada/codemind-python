s=input()
ls=[]
for i in s:
    if i.isdigit():
        ls.append(int(i))
print(sum(ls))