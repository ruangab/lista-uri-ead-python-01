l = int(input())
c = int(input())

if(l&c>=1 and l&c<=1000):
    if((l+c)%2==0):
        print(1)
    else:
        print(0)