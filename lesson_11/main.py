#MANUAL 11

# FIRST CODE
class Auto:
    @staticmethod
    def get_class_info():
        print('Детальная информация о классе')

Auto.get_class_info()

# SECOND CODE
class MyClass:
    @staticmethod
    def on_sum_1(param_1, param_2):
        return param_1 + param_2

    def on_sum_2(self, param_1, param_2):
        return param_1 + param_2

    def on_sum_3(self, param_1, param_2):
        return MyClass.on_sum_1(param_1, param_2)

print(MyClass.on_sum_1(20, 30))