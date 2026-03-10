### AUCUNE MODIFICATION NÉCESSAIRE JUSQU'À LA LIGNE 67 ###
import random
import sys

ALEX = ("N", "H", "Br", "N", "N", "P", "O", "N")
ALFRED = ("R", "H", "Bl", "N", "N", "P", "O", "N")
ANITA = ("J", "F", "Bl", "N", "N", "P", "N", "N")
ANNE = ("N", "F", "Br", "N", "N", "G", "N", "N")
BERNARD = ("Br", "H", "Br", "O", "N", "G", "N", "N")
BILL = ("R", "H", "Br", "N", "N", "P", "N", "O")
CHARLES = ("J", "H", "Br", "N", "N", "P", "O", "N")
CLAIRE = ("R", "F", "Br", "O", "O", "P", "N", "N")
DAVID = ("J", "H", "Br", "N", "N", "P", "N", "N")
ERIC = ("J", "H", "Br", "O", "N", "P", "N", "N")
FRANS = ("R", "H", "Br", "N", "N", "P", "N", "N")
GEORGE = ("Bl", "H", "Br", "O", "N", "P", "N", "N")
HERMAN = ("R", "H", "Br", "N", "N", "G", "N", "O")
JOE = ("J", "H", "Br", "N", "O", "P", "N", "N")
MARIA = ("Br", "F", "Br", "O", "N", "P", "N", "N")
MAX = ("N", "H", "Br", "N", "N", "G", "N", "N")
PAUL = ("Bl", "H", "Br", "N", "O", "P", "N", "N")
PETER = ("Bl", "H", "Bl", "N", "N", "G", "N", "N")
PHILIP = ("N", "H", "Br", "N", "N", "P", "N", "N")
RICHARD = ("Br", "H", "Br", "N", "N", "P", "O", "O")
ROBERT = ("Br", "H", "Bl", "N", "N", "G", "N", "N")
SAM = ("Bl", "H", "Br", "N", "O", "P", "N", "O")
SUSAN = ("Bl", "F", "Br", "N", "N", "P", "N", "N")
TOM = ("N", "H", "Bl", "N", "O", "P", "N", "O")
BENJAMIN = ("N", "H", "Br", "N", "O", "P", "N", "N")

LISTE_VALEUR_PERSO = [ALEX, ALFRED, ANITA, ANNE, BERNARD, BILL, CHARLES, CLAIRE, DAVID, ERIC, FRANS, GEORGE, HERMAN, JOE, MARIA, MAX, PAUL, PETER, PHILIP, RICHARD, ROBERT, SAM, SUSAN, TOM, BENJAMIN]
LISTE_NOM_STRING_PERSO = ["Alex", "Alfred", "Anita", "Anne", "Bernard", "Bill", "Charles", "Claire", "David", "Eric", "Frans", "George", "Herman", "Joe", "Maria", "Max", "Paul", "Peter", "Philip", "Richard", "Robert", "Sam", "Susan", "Tom", "Benjamin"]

dictionnaireEtatPerso = {
ALEX : True,
ALFRED : True,
ANITA : True,
ANNE : True,
BERNARD : True,
BILL : True,
CHARLES : True,
CLAIRE : True,
DAVID : True,
ERIC : True,
FRANS : True,
GEORGE : True,
HERMAN : True,
JOE : True,
MARIA : True,
MAX : True,
PAUL : True,
PETER : True,
PHILIP : True,
RICHARD : True,
ROBERT : True, 
SAM : True, 
SUSAN : True,
TOM : True,
BENJAMIN : True
}

QUESTION1_1 = "La pilosité de votre personnage est-elle noire ?"
QUESTION1_2 = "La pilosité de votre personnage est-elle brune ?"
QUESTION1_3 = "La pilosité de votre personnage est-elle rousse ?"
QUESTION1_4 = "La pilosité de votre personnage est-elle jaune ?"
QUESTION1_5 = "La pilosité de votre personnage est-elle blanche ?"

QUESTION2 = "Votre personnage est-il un homme ?:"
QUESTION3 = "Votre personnage a-t-il les yeux bruns ?:"
QUESTION4 = "Votre personnage porte-t-il un chapeau ?:"
QUESTION5 = "Votre personnage porte-t-il des lunettes ?:"
QUESTION6 = "Votre personnage a-t-il un petit nez ?:" 
QUESTION7 = "Votre personnage a-t-il une moustache ?:"
QUESTION8 = "Votre personnage est-t-il chauve ?:"

listeDeQuestion1 = [QUESTION1_1, QUESTION1_2, QUESTION1_3, QUESTION1_4, QUESTION1_5]

listeDeQuestion = [QUESTION2, QUESTION3, QUESTION4, QUESTION5, QUESTION6, QUESTION7, QUESTION8]

reponse1_1 = None
reponse1_2 = None
reponse1_3 = None
reponse1_4 = None
reponse1_5 = None

listeDeReponse1 = [reponse1_1, reponse1_2, reponse1_3, reponse1_4, reponse1_5]

reponse2 = None
reponse3 = None
reponse4 = None
reponse5 = None
reponse6 = None
reponse7 = None
reponse8 = None

print("Vous devez toujours répondre par oui (O) ou par non (N)")

### LES MODIFICATIONS NÉCESSAIRES SE FONT À PARTIR D'ICI ###
random.shuffle(listeDeQuestion)

while reponse1_1 == None:
    while reponse1_1 != "O" and reponse1_1 != "N":
        reponse1_1 = input(QUESTION1_1)
        reponse1_1 = reponse1_1.capitalize()  
        if reponse1_1 == "O":
            reponse1 = "N"   
            reponse1_2 = "N"
            reponse1_3 = "N"
            reponse1_4 = "N"
            reponse1_5 = "N"

