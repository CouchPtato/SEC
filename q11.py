birthdays = {"Alice": "2000-06-15", "Bob": "1998-02-22"}
name = input("Enter name: ")
print("Birthday:", birthdays.get(name, "Not found"))

sentence = "Hello world, Python is great"
words = sentence.split()
print("Split words:", words)
print("Joined sentence:", " ".join(words))
