a = 1
b = 2
c = a + b
fib = [a, b]
evenFib = []
sum = 0
while a + b < 4000000:
    c = a + b
    fib.append(c)
    a = b
    b = c
for f in fib:
        if f %2 == 0:
            evenFib.append(f)
for e in evenFib:
    sum = sum + e

print(fib)
print(evenFib)
print(sum)
    
