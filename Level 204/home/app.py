
# 1) შექმენი კლასი Player: რომელსაც ექნება name, score, level. შექმენი 3 მოთამაშე და დაბეჭდე: რომელი მოთამაშეა ყველაზე მაღალი score-ით

# Homework 1

class Player:
  def __init__(self, name, score, level):
    self.name = name
    self.score = score
    self.level = level

pl_1 = Player("Davit", 21, 204)
pl_2 = Player("Aleksandre", 18, 204)
pl_3 = Player("Ana", 25, 204)

def getHighest(scores):
  return max(scores)

print(getHighest([pl_1.score, pl_2.score, pl_3.score]))

# 2) შექმენი კლასი Product: რომელსაც ექნება name, price, quantity. შექმენი პროდუქტების სია და დაბეჭდე ყველაზე ძვირი და ყველაზე იაფი პროდუქტები

# Homework 2

class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

prod_1 = Product("Apple", 10, 1)
prod_2 = Product("Bread", 5, 2)
prod_3 = Product("Chocolate", 15, 3)

arr = [prod_1, prod_2, prod_3]

def get_min_max(arr):
  pr = []
  for i in arr:
    pr.append(i.price)

  arr_min = min(pr)
  arr_max = max(pr)

  for i in arr:
    if i.price == arr_min:
      print(f"Cheapest product is {i.name}, price: {i.price}")
    elif i.price == arr_max:
      print(f"Expensive product is {i.name}, price: {i.price}")
    else:
      pass

get_min_max(arr)

# 3) შექმენი კლასი ExamResult: რომელსაც ექნება student_name, math, english, science. შექმენი 2 სტუდენტი და დაბეჭდე: ვის აქვს ჯამური ქულა მეტი.

# Homework 3

class ExamResult:
  def __init__(self, student_name, math, english, science):
    self.student_name = student_name
    self.math = math
    self.english = english
    self.science = science

student_1 = ExamResult("Davit", 90, 100, 60)
student_2 = ExamResult("Aleksandre", 70, 100, 70)

def getExamScoreSum(student):
  res = 0
  res += student.math
  res += student.english
  res += student.science
  return res

res_1 = getExamScoreSum(student_1)
res_2 = getExamScoreSum(student_2)

def getBetterScore(score1, score2):
  if score1 > score2:
    print(f"{student_1.student_name} with score {score1} has more score than {student_2.student_name} with score {score2}")
  elif score1 == score2:
    print(f"{student_1.student_name} has same score as {student_2.student_name}. score: {score1}")
  else:
    print(f"{student_2.student_name} with score {score1} has more score than {student_1.student_name} with score {score2}")

getBetterScore(res_1, res_2)

# 4) შექმენი კლასი BankAccount: რომელსაც ექნება owner, balance, currency. შექმენი 2 ანგარიში და დაბეჭდე: რომელი ანგარიშია უფრო დიდი თანხით.

# Homework 4

class BankAccount:
  def __init__(self, owner, balance, currency):
    self.owner = owner
    self.balance = balance
    self.currency = currency

acc_1 = BankAccount("Davit Shavidze", 10000, 1000)
acc_2 = BankAccount("Cotne Gagnidze", 5000, 900)

def getBigger(acc_1, acc_2):
  if acc_1.balance > acc_2.balance:
    print(f"{acc_1.owner} has more money on his balance (${acc_1.balance}) than {acc_2.owner} with balance of (${acc_2.balance})")
  elif acc_1.balance == acc_2.balance:
    print(f"{acc_1.owner} and {acc_2.owner} have same balance on their bank accounts (${acc_1.balance})")
  else:
    print(f"{acc_2.owner} has more money on his balance (${acc_2.balance}) than {acc_1.owner} with balance of (${acc_1.balance})")

getBigger(acc_1, acc_2)

# 5) შექმენი კლასი Subscription: რომელსაც ექნება user_name, plan("free", "basic", "pro"), months_active. წესები: free -> max 1 month, basic -> max 6 months, pro -> unlimited. დაბეჭდე რომელ მომხმარებლებს აქვთ ვალიდური subscription. ლოგიკა დაწერე class-ის გარეთ

# Homework 5

class Subscription:
  def __init__(self, user_name, plan, months_active):
    self.user_name = user_name
    self.plan = plan
    self.months_active = months_active

def is_valid_sub(sub):
  if sub.plan == "free":
    if sub.months_active <= 1:
      return f"Free Valid Subscription active"
  elif sub.plan == "basic":
    if sub.months_active <= 6:
      return f"Basic Valid Subscription active"
  elif sub.plan == "pro":
    return f"Pro Valid Subscription active"
  else:
    return False

subs = [
  Subscription("Davit", "free", 1),
  Subscription("DzukDzuka", "basic", 5),
  Subscription("Ana", "basic", 7),
  Subscription("Saba", "pro", 12)
]

for i in subs:
  if is_valid_sub(i):
    print(f"{i.user_name} have valid {i.plan} subscription")