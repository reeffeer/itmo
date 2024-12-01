from task_9_checks import Checks


class Input(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


search = Input('Search', 'input#search')

#print(search.text)
print(search.check_text())


class Button(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


run = Button('Run', 'press#run')

#print(run.loc)
print(run.check_text())


class Title(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


name = Title('Name', 'show#name')

#print(name.loc)
print(name.check_text())


class Link(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


forward = Link('/next', 'press#next')

#print(forward.text)
print(forward.check_text())
