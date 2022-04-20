
# задание 3


def type_logger(func):
    print(type_logger)

    def arg_f(x):
        class_x = type(x)
        return f'{x}: {class_x}'
    return arg_f

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(6)
print(a)
# 5: <class 'int'>