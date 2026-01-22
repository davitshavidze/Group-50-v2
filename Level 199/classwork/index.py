
# 1) map ფუნქციის და lambdaს გამოყენებით ლისტის ყველა ელემენტი აქციე uppercaseებად. names = ["nika", "ana", "aleqsandre', "daviti", "gabrieli", "luka"]

names = ["nika", "ana", "aleqsandre", "daviti", "gabrieli", "luka"]

upper = list(map(lambda x: x.upper(), names))

print(upper)

# 2) filter ფუნქციის და lambdaს გამოყენებით შექმენი ახალი სია და ახალ სიაში ჩაამატე მხოლოდ ის სიტყვები რომელთა სიგრძეც მეტია 4-ზე.  names = ["nika", "ana", "aleqsandre', "daviti", "gabrieli", "luka"]

names = ["nika", "ana", "aleqsandre", "daviti", "gabrieli", "luka"]

len_4 = list(filter(lambda x: len(x) > 4, names))

print(len_4)

# 3) sort ფუნქციის გამოყენებით დაალაგე (name, age) tuple-ების სია ასაკის მიხედვით. people = [
#   ("Nika", 21),
#   ("Ana", 19),
#   ("Gio", 25)
# ]

people = [
    ("Nika", 21),
    ("Ana", 19),
    ("Gio", 25)
]

sorted_arr = sorted(people, key=lambda x: x[1])

print(sorted_arr)