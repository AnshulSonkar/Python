# First Class
# class Car:
#     brand = "Toyota"
#     color = "Red"
#     speed = 120


# car1 = Car()

# print(car1.brand)
# print(car1.color)
# print(car1.speed)
# 


#Creating Methods Inside a Class 
class Car:

    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")


car1 = Car()

car1.start()
car1.stop()
