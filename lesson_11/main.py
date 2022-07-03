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

print(MyClass.on_sum_1(20, 30))
mc = MyClass()
print(mc.on_sum_2(20, 10))
print(mc.on_sum_2(40, 30))
print(mc.on_sum_3(50, 50))

class MyClass_2:
    @classmethod
    def my_method(cls, param):
        print(cls, param)

MyClass_2.my_method(30)
mc_2 = MyClass_2()
mc_2.my_method(70)

class User:
    def __init__(self, name, login, passwd, email):
        self.name = name
        self.login = login
        self.passwd = passwd
        self.email = email
    def on_get_data(self):
        print(f"имя: {self.name}, логин: {self.login}, " 
              f"пароль: {self.passwd}, email: {self.email}")

u = User("Ivan Ivanov", "IvIv", "11111", "iviv@mail.ru")
u.on_get_data()

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str__(self):
        return f'Name and surname: {self.name} {self.surname}'

class Teacher(Person):
    def to_teach(self, subj, *pupils):
        for pupil in pupils:
            pupil.to_take(subj)

class Pupil(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledges = []
    def to_take(self, subj):
        self.knowledges.append(subj)

class Subject:
    def __init__(self, *subjects):
        self.subjects = list(subjects)
    def my_list(self):
        return self.subjects

s = Subject("maths", "physics", "chemistry")

t = Teacher('Ivan', 'Ivanov')
print(t)

p_1 = Pupil("Petr", "Petrov")
p_2 = Pupil("Sergey", "Sergeev")
p_3 = Pupil("Vladimir", "Vladimirov")

print(f"{p_1}; {p_2}; {p_3}")

t.to_teach(s, p_1, p_2, p_3)

print(p_1.knowledges[0].my_list())


class OwnError(Exception):
    def __init__(self, text):
        self.text = text

inp_data = input('введите положительносе число: ')

try:
    inp_data = int(inp_data)
    if inp_data < 0:
        raise OwnError('вы ввели отричетельное число')
except ValueError:
    print('вы ввели не число')
except OwnError as err:
    print(err)
else:
    print(f'все хорошо, ваше число: {inp_data}')

import psutil

# Информация о системных вызовах и контекстных переключателях
print(psutil.cpu_stats())
