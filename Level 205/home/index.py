# გვაქვს ერთი ტექსტური ფაილი, სადაც წერია რენდომ ტექსტი და ჩვენი მიზანია გავაკეთოთ კლასი რომელსაც ექნება თავისი მეთოდები, ეს კლასი მიიღებს ინფორმაციას ამ ტექსტური ფაილიდან და დააბრუნებს ინფორმაციას თუ რამდენი ხმოვანი ასოა მიღებული ფაილის ტექსტში.

class getTextVowels:
  def __init__(self, path):
    self.path = path

  def count(self):
    count = 0
    vow = "aeiouAEIOU"

    with open(self.path, "r") as f:
      readed = f.read()
      for i in readed:
        if i in vow:
          count += 1
      return f"in sentence | '{readed}' | is {count} vowels."

c1 = getTextVowels("./Level 205/home/text.txt")
print(c1.count())