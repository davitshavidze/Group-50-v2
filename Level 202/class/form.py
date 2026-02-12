
first_inp = input("Do you want to register? (yes/no): ")

if first_inp == "yes":
  name = input("Enter your name: ")
  full = ""
  readed = ""

  with open("./Level 202/class/form.txt") as file:
    readed = file.read()

  while True:
    if name in list(readed):
      print("User Already Exists!")
      break
    password = input("Enter your password: ")
    if len(password) < 8:
      print("password must be minimum 8 chars!")
      break
    if name != "" and password != "":
      full = f"{name} {password}"
      with open("./Level 202/class/form.txt", "a") as register:
        register.write(f"\n{full}")
      break
    else:
      print("Invalid Enters!")
elif first_inp != "yes":
  second_inp = input("Do you want to Login? (yes/no): ")

  if second_inp == "yes":
    log_name = input("Enter your name: ")
    log_pass = input("Enter your password: ")

    with open("./Level 202/class/form.txt") as file:
      readed = file.read().split()
      for i in range(len(readed)):
        if log_name in readed and log_pass in readed:
          print(f"Welcome {log_name}")
          break
        else:
          print("User not Found!")
          break
  elif second_inp != "yes":
    reset = input("Do you want to reset your password? (yes/no): ")

    if reset == "yes":
      res_name = input("Enter your name to reset password: ")
      res_pass = input("Enter your old password to reset password: ")
      with open("./Level 202/class/form.txt") as file:
        readed = file.read().split()
        for i in readed:
          if res_name in readed and res_pass in readed:
            new_res = input("Enter your new password: ")
            if len(new_res) < 8:
              print("password must be minimum 8 chars!")
            else:
              ind = readed.index(res_pass)
              readed.pop(ind)
              readed.insert(ind, new_res)

              with open("./Level 202/class/form.txt", "w") as main:
                main.write("\n".join(readed))

              print(f"Password was Succesfully reseted! new password: {new_res}")
else:
  print("Goodbye!")