a = int(input())


b = (a%10)*1000
c = (a//10)%10*100
d = (a//100)%10*10
e = (a//1000)%10

f = b+c+d+e


if (f == a):
    print("YES")
else:
    print("NO")