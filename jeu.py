#Jeu du Pierre Feuille Ciseaux en Python

#Import du module random
import random

#Fonction pour la victoire du joueur qui lui met un message de félicitation et lui propose de retenter sa chance
def victoireJoueur():
    print("Félicitation ! Vous avez gagné cette partie.")
    return reMatch()

#Fonction pour la victoire du robot qui met un message au joueur pour retenter sa chance
def victoireRobot():
    print("Quel dommage ! Vous avez perdu la partie, reessayer !")
    return reMatch()

#Fonction d'égalité qui propose au joueur de retenter sa chance
def egalite():
    print("Vous avez fait un match nul ! Re tenter votre chance")
    return reMatch()

#Fonction error qui affiche un message d'erreur
def error():
    print("Error ! L'objet choisie n'est pas jouable")
    return reMatch()

#Fonction permettant de proposer au joueur de relancer une partie ou non
def reMatch():
    reponse = input("Voulez-vous retenter votre chance ? ")
    if reponse == "non":
        print("Merci d'avoir jouer !")
    elif reponse == "oui":
        game()
    else :
        print("Je n'ai pas compris votre réponse.")
        reMatch()

#Fonction du jeu Pierre Feuille Ciseaux
def game():
    #Liste des objets disponnible jouable
    objetDisponnible=["Pierre", "Feuille", "Ciseaux"]
    #Le joueur choisie ici son objet qu'il souhaite jouer parmis la liste d'objet disponnible
    objetJoueur = str(input("Choisissez ce que vous voulez jouer : "))
    #Si le joueur choisi un objet autre que Pierre, Feuille ou Ciseaux un message d'erreur est renvoyé 
    if objetJoueur != "Pierre" and objetJoueur != "Feuille" and objetJoueur != "Ciseaux":
        return error()
    #Si le joueur choisi un objet dans la liste des objets disponnibles alors :
    else : 
        #on fait choisir au robot un objet aléatoirement parmis la liste
        objetRobot = objetDisponnible[random.randint(0,2)]
        print("Le Robot à choisie de faire :", objetRobot)
        #On compare ensuite le choix du robot à celui du joueur, si le joueur à un objet plus fort que le robot, on lui fait gagner la partie, et inversement
        if objetRobot == "Pierre" and objetJoueur == "Feuille" :
            return victoireJoueur()
        elif objetRobot == "Feuille" and objetJoueur == "Pierre" :
            return victoireRobot()
        elif objetRobot == "Feuille" and objetJoueur == "Ciseaux" :
            return victoireJoueur()
        elif objetRobot == "Ciseaux" and objetJoueur == "Feuille" :
            return victoireRobot()
        elif objetRobot == "Ciseaux" and objetJoueur == "Pierre" :
            return victoireJoueur()
        elif objetRobot == "Pierre" and objetJoueur == "Ciseaux" :
            return victoireRobot()
        #Si le joueur et le robot possèdent le même objet alors on fait une égalité 
        elif objetRobot == "Feuille" and objetJoueur == "Feuille" :
            return egalite()
        elif objetRobot == "Ciseaux" and objetJoueur == "Ciseaux" :
            return egalite()
        elif objetRobot == "Pierre" and objetJoueur == "Pierre" :
            return egalite()

game()