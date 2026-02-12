# შექმენი shopping cartი რომელსაც ექნება გამართული რეგისტრაცია და ლიგინი, ასევე ქართში შეგვეძლება პროდუქტების დამატება, ამოშლა და რედაქტირება python file handling-ის გამოყენებით.

register = input("Do you want to register? (yes/no): ")
file = ""
cart = []

with open("./Level 203/class/users.txt") as readen:
  file = readen.read()

prods = [
  {"apple": 2},
  {"Xinkali": 100},
  {"Pinapple": 5},
  {"Shawarma": 15},
  {"Watermelon": 10},
]

def addProd(curr, order):
  curr = list(curr)
  for i in range(len(curr)):
    if i == 2:
      if order == 5:
        order -= 1
        curr[i].append(prods[order])
      else:
        curr[i].append(prods[order - 1])
    else:
      pass
  print(tuple(curr))
  return tuple(curr)

def update():
  return

if register == "yes":
  email = input("Enter your email: ")

  while True:
    if email in list(file):
      print("User already registered with this email!")
      break
    password = input("Enter your password: ")
    if len(password) < 8:
      print("Password must be at least 8 charachters!")
      break
    if email != "":
      with open("./Level 203/class/users.txt", "a") as main:
        main.write(f"('{email}', '{password}', {cart})\n")
        break
    else:
      print("Email or password is incorrect!")
elif register != "yes":
  login = input("Do you want to login? (yes/no): ")

  if login == "yes":
    log_email = input("Enter your email: ")
    log_pass = input("Enter your password: ")
    curr = ""

    for i in file.split("\n"):
      read = eval(i)
      if log_email in read and log_pass in read:
        print(f"Welcome dear user!")
        curr = eval(i)
        print(curr)

        acc_cart = input("Do you want to add products in your cart? (yes/no): ")

        if acc_cart == "yes":
          user_inp = int(input("What you want to add cart? \n 1. Apple: 2$ \n 2. Xinkali: 100$ \n 3. Pinapple: 5$ \n 4. Shawarma: 15$ \n 5. Watermelon: 10$ \nNumber: "))
          break
        else:
          print("Goodbye!")
          break
else:
  print("Goodbye!")