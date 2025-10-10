""""
TP4 exercice 6
Camille Voisin 404
10 octobre 2025
"""


import random as rd


class CharaDND:
    def __init__(self, force, const, dex, intel, sage, char):
        self.force = force
        self.const = const
        self.dex = dex
        self.intel = intel
        self.sage = sage
        self.char = char
    def bonuses1(self,bat):
        self.bat = bat
        return self.bat
    def bonuses2(self, bac):
        self.bac = bac
        return self.bac


charap = CharaDND(rd.randint(1, 20), rd.randint(1, 20),
                  rd.randint(1, 20), rd.randint(1, 20), rd.randint(1, 20), rd.randint(1, 20))

print(f"Votre personnage a {charap.force} points de force.")
print(f"Votre personnage a {charap.const} points de constitution.")
print(f"Votre personnage a {charap.dex} points de déxterité.")
print(f"Votre personnage a {charap.intel} points d'intelligence.")
print(f"Votre personnage a {charap.sage} points de sagesse.")
print(f"Votre personnage a {charap.char} points de charisme.")
print(f"Votre bonus d'attaque est de {charap.bonuses1(rd.randint(1, 6))}")
print(f"Votre bonus de défense est de {charap.bonuses2(rd.randint(1, 6))}")