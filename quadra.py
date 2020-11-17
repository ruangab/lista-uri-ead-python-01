x, y = map(int, input().split())
if(x>=-500 and x<=500) and (y>=-500 and y<=500):
    if(x>=0 and y>=0) and (x<=432 and y<=468):
        print("dentro")
    else:
        print("fora")