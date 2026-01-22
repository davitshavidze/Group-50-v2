
# მოცემულია რიცხვების სია: numbers = [1, 2, 3, 4, 5]. შექმენი lambda რომელიც ამ რიცხვებს გაამრავლებს 2-ზე. გამოიყენე for ციკლი რათა ახალ ლისთში ჩაამატო უკვე ორზე გამრავლებული რიცხვები.

numbers = [1, 2, 3, 4, 5]
new = []

twice = lambda arr: [x * 2 for x in arr]

for i in twice(numbers):
  new.append(i)

print(new)