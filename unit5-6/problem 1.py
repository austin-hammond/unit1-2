a = str(input())
b = a
c = a[::-1]
if len(a) < 2:
    b = "Empty String"
else:
    b = a[:(len(a) + 0) // 2] + c[:(len(c) + 0) // 2]
    
print(b)