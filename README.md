# Метод Ньютона и нахождение производной через предел на **python**
## Описание вычислений производных
Класс `CalcDerivativeLimit` в файле **derivative.py** предназначен для числового вычисления производных функций с помощью пределов.\
Он позволяет вычислить производные от отдельных аргументов или от всех аргументов функции.
### Использование
### Инициализация
Класс инициализируется с помощью трёх параметров:
* `function`: объект функции, от которой нужно найти производную.
* `function_args`: словарь, где ключи - строковые значения аргументов, а значения - числовые аргументы функции.
* `delta`: инкремент значений (по умолчанию равен `1e-3`).
### Методы
* `calc_from_simple_arg(arg: str)`
Вычисляет производную от указанного аргумента. Возвращает производную от аргумента arg.
* `calc_from_all_args()`
Вычисляет производные от всех аргументов функции. Возвращает словарь, где ключи - названия аргументов, а значения - соответствующие производные.
### Пример использования
```python
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
```
## Описание Метода Ньютона
Класс `NewtonMethod` в файле **newton_method.py** предназначен для вычисления корней уравнений с помощью метода Ньютона.\
Он использует производную, вычисленную через предел, для нахождения корня.
### Использование
### Инициализация
Класс инициализируется с помощью шести параметров:
* `initial_val`: начальное значение алгоритма.
* `function`: объект функции, для которой нужно найти корень.
* `kwargs_function`: словарь аргументов функции, кроме искомого.
* `key`: название аргумента, который будет вычисляться.
* `eps`: точность алгоритма (по умолчанию равна `1e-6`).
* `stop`: количество итераций для остановки алгоритма (по умолчанию равна `1000`).
### Методы
`calculate()` \
Вычисляет корень уравнения методом Ньютона. Возвращает корень уравнения.
Пример использования
```python
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
```