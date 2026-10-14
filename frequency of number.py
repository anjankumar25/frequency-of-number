"""a=input("give:")
p={}
for i in a.lowe():
    if i in a:
        p[i]=1
    else:
        p[i]+=1
print(p)
a=input("give:")
b={"a","e","i","o","u","A","E","I","O","U"}
c=0
for i in a:
    if i in b:
        c=c+1
        print(i)
print(f" there is {c} vowels")
    """
a = int(input("give:"))
p=a
for v in range(1,11):
    c=0
    a=p
    while (a>0):
        i = a%10
        if i == v:
            c+=1
        a=a//10
    if c>0:
        print(f"{v} is {c}times")