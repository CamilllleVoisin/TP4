"""
TP4 exercice 1
Par Camille Voisin
Le 3 Octobre 2025
"""


class StringFoo():
    def __init__(self):
        self.message = ""
    def message(self, txt):
        print(txt.upper())

test = StringFoo
test.message(test, "Fromage")