def one(a, b):
    if a > b:
        print(a)
    else:
        print(b)


one(1, 5)


def difference(num1, num2):
    if abs(num1 - num2) == 135:
        print('yes')
    else:
        print('No')


difference(137, 3)


def get_season(month: int):
    if 1 <= month <= 12:
        if month in (12, 1, 2):
            print("Зима")
        elif month in (3, 4, 5):
            print("Весна")
        elif month in (6, 7, 8):
            print("Лето")
        elif month in (9, 10, 11):
            print("Осень")
    else:
        print("Некорректный номер месяца. Введите число от 1 до 12.")


get_season(5)


def is_more_than_ten(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")


is_more_than_ten(32, 49, 12)


def find_positive_numbers_quantity(numbers):
    if len(numbers) != 5:
        raise ValueError("The list must contain exactly 5 numbers.")
    else:
        count = sum(1 for num in numbers if num > 0)
    return count


print(find_positive_numbers_quantity([2, 0, -3, 5, 101]))


def calculate_days(years, months):
    days = years * 12 * 29 + months * 29
    print(days)


calculate_days(1, 6)
