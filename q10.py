n = int(input("Enter a number less than 4000000: "))
a, b = 1, 2
total = 0
while b <= n <= 4000000:
    if b % 2 == 0:
        total += b
    b = a + b
    a = b

print("Sum of even Fibonacci terms till", n, ": ", total)
