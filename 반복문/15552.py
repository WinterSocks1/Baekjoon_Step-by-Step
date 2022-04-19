n=int(input())

a=[]

for i in range(n):
    c,d=map(int,input().split())
    a.append(c+d)
    
for i in range(n):
    print(a[i])