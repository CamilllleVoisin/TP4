""""
TP4 exercice 5
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

charap = CharaDND(rd.randint(1, 20), rd.randint(1, 20), rd.randint(1, 20), rd.randint(1, 20), rd.randint(1, 20), rd.randint(1, 20))
print(f"Votre personnage a {charap.force} points de force.")
print(f"Votre personnage a {charap.const} points de constitution.")
print(f"Votre personnage a {charap.dex} points de déxterité.")
print(f"Votre personnage a {charap.intel} points d'intelligence.")
print(f"Votre personnage a {charap.sage} points de sagesse.")
print(f"Votre personnage a {charap.char} points de sagesse.")