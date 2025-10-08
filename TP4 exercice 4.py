"""
TP4 exercice 4
Par Camille Voisin
Le 8 Octobre 2025
"""



import random as rd


class Hero:
    def __init__(self, hp, at, ac, lvl, name):
        self.hp = rd.randint(1, 10) + rd.randint(1, 10)
        self.at = rd.randint(1, 6)
        self.ac = rd.randint(1, 6)
        self.lvl = ""
        self.name = name
    def attack(self, atta):
        self.atta = rd.randint(1, 6)

chara = Hero((rd.randint(1, 10) + rd.randint(1, 10)), rd.randint(1, 6), rd.randint(1, 6), "1", "Bundur")
print(f"Vous avez : {chara.hp}HP")
print(f"Votre force d'attaque est de {chara.at}:")
print(f"Votre défense est de : {chara.ac}")
print(f"Vous êtes niveau {chara.lvl}")
print(f"Votre nom est : {chara.name}")
