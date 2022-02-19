#afficher l'imformation de la personne
def demande_info(nom, age):
    print("votre nom est "+nom+ ", vous avez "+str(age)+" ans")
    print("l'annee prochaine vous "+str(age+1)+" ans")
    
    if age < 10:
        print("vous etes enfant")
    elif age == 17:
        print("vous etes presque majeur")
    elif age == 18:
        print("vous etes tout juste majeur: felicitaton")
    elif age > 60:
        print("vous etes senior")
    elif age < 18:
        print("vous etes mineur")
    else:
        print("vous etes majeur")

def demande_nom():
    nom = ""
    while nom =="":
            nom = input("quel est votre nom ? ")
    return nom

def demande_age():
    age_n = 0
    while age_n ==0:
        age_r = input("quel est votre age ? ")
        try:
            age_n = int(age_r)
        except:
            print("erreur: entrer un nombre correct")
    return age_n
#info1

nom1 = demande_nom()
age1= demande_age()
demande_info(nom1, age1)
#info2

nom2 = demande_nom()
age2 = demande_age()
demande_info(nom2, age2)