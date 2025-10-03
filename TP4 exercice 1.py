class StringFoo():
    def __init__(self):
        self.message = ""
    def message(self, txt):
        print(txt.upper())

test = StringFoo
test.message(test, "Fromage")