Printemps = "printemps"
Été = "été"
Automne = "automne"
Hiver = "hiver"

print("Quel est ta saison préféré ?")
reponse = input("réponse : ")

rep_norm = reponse.strip().lower()

if rep_norm == Printemps:
    print("Tu as souvent hâte à l'été!")
elif rep_norm == Été:
    print("Tu aimes bien être en vacances")
elif rep_norm == Automne:
    print("Tu aimes bien les couleurs chaudes et les feuilles qui tombent")
elif rep_norm == Hiver:
    print("Tu es bizare, tu aimes le froid")
else:  
    input("Tu as entré une saison qui n'existe pas, appuie sur entrée pour quitter")