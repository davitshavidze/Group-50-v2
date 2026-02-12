
# class 1

class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

st_1 = Student("Davit", 16, 10)
st_2 = Student("Nika", 14, 8)

print(st_1.name)
print(st_1.age)
print(st_1.grade)

print(st_2.name)
print(st_2.age)
print(st_2.grade)


# class 2

class Phone:
  def __init__(self, brand, storage, price):
    self.brand = brand
    self.storage = storage
    self.price = price

phone_1 = Phone("Iphone 16 pro", 128, 700)
phone_2 = Phone("Xiaomi F20", 128, 500)

def getGrater(phone1, phone2):
  if phone1.price > phone2.price:
    print(f"{phone1.brand} is grater in price than {phone2.brand}")
  else:
    print(f"{phone2.brand} is grater in price than {phone1.brand}")

getGrater(phone_1, phone_2)


# class 3

class Movie:
  def __init__(self, title, rating, year):
    self.title = title
    self.rating = rating
    self.year = year

film_1 = Movie("Counter Strike 2", 9, 2013)
film_2 = Movie("Aleksandre DzukDzuka Action", 10, 2011)
film_3 = Movie("Hachiko", 10, 2009)

def ratingGreater(film):
  if film.rating > 8:
    print(f"{film.title} rating is grater than 8!")
  else:
    pass

ratingGreater(film_1)
ratingGreater(film_2)
ratingGreater(film_3)