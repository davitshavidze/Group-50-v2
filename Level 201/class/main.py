
file = open("Level 201/class/text.txt")
file_2 = open("Level 201/class/main.js")

print(file.read())
print(file_2.read())

with open("Level 201/class/text.txt") as file:
  print(file.read())
  
with open("Level 201/class/main.js") as file_2:
  print(file_2.read())

with open("Level 201/class/text2.txt") as file:
  print([(x + " GOA") for x in file.read().strip().split(" ")])