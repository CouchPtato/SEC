birthdays = {"Abhay": "2004-10-06", "Ritu": "2000-10-12"}
name = input("Enter name: ")
print("Birthday:", birthdays.get(name, "Not found"))

sentence = "Hello world, This is question 12"
words = sentence.split()
print("Split words:", words)
print("Joined sentence:", " ".join(words))

