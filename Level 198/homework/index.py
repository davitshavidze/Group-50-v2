# 1) მოცემულია სია numbers = [1, 2, 3, 4, 5, 12, 24, -1, -3, 44, 65, 43], lambdaს გამოყენებით დააბრუნე მხოლოდ ის რიცხვები რომლებიც მეტია 3-ზე.

numbers = [1, 2, 3, 4, 5, 12, 24, -1, -3, 44, 65, 43]

func = lambda arr: [x for x in arr if x > 3]

print(func(numbers))

# 2) მოცემუმლია სია numbers = [1, 2, 3, 4, 5, 6], lambdaს გამოყენებით ახალ სიაში ჩაამატე მხოლოდ ლუწი რიცხვები

numbers = [1, 2, 3, 4, 5, 6]

func_2 = lambda arr: [x for x in arr if x % 2 == 0]

print(func_2(numbers))

# 3) მოცემულია words = ["hi", "hello", "world"], შექმენი lambda რომელიც აბრუნებს სტრინგების სიგრძეს

words = ["hi", "hello", "world"]

func_3 = lambda arr: [len(x) for x in arr]

print(func_3(words))

# 4) მოცემულია სია numbers = [2, 3, 4, 5, 7], lambdaს გამოყენებით სიის ყველა წევრი გაამრავლე საკუთარ ინდექსებზე და შემდეგ ჩაამატე ეს რიცხვები ახალ ცარიელ ლისტში

numbers = [2, 3, 4, 5, 7]
arr = []

multiplication = lambda arr: [(x * arr.index(x)) for x in arr]

for i in multiplication(numbers):
  arr.append(i)

print(arr)

# 5) მოცემულია სია numbers = [12, 24, 55, 67, 98], შექმენი lambda, რომელიც აბრუნებს რიცხვის ციფრების ჯამს.

numbers = [12, 24, 55, 67, 98]
arr_2 = []

func_4 = lambda arr: [str(x) for x in arr]

for i in func_4(numbers):
  sum = 0
  for x in i:
    sum += int(x)
  arr_2.append(sum)

print(arr_2)

