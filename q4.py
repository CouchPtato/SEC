import sys

if len(sys.argv) != 3:
    print("Usage: python q4.py num1 num2")
else:
    num1, num2 = map(float, sys.argv[1:3])
    print("Sum:", num1 + num2)
