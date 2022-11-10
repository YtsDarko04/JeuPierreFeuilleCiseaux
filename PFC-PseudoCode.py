#Début 

#JEU PFC
#On admet que la fonction "random" existe et qu'elle permet de récupérer un chiffre aléatoirement
#On admet que la fonction "input" existe et qu'elle permet de récupérer un élément entrée par le joueur
#On crée une fonction "victoireJoueur",  affiche ("Félicitation ! Vous avez gagné cette partie."), retourner "reMatch"
#On crée une fonction "victoireRobot",  affiche ("Quel dommage ! Vous avez perdu la partie, reessayer !"), retourner "reMatch"
#On crée une fonction "egalite",  affiche ("Vous avez fait un match nul ! Re tenter votre chance"), retourner "reMatch"
#On crée une fonction "error",  affiche ("Error ! L'objet choisie n'est pas jouable"), retourner "reMatch"
#On crée une fonction "reMatch" qui utilise la fonction input("Voulez-vous retenter votre chance ? ") dans une variable réponse, 
    #si la réponse est égale à "oui" alors on relance la partie en éxécutant la fonction "game", 
    #si la réponse est "non" on arrête la partie et on affiche "Merci d'avoir jouer !", 
    #sinon afficher ("Je n'ai pas compris votre réponse."), on retourner "reMatch"
#On crée la fonction "game", on crée un tableau "objetDisponnible" comprennant 3 objets (Pierre, Feuille et Ciseaux), on crée une variable "objetJoueur" utilisant la fonction input pour récupérer ce que joue le joueur
    #si "objetJoueur" n'appartient pas au tableau (donc qu'il est différent de Pierre, Feuille et Ciseaux) alors on retourne la fonction 'error", si "objetJoueur" figure bien parmis la liste alors 
        #on crée une variable "objetRobot" qui prends un objet aléatoirement grace à la fonction random dans le tableau "objetDisponnible", on affiche ensuite la variable "objetRobot" avec un message
        #on compare ensuite le choix du robot à celui du joueur, si "objetRobot" est égal à "Pierre" et que "objetJoueur" est égal à "Feuille" alors on retourne victoireJoueur
        #si "objetRobot" est égal à "Feuille" et que "objetJoueur" est égal à "Ciseaux" 
            #alors on retourne victoireJoueur,
        #si "objetRobot" est égal à "Ciseaux" et que "objetJoueur" est égal à "Pierre" 
            #alors on retourne victoireJoueur,
        #si "objetRobot" est égal à "Pierre" et que "objetJoueur" est égal à "Ciseaux" 
            #alors on retourne victoireRobot,
        #si "objetRobot" est égal à "Ciseaux" et que "objetJoueur" est égal à "Feuille" 
            #alors on retourne victoireRobot,
        #si "objetRobot" est égal à "Feuille" et que "objetJoueur" est égal à "Pierre" 
            #alors on retourne victoireRobot,
        #si "objetRobot" est égal à "Pierre" et que "objetJoueur" est égal à "Pierre" 
            #alors on retourne egalite,
        #si "objetRobot" est égal à "Feuille" et que "objetJoueur" est égal à "Feuille" 
            #alors on retourne egalite,
        #si "objetRobot" est égal à "Ciseaux" et que "objetJoueur" est égal à "Ciseaux" 
            #alors on retourne egalite
#executer "game"
#Fin 