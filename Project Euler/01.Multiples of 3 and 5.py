list = [i for i in range (1000) if (i % 3 == 0 or i % 5 == 0)]
sum = 0
for l in list:
    sum = sum + l
print(list)
print(sum)
