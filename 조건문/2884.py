h,m=map(int,input().split())

if m>=45:
    m=m-45
    print(h,m)
elif m<45:
    if h==0:
        h=24
    m=m-45+60
    h=h-1
    print(h,m)
    
