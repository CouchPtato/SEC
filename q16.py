filename = input("Enter filename: ")
with open(filename, "r") as file:
    text = file.read()

char_count = len(text)
word_count = len(text.split())
line_count = text.count("\n") + 1

print(f"Characters: {char_count}, Words: {word_count}, Lines: {line_count}")
