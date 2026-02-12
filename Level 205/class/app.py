
# გვაქვს ცარიელი ტექსტური ფაილი, შევქმნათ კლასი TodoList, გვქონდეს რაღაც მეთოდები რომლითაც todolistში ჩავამატებთ task-ებს, ასევე ამოვშლით თასქებს და მოვნიშნავთ შესრულებულად, ეს ყველა ასევე უნდა ჩაემატოს და წაიშალოს ცარიელი ფაილიდანაც, მაგისთვის გამოვიყენოთ file handling

class TodoList:
  def __init__(self, task):
    self.task = task

  def add_to_list(self):
    with open('./Level 205/class/text.txt', 'a') as f:
      f.write(f"\n{self.task}")

  def remove_task(self, task):
    with open('./Level 205/class/text.txt', 'r') as f:
      readed = f.read().strip().split('\n')
      res = []

      for i in readed:
        if i != task:
          res.append(i)

      with open('./Level 205/class/text.txt', 'w') as file:
        file.write("\n".join(res))


val = input("Enter value to add in tasks: ")

task = TodoList(val)
task.add_to_list()
