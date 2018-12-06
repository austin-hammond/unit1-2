numbers = (1,2,3,4,5,6,7,8,9)
even = 0
odd = 0
for x in numbers:
    if not x % 2:
        even += 1
    else:
        odd += 1
print("even: ",even)
print("odd: ",odd)