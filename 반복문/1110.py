n=int(input())

if n<10:
    n=n*10

first = n
len=0
a=0

while 1:
    a = n//10 + n%10
    n = n%10*10 + a%10
    len = len+1
    if n==first:
        break
    
print(len)