
a, b  = map(int, input().split())

if (a>b):
    c = a//b    
else:
    c = b//a

if (c*a==b)or(c*b==a):
    print("são multiplos")
else:
    print("Não são multiplos")