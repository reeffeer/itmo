class Page:

    def __init__(self, url):
        self.url = url


    def get(self):
        print(self.url)


home = Page('https://backseat.ru/')

home.get()
