# Задача "Изменять нельзя получать":
# В этой задаче мы реализуем классы транспорта,
# в которых нельзя будет просто так поменять цвет,
# мощность двигателя и прочие свойства,
# т.к. в реальной жизни это чаще всего делается не владельцем,
# а в специальных сервисах. Да, узнать значения этих свойств мы сможем, но вот изменить - нет.
#
# Вам необходимо создать 2 класса: Vehicle и Sedan,
# где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса Vehicle.
#
#
# Пункты задачи:
# Создайте классы Vehicle и Sedan.
# Напишите соответствующие свойства в обоих классах.
# Не забудьте сделать Sedan наследником класса Vehicle.
# Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color =  __color
        self.__engine_power = __engine_power

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower()),
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = self.new_color
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


# Вывод на консоль:
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: blue
# Владелец: Fedos
# Нельзя сменить цвет на Pink
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: BLACK
# Владелец: Vasyok