"""一个用来模拟汽车的类"""

class Car:
    """模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化汽车的描述"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 添加一个里程表属性，默认值为0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        修改里程表读数
        禁止回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """让里程表度数增加指定的量"""
        self.odometer_reading += miles



