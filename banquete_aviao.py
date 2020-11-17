f, bf, m = map(int, input().split())
a, b, c = map(int, input().split())


total = 0

if(a>f):
    total = total + (a-f)
if(b>bf):
    total = total + (b-bf)
if(c>m):
    total = total + (c-m)
print(total)