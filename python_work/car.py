class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odemeter(self, mileage):
        if mileage >= self.odemeter_reading:
            self.odemeter_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odemeter_reading += miles

#将实例用作属性
class Battery():
    """一次模拟电动汽车的简单尝试"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size=battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a  "+str(self.battery_size)+" -kwh battery.")

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性，在初始化电动汽车特有的属性"""
        super().__init__(make,model,year)
        self.battery=Battery()