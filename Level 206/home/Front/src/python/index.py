
#  გვაქვს ცარიელი ტექსტური ფაილი, შევქმნათ კლასი TodoList, გვქონდეს რაღაც მეთოდები რომლითაც todolistში ჩავამატებთ task-ებს, ასევე ამოვშლით თასქებს და მოვნიშნავთ შესრულებულად, ეს ყველა ასევე უნდა ჩაემატოს და წაიშალოს ცარიელი ფაილიდანაც, მაგისთვის გამოვიყენოთ file handling

class TodoList:
  def __init__(self, file):
    self.file = file

  def add_task(self, task):
    with open(self.file, 'a') as file:
      file.write(f"- | {task}\n")
  
  def delete_task(self, task):
    with open(self.file, "r") as file:
      readed = file.read().strip().split('\n')
      res = []

      for i in readed:
        if i[4:] != task:
          res.append(i)

      with open(self.file, "w") as f:
        f.write("\n".join(res))

  def getAllTasks(self):
    with open(self.file, 'r') as file:
      readed = file.read()
      print(readed)

  def mark_done(self, task):
    with open(self.file, "r") as file:
      readed = file.read().strip().split("\n");
      res = []

      for i in readed:
        if '-' in i and i[4:] == task:
          i = i.replace('-', '+')
          res.append(i)
        else:
          res.append(i)

      with open(self.file, "w") as f:
        f.write("\n".join(res))
  def unmark_done():
    pass

first_inp = input("Do you want to register? (yes/no): ")

if first_inp == "yes":
  name = input("Enter your name: ")
  full = ""
  readed = ""

  with open("./Level 206/home/Front/src/python/users.txt") as file:
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
      with open("./Level 206/home/Front/src/python/users.txt", "a") as register:
        register.write(f"{full}\n")
      break
    else:
      print("Invalid Enters!")
elif first_inp != "yes":
  second_inp = input("Do you want to Login? (yes/no): ")

  if second_inp == "yes":
    log_name = input("Enter your name: ")
    log_pass = input("Enter your password: ")

    with open("./Level 206/home/Front/src/python/users.txt") as file:
      readed = file.read().split()
      for i in range(len(readed)):
        if log_name in readed and log_pass in readed:
          print(f"Welcome {log_name}")
          c1 = TodoList("./Level 206/home/Front/src/python/todoApp.txt")
          while True:
            print("Choose operation: ")
            print("1) Check Tasks: ")
            print("2) Add Task: ")
            print("3) Delete Task: ")
            print("4) Mark Done Task: ")
            print("5) Unmark Task: ")
            print("6) Leave Out: ")

            choice = int(input('Enter an operation number: '))
            print("")

            if choice == 1:
              c1.getAllTasks()
              print("")
            elif choice == 2:
              new_task = input('Enter new task to add: ')
              if new_task != '':
                c1.add_task(new_task)
              else:
                print("Error! Try Again.")
            elif choice == 3:
              del_task = input('Enter a task you want to delete: ')
              if del_task != '':
                c1.delete_task(del_task)
              else:
                print("Error! Try Again.")
            elif choice == 4:
              check_task = input('Enter a task to mark done: ')
              if check_task != '':
                c1.mark_done(check_task)
              else:
                print("Error! Try Again.")
            else:
              print("You left the system.")
              break
        else:
          print("User not Found!")
          break
  elif second_inp != "yes":
    reset = input("Do you want to reset your password? (yes/no): ")

    if reset == "yes":
      res_name = input("Enter your name to reset password: ")
      res_pass = input("Enter your old password to reset password: ")
      with open("./Level 206/home/Front/src/python/users.txt") as file:
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

              with open("./Level 206/home/Front/src/python/users.txt", "w") as main:
                main.write("\n".join(readed))

              print(f"Password was Succesfully reseted! new password: {new_res}")
else:
  print("Goodbye!")