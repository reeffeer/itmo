def task_1():
    a = 3
    b = 5.07
    c = 'Hello'
    d = [1, '2', 3.5]
    e = True
    print(type(a), "\n", type(b), "\n", type(c), "\n", type(d), "\n", type(e))


task_1()


def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21] #Последовательность Фибоначчи
    print(a[0], a[1], a[2])


task_2()


def task_3(a: int) -> int:
    return a ** 2


print(task_3(3))
