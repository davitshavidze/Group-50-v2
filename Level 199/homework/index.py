# 1) მოცემულია სია nums = [1, 2, 3, 4, 5], map-ის და lambda-ს გამოყენებით მიიღე ახალი სია სადაც თითოეული რიცხვი გამრავლებულია 3-ზე

nums = [1, 2, 3, 4, 5]

multiple = list(map(lambda x: x * 3, nums))

print(multiple)

# 2) მოცემულია სია nums = [3, -1, 0, -7, 8, -2], filter-ის გამოყენებით დატოვე მხოლოდ უარყოფითი რიცხვები

nums = [3, -1, 0, -7, 8, -2]

filtered = list(filter(lambda x: x < 0, nums))

print(filtered)

# 3) მოცემულია სია nums = [1, 2, 3, 4, 5, 6], filter -> map ის გამოყენებით დატოვე ლუწი რიცხვები და თითოეული გაამრავლე 2-ზე

nums = [1, 2, 3, 4, 5, 6]

filtered = list(filter(lambda x: x % 2 == 0, nums))

multiplied = list(map(lambda x: x * 2, filtered))

print(multiplied)

# 4) მოცემულია სია nums = [1, 2, 3, 4, 5, 6], filter -> map ის გამოყენებით აიყვანე ყველა რიცხვი კვადრატში და დატოვე მხოლოდ ის რიცხვები რომლებიც 
# მეტია 20-ზე 

nums = [1, 2, 3, 4, 5, 6]

powered = list(map(lambda x: x ** 2, nums))

after_filter = list(filter(lambda x: x > 20, powered))

print(after_filter)

# 5) nums = [9, 2, 7, 4, 5, 6, 1], დატოვე მხოლოდ კენტი რიცხვები დაა დაალაგე ზრდადობით

nums = [9, 2, 7, 4, 5, 6, 1]

filtered = list(filter(lambda x: x % 2 != 0, nums))

sort = sorted(filtered, key=lambda x: x)

print(sort)