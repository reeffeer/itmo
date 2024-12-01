class Button:

    def __init__(self, text, link):
        self.text = text
        self.link = link


home = Button('Home', '/home')
catalog_msk = Button('Catalog', '/msk/catalog')


print(home.text)
print('Button ' + home.text + ' has a link ' + home.link)

print('\n')

print(catalog_msk.text)
print('Button ' + catalog_msk.text + ' has a link ' + catalog_msk.link)


class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Click on locator - {}".format(self.loc)


home_two = ButtonTwo('Home', '/home', 'button#home')

print(home_two.click())


class Input:

    def __init__(self, loc):
        self.loc = loc

search = Input('input#search')

print(search.loc)
