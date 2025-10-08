"""
TP4 exercice 3
Par Camille Voisin
Le 6 Octobre 2025
"""


from math import pi

class Cercle:
    def __init__(self, rayon):
        self.rayon = ""
        self.aire = pi*rayon**2
        self.circo = 2*pi*rayon

donnee = Cercle(789)
print(f"L'aire du cercle est de {donnee.aire} cm2")
print(f"La circonférence du cercle est de {donnee.circo}cm2")