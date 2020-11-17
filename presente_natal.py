n = int(input())
a, b = map(int, input().split())
if(n>=2 and n<=100)and(a&b>=1 and a&b<=100):
    if(n>=a+b):
        print("Farei hoje!")
    else:
        print("Deixa para amanha!")