class Soda:

    def __init__(self, addition = None):
        self.addition = addition


    def show_my_drink(self):
        if self.addition:
            print(f'Soda and {self.addition}')

        else:
            print('Common soda')


drink1 = Soda()
drink2 = Soda('Strawberry')
drink1.show_my_drink()
drink2.show_my_drink()