while reponse1_2 == None:
    while reponse1_2 != "O" and reponse1_2 != "N":
        reponse1_2 = input(QUESTION1_2) 
        reponse1_2 =reponse1_2.capitalize()  
        if reponse1_2 == "O":
            reponse1 = "Br"  
            reponse1_3 = "N"
            reponse1_4 = "N"
            reponse1_5 = "N"

while reponse1_3 == None:
    while reponse1_3 != "O" and reponse1_3 != "N":
        reponse1_3 = input(QUESTION1_3) 
        reponse1_3 = reponse1_3.capitalize()  
        if reponse1_3 == "O":
            reponse1 = "R"  
            reponse1_4 = "N"
            reponse1_5 = "N"


while reponse1_4 == None:
    while reponse1_4 != "O" and reponse1_4 != "N":
        reponse1_4 = input(QUESTION1_4) 
        reponse1_4 = reponse1_4.capitalize()  
        if reponse1_4 == "O":
            reponse1 = "J"   
            reponse1_5 = "N"

while reponse1_5 == None:
    while reponse1_5 != "O" and reponse1_5 != "N":
        reponse1_5 = input(QUESTION1_5) 
        reponse1_5 = reponse1_5.capitalize()    
        if reponse1_5 == "O":
            reponse1 = "Bl" 

reponse2 = input(QUESTION2)
reponse2 = reponse2.capitalize()
if reponse2 == "O":
    reponse2 = "H"
else:
    reponse2 = "F"

if reponse2 == "F" and reponse1 == "J":
    reponse3 = "Bl"
    reponse4 = "N"
    reponse5 = "N"
    reponse6 = "P"
    reponse7 = "N"
    reponse8 = "N"
elif reponse2 == "F" and reponse1 == "Bl":
    reponse3 = "Br"
    reponse4 = "N"
    reponse5 = "N"
    reponse6 = "P"
    reponse7 = "N"
    reponse8 = "N" 
elif reponse2 == "H" and reponse1 == "Bl" and reponse3 == "Br":
    reponse4 = "N"
    reponse5 = "O"
    reponse6 = "P"
    reponse7 = "N"
    reponse8 = "N"
elif reponse2 == "H" and reponse1 == "J" and reponse3 == "Br" and reponse4 == "O":
    reponse5 = "N"
    reponse6 = "P"
    reponse7 = "N"
    reponse8 = "N"
elif reponse1 == "Bl" and reponse8 == "O" and reponse5 == "O":
    reponse3 = "Br"
    reponse4 = "N"
    reponse6 = "P"
    reponse7 = "N"
elif reponse1 == "R" and reponse2 == "F":
    reponse3 = "Br"
    reponse4 = "O"
    reponse5 = "O"
    reponse6 = "P"
    reponse7 = "N"
    reponse8 = "N"


while reponse3 == None:
    reponse3 = input(QUESTION3) 
    reponse3 = reponse3.capitalize()
    if reponse3 == "O":
        reponse3 = "Br"
    else:
        reponse3 = "Bl"

while reponse4 == None:
    reponse4 = input(QUESTION4) 
    reponse4 = reponse4.capitalize()    
    if reponse4 == "O":
        reponse4 = "N" 

while reponse5 == None:
    reponse5 = input(QUESTION5) 
    reponse5 = reponse5.capitalize()    
    if reponse5 == "O":
        reponse5 = "O" 
    else:
        reponse5 = "N"

while reponse6 == None: 
    reponse6 = input(QUESTION6) 
    reponse6 = reponse6.capitalize()
    if reponse6 == "O":
        reponse6 = "P"
    else:
        reponse6 = "G"

while reponse7 == None:
    reponse7 = input(QUESTION7) 
    reponse7 = reponse7.capitalize()

while reponse8 == None:
    reponse8 = input(QUESTION8) 
    reponse8 = reponse8.capitalize()

### AUCUNE MODIFICATION NÉCESSAIRE APRÈS CETTE LIGNE ###

listeDeReponse = tuple([reponse1, reponse2, reponse3, reponse4, reponse5, reponse6, reponse7, reponse8])
# print(listeDeReponse)

for i in range(len(LISTE_VALEUR_PERSO)): # Pour chaque élément [i] de la liste LISTE_VALEUR_PERSO
    for j in range(len(listeDeReponse)): # Pour chaque élément [j] de notre liste de réponse
        if LISTE_VALEUR_PERSO[i] != listeDeReponse: # Si la valeur dans la liste à la position [i] n'est pas égale à notre liste de réponse
            dictionnaireEtatPerso[LISTE_VALEUR_PERSO[i]] = False # Assigner la valeur False à la position [i] dans le dictionnaire de personnage

for k in range(len(LISTE_VALEUR_PERSO)): # Pour chaque élément [k] de la liste LISTE_VALEUR_PERSO
    if dictionnaireEtatPerso[LISTE_VALEUR_PERSO[k]] == True: # Si la valeur dans liste à la position [k] est vrai
        print("Le nom de votre personnage est-il " + LISTE_NOM_STRING_PERSO[k] + " ?") # Imprimer dans le terminal 
    else:

        sys.exit()

verification = None

while verification == None :
    while verification != "O" and verification !="N" :     
        verification = str(input("Confirmez avec O ou N :"))
        verification = verification.capitalize()

if verification == "O":
    print("Super, j'ai gagné !")
elif verification == "N":
     print("Vous êtes certain ? Avez-vous bien rempli les réponses ? J'ai toujours raison !")