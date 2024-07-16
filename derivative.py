from typing import Callable


class CalcDerivativeLimit:
    """
    Вычисление производных через предел
    """
    def __init__(self, function: Callable, function_args: dict, delta: float = 1e-3):
        """
        :param function: - объект функции от которой нужно найти производную
        :param function_args: - словарь, где ключ строковое значение аргумента, значение - числовой аргумент функции
        :param delta: - инкремент значений
        """
        self.function = function
        self.function_args = function_args
        self.delta = delta
        self.result = self.function(**function_args)

    def calc_from_simple_arg(self, arg: str):
        """
        :param arg: - строковое значение аргумента, например, 'Ro' или 'compound'
        :return: производную от arg
        """
        if arg not in self.function_args:
            raise Exception(f'Argument {arg} not in function args')
        new_args = {key: (val + self.delta * val if key == arg else val)
                    for key, val in self.function_args.items()}
        increment_result = self.function(**new_args)
        diff = (increment_result - self.result) / (self.function_args[arg] * self.delta)
        return diff

    def calc_from_all_args(self):
        """
        Вычисляет производные от всех аргументов
        :return: словарь производных, где ключ - название аргумента, значение - производная
        """
        return {key: self.calc_from_simple_arg(key)
                for key, arg in self.function_args.items()}


if __name__ == '__main__':
    # тестовая функция
    def func(x, z):
        return x ** 3 * z
    # аргументы функции
    args = {
        'x': 4,
        'z': 2
    }
    # повысим точно до 1e-10
    derivative = CalcDerivativeLimit(func, args, delta=1e-10)
    # производная через предел от 'x'
    y = derivative.calc_from_simple_arg('x')
    print(y)
    # словарь с производными от 'x' и 'z'
    y = derivative.calc_from_all_args()
    print(y)
