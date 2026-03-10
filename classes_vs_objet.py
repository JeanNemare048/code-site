class Livre:
    def __init__(self, type, longeur, text_size, ennuyant, color):
        self.type = type
        self.longeur = longeur
        self.text_size = text_size
        self.boring = ennuyant
        self.color = color

    def lire(self):
        print(f"Le {self.type} {self.color} de {self.longeur} pages est {self.boring}, car son texte est de taille {self.text_size}.")

livre1 = Livre("roman", "500", "petite", "ennuyant", "rouge")
livre1.lire()  # Utilisation de la méthode lire de l'objet livre1

livre2 = Livre("poème", "100", "medium", "ennuyant", "bleu")
livre2.lire()