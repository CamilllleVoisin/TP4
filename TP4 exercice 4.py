"""
TP4 exercice 4
Par Camille Voisin
Le 8 Octobre 2025
"""



import random as rd

def beggining():
    class Hero:
        def __init__(self, hp, at, ac, lvl, name):
            self.hp = hp
            self.at = at
            self.ac = ac
            self.lvl = lvl
            self.name = name
        def attack(self, atta):
            self.atta = atta + self.at
            return self.atta

        def degatsair(self, atair):
            self.atair = atair
            return self.atair


    chara = Hero((rd.randint(1, 10) + rd.randint(1, 10)), rd.randint(1, 6), rd.randint(1, 6), "1", "Bundur")
    print(f"\nVous avez : {chara.hp}HP")
    print(f"Votre force d'attaque est de {chara.at}:")
    print(f"Votre défense est de : {chara.ac}")
    print(f"Vous êtes niveau {chara.lvl}")
    print(f"Votre nom est : {chara.name}")
    attaquer = input("Voulez vous attaquer l'air? \nOui\nNon\n")
    if attaquer == "Oui" or "oui":
        print(f"Vous attaquez dans le vide et faites {chara.attack(rd.randint(1, 6))} dégats à l'air.")
        chance_replique = rd.randint(1, 2)
        if chance_replique == 1:
            print("L'air vous attaque en retour!")
            degatsPrits = chara.degatsair(rd.randint(1, 6))
            print(f"Vous prenez {degatsPrits} dégats!")
            if degatsPrits - chara.ac <= 0:
                print("Votre défense est assé forte pour annuler les dégats, bien joué!")
                print(f"Vous avez maintenant {chara.hp -0}HP\n")
                beggining()
            elif degatsPrits - chara.ac > 0:
                print(f"Votre défense n'est pas assez bonne vous prenez quelques dégats : {degatsPrits - chara.ac} dégats")
                print(f"Vous avez maintenant {chara.hp - chara.ac}HP\n")
                beggining()

        elif chance_replique == 2:
            print("L'air vous dit : Tu as de la chance, petit, je n'vais pas t'attaquer, pour l'instant...\n")
            beggining()
    elif attaquer == "Non" or "non":
        print("Le menu reprend du debut.")
        beggining()
beggining()