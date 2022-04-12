a,b,c=map(int,input().split())
n=0
s=0
if a==b==c:
    n=10000+a*1000
elif (a==b) or (a==c) or (b==c):
    if a==b:
        n=1000+a*100
    elif a==c:
        n=1000+a*100
    elif b==c:
        n=1000+b*100
else:
    if (a>b) & (a>c):
        s=a
    elif (b>a) & (b>c):
        s=b
    else:
        s=c
    n=s*100
print(n)