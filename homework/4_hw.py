class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return self.height * 2 + self.width * 2

    def square(self):
        return self.height * self.width


rect1 = Rectangle(4, 5)
print(f'Perimeter of the first rectangle is {rect1.perimeter()}')
print(f'Square of the first rectangle is {rect1.square()}')

rect2 = Rectangle(32, 12)
print(f'Perimeter of the second rectangle is {rect2.perimeter()}')
print(f'Square of the second rectangle is {rect2.square()}')

rect3 = Rectangle(17.5, 0.8)
print(f'Perimeter of the third rectangle is {rect3.perimeter()}')
print(f'Square of the third rectangle is {rect3.square()}')


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f"Сумма {self.a} и {self.b} равна {result}")
        return result

    def multiplication(self):
        result = self.a * self.b
        print(f"Произведение {self.a} и {self.b} равно {result}")
        return result

    def division(self):
        if self.b == 0:
            print("Ошибка: Деление на ноль невозможно!")
            return None
        result = self.a / self.b
        print(f"Частное {self.a} и {self.b} равно {result}")
        return result

    def subtraction(self):
        result = self.a - self.b
        print(f"Разность {self.a} и {self.b} равна {result}")
        return result


res = Math(21, 13)
res.addition()
res.subtraction()
res.multiplication()
res.division()


class Button:
    def __init__(self, text):
        self.text = text
        self.type = 'Кнопка'
        self.loc = ''


    def press_button(self):
        print(f'Клик по кнопке {self.text}')


class TextBox(Button):
    def __init__(self, text):
        super().__init__(text)
        self.type = 'Текстовое поле'


class CheckBox(Button):
    def __init__(self, text):
        super().__init__(text)
        self.type = 'Текстовое поле'


class RadioButton(Button):
    def __init__(self, text):
        super().__init__(text)
        self.type = 'Текстовое поле'


class WebTables(Button):
    def __init__(self, text):
        super().__init__(text)
        self.type = 'Текстовое поле'


class Buttons(Button):
    def __init__(self, text):
        super().__init__(text)
        self.type = 'Текстовое поле'


class Links(Button):
    def __init__(self, text):
        super().__init__(text)
        self.type = 'Текстовое поле'


class BrokenLinksImages(Button):
    def __init__(self, text):
        super().__init__(text)
        self.type = 'Текстовое поле'


class UploadDownload(Button):
    def __init__(self, text):
        super().__init__(text)
        self.type = 'Текстовое поле'


class DynamicProperties(Button):
    def __init__(self, text):
        super().__init__(text)
        self.type = 'Текстовое поле'


textBox = TextBox('Text Box')
checkBox = CheckBox('Check Box')
radioButton = RadioButton('Radio Button')
webTables = WebTables('Web Tables')
buttons = Buttons('Buttons')
links = Links('Links')
brokenLinks = BrokenLinksImages('Broken Links - Images')
uploadDownload = UploadDownload('Upload and Download')
dynamicProperties = DynamicProperties('Dynamic Properties')

textBox.press_button()
checkBox.press_button()
radioButton.press_button()
webTables.press_button()
buttons.press_button()
links.press_button()
brokenLinks.press_button()
uploadDownload.press_button()
dynamicProperties.press_button()
