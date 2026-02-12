# გვაქვს ერთი ტექსტური ფაილი, რომელშიც არის რაიმე დიდი ზომის ტექსტი, ჩვენი მიზანია გავაკეთოთ კლასი, რომელსაც ექნება თავისი მეთოდები და დაითვლის თუ რამდენი კითხვითი და რამდენი თხრობითი წინადადებაა ჩვენს ტექსტურ ფაილში

class sentCounter():
  def __init__(self, path):
    self.path = path

  def checkSentence(self):
    with open(self.path, "r", encoding="utf-8") as file:
      readed = file.read().strip().split("\n")
      read_count = 0
      quest_count = 0

      for i in readed:
        if '?' in i:
          quest_count += 1
        elif '!' or '.' in i:
          read_count += 1

      print(f"ბრძანებითი / თხრობითი სიტყვები count: {read_count}")
      print(f"კითხვითი სიტყვები count: {quest_count}")

  def checkPalindrome(self):
    pal = []
    res = []
    with open(self.path, 'r', encoding="utf-8") as file:
      readed = file.read().strip().split('\n')

      for i in readed:
        res.append(i.strip('.?/!'))
        for x in i.split():
          if len(x) > 2:
            if x == x[::-1]:
              pal.append(x)
      print(f"Palindrome words: {pal}")

c1 = sentCounter("./Level 207/home/text.txt")
c1.checkSentence()
c1.checkPalindrome()