from typing import Callable

from derivative import CalcDerivativeLimit


class NewtonMethod:
    def __init__(self, initial_val: float | int, function: Callable, kwargs_function: dict, key: str,
                 eps: float = 1e-6, stop: int = 1000):
        """
        Расчет уравнения методом Ньютона (производная вычисляется через предел)
        :param initial_val: начальное значение алгоритма
        :param function: объект функции - уравнения
        :param kwargs_function: аргументы функции (кроме искомого) в виде словаря, где ключ - название аргумента
        :param key: название аргумента, который будет вычисляться
        :param eps: точность алгоритма
        :param stop: количество итераций для остановки
        """
        self.initial_val = initial_val
        self.func = function
        self.kwargs = kwargs_function
        self.key = key
        self.eps = eps
        self.stop = stop
        self.through_press = False
        self.pressure = None
        self.func_pres = None
        self.kwargs_pres = None

    def calculate(self):
        """
        Вычисление методом Ньютона
        :return: корень уравнения
        """
        k = 0
        while k < self.stop:
            self.kwargs[self.key] = self.initial_val
            fx = self.func(**self.kwargs)
            dfx = CalcDerivativeLimit(self.func, self.kwargs).calc_from_simple_arg(self.key)
            x_next = self.initial_val - fx / dfx
            if abs(self.initial_val - x_next) <= self.eps:
                return x_next
            self.initial_val = x_next
        raise StopIteration(f'The algorithm made {self.stop} iterations and did not converge.')


if __name__ == '__main__':
    # пример функции
    def func(x, a, b, c, d):
        return a * x ** 3 + b * x ** 2 + c * x + d
    # аргументы функции
    args = {
        'a': 1,
        'b': 9,
        'c': 27,
        'd': 27
    }
    newton = NewtonMethod(initial_val=1, function=func, kwargs_function=args, key='x')
    # вычисление корня уравнения
    y = newton.calculate()
    print(y)
