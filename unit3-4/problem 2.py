a = int(input())
b = int(input())
c = int(input())

counter = 0

if ((a <= b) and (a <= c)) and ((b >= a) and (b <= c)) and ((c >= b) and (c >= a)):
    print("YES")
    print(a)
    print(b)
    print(c)
else:
    print("NO")
    if ((a <= b) and (a <= c)):
        print(a)

    if ((b <= a) and (b <= c)):
        print(b)

    if ((c <= b) and (c <= a)):
        print(c)
        
        
        
    if ((a >= b) and (a <= c)):
        print(a)
        
    if ((b >= a) and (b <= c)):
        print(b)
        
    if ((b <= a) and (b >= c)):
        print(b)
        
    if ((c >= a) and (c <= b)):
        print(c)
        
        
        
    if ((a >= b) and (a >= a)):
        print(a)
        
    if ((b >= c) and (b >= a)):
        print(b)
        
    if ((c >= b) and (c >= a)):
        print(c)
    
