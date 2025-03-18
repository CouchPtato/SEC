filename = input("Enter filename: ")
with open(filename, "r") as file:
    text = file.read()

char_freq = {}
for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)

if filename.endswith(".py"):
    print("This is a Python file.")
elif filename.endswith(".c"):
    print("This is a C file.")
else:
    print("This is a text file.")
