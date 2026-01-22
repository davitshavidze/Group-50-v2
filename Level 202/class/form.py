
first_inp = input("Do you want to register? (yes/no): ")
second_inp = input("Do you want to Login? (yes/no): ")

if first_inp == "yes":
  name = input("Enter your name: ")
  password = input("Enter your password: ")
  full = ""
  readed = ""

  while True:
    if name != "" and password != "":
      full = f"{name} {password}"
      with open("./Level 202/class/form.txt") as file:
        readed = file.read()
      with open("./Level 202/class/form.txt", "a") as register:
        register.write(f"\n{full}")
      break
    else:
      print("Invalid Enters!")

elif second_inp == "yes":
  log_name = input("Enter your name: ")
  log_pass = input("Enter your password: ")

  with open("./Level 202/class/form.txt") as file:
    readed = file.read().split()
    print(readed)
    for i in range(len(readed)):
      if readed[i] == log_name and readed[i + 1] == log_pass:
        print(f"Welcome {log_name}")
        break
      else:
        print("User not Found!")
        break
else:
  print("Goodbye!")



