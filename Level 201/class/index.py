
arr = ["Davit", "Gabrieli", "Andria", "Ana", "Luka"]

# Way 1
by_a = [x for x in arr if x.lower().startswith("a")]

# Way 2
by_a_2 = [y for y in arr if y.lower()[0] == "a"]

print(by_a)
print(by_a_2)
