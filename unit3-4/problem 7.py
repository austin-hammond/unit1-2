a = int(input())
b = int(input())

for i in range(a, b):
    if (i >= 2):
        for j in range(2, i):
            if not (i % j):
                print("no")
    else:
        print("no")
    print(i)