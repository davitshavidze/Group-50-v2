
readed = ""

with open("./Level 202/class/names.txt", "r") as file:
  readed = " ".join([(x + "-GOA") for x in file.read().strip().split(" ")])

with open("./Level 202/class/names.txt", "w") as file_2:
  file_2.write(readed)