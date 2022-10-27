#Пара2
# class Student:
#     def __init__(self):
#         self.height = 160
#         print("I am a live!")
#
#
# first = Student()
# print(first.height)

# class Student:
#      def __init__(self, name, height = 180, age = 18):
#          self.name = name
#          self.height = height
#          self.age = age

# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return a ** 2

#Дз пра2
# class Birds:
#     def __init__(self, name, age, color, weight):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.weight = weight
#
# cat1 = Birds('Piter', 3, 'blu', 12)
# cat2 = Birds('fortniter', 5, 'red', 9)
# cat3 = Birds('bulion', 2, 'purple', 10)

# print(cat1.name, cat1.age, cat1.color, cat1.weight)
# print(cat2.name, cat2.age, cat2.color, cat2.weight)
# print(cat3.name, cat3.age, cat3.color, cat3.weight)


#Пара3


# class Student:
#
#     def __init__(self, name):
#         self.name = name
#         self.progress = 0
#         self.gladness = 50
#         self.alive = True
#
#     def to_study(self):
#         print("Time to study")
#         self.pro
# # class Girl:
# #     species = "bird"
# #     def __init__(self, height=160):
# #         self.height = height
# #
# #     def grow(self, height=1):
# #         self.height += height
# #
# #
# # kate = Girl(height=170)
# # kate.grow(height=15)
# # print(kate.height)gress += 0.5
#         self.gladness -= 2
#
#     def to_sleep(self):
#         print("Time to sleep")
#         self.gladness += 5
#
#     def to_chill(self):
#         print("Time to chill")
#         self.gladness += 6
#         self.progress -= 0.2
#
#     def is_alive(self):
#         if self.progress < -0.5:
#             self.alive = False
#
#         elif self.gladness <= 0:
#             print('Depression')
#             self.alive = False
#
#
#     def end_of_day(self):
#         print(f"Gladness = {self.gladness}")
#         print(f"Progress = {self.progress}")


#Пара 4

class Human:
    def __init__(self, name = "Human"):
        self.name = name


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers_name(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers")
            for passenger in self.passengers:
                print(passenger.name)

        else:
            print(f"There are no passenger in {self.brand}")


nick = Human("Nick")
kate = Human("Kate")
car = Car("BMW")

car.add_passengers(nick)
car.add_passengers(kate)
car.print_passengers_name()


