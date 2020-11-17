a,b,c = map(int, input().split())
h,l = map(int, input().split())

if(h>a) and (h>c):
    if(l>b):
        print('S')   
    else:
        print('N')  