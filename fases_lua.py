a, b  = map(int, input().split())

if(b <= 2) and (b >= 0):
    print('nova')
elif(b <= 100) and (b >= 97):
    print('cheia')
elif(b > a):
    print('crescente')
else:
    print('minguante')
# if(a&b>=0) and (a&b<2):
#     print('nova')
# if(a&b>=2) and (a&b<96):
#     print('crescente')
# if(a&b>=96) and (a&b<100):
#     print('cheia')
