# plateau: List[List[nat]]
# liste de listes (lignes du plateau) d'entiers correspondant aux contenus des cases du plateau de jeu

# coup: Pair[nat nat]
# Numero de ligne et numero de colonne de la case correspondante a un coup d'un joueur

# Jeu
# jeu:N-UPLET[plateau nat List[coup] List[coup] Pair[nat nat]]
# Structure de jeu comportant :
#           - le plateau de jeu
#           - Le joueur a qui c'est le tour de jouer (1 ou 2)
#           - La liste des coups possibles pour le joueur a qui c'est le tour de jouer
#           - La liste des coups joues jusqu'a present dans le jeu
#           - Une paire de scores correspondant au score du joueur 1 et du score du joueur 2

game=None #Contient le module du jeu specifique: awele ou othello
joueur1=None #Contient le module du joueur 1
joueur2=None #Contient le module du joueur 2


#Fonctions minimales 

def getCopieJeu(jeu):
    """ jeu->jeu
        Retourne une copie du jeu passe en parametre
        Quand on copie un jeu on en calcule forcement les coups valides avant
    """
    l2 = getCoupsValides(jeu)
    copie_jeu = jeu
    copie_jeu[2]=l2
    return copie_jeu

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    if jeu[4][0]>24 or jeu[4][1]>24 :
        return True 
    else :
        return False

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
        On suppose que la fonction n'est appelee que si il y a au moins un coup valide possible
        et qu'elle retourne obligatoirement un coup valide
    """
    



def joueCoup(jeu,coup):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
        Met tous les champs de jeu a jour (sauf coups valides qui est fixee a None)
        """
        
        
        
    game.joueCoup(jeu,coup)
    
    
    
def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    game.init()

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    if jeu[4][0]>24 :
        return 1
    elif jeu[4][1]>24 :
        return 2
    else :
        return 0

def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """
    i=0
    print 'Coup joue = '+jeu[3][len(jeu[3])-1]+'\n'
    print jeu[3][len(jeu[3])-1]+'\n'
    print 'Scores ='+jeu[4][0]+', '+jeu[4][1]+'\n'
    print 'Plateau : \n'
    for i in len(jeu[0]) :
        for j in len(jeu[0][0]) :
            if i==0 and j==0 :
                print '     |'
            elif i==0 :
                print '  '+j-1+'  |'
            elif j==0 :
                print '  '+i-1+'  |'
            else :
                print ' '+jeu[0][i-1][j-1]+' |'
        print '\n'
        print '-------------------------------------------------------\n'
    print 'Joueur' +jeu[1]+',a vous de jouer'
    
                
    
    
# Fonctions utiles

def getPlateau(jeu):
    """ jeu  -> plateau
        Retourne le plateau du jeu passe en parametre
    """
    return jeu[0]

def getCoupsJoues(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups joues dans le jeu passe en parametre
    """
    return jeu[3]


def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met a jour la liste des coups valides
    """
    if jeu[2] is None :
        jeu[2] = game.getCoupsValide(jeu)
        
    return jeu[2]


def getScores(jeu):
    """ jeu  -> Pair[nat nat]
        Retourne les scores du jeu passe en parametre
    """
    return jeu[4]

def getJoueur(jeu):
    """ jeu  -> nat
        Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    return jeu[1]



def changeJoueur(jeu):
    """ jeu  -> void
        Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre (1 ou 2)
    """
    if jeu[1]==1:
        return 2
    if jeu[1]==2:
        return 1

def getScore(jeu,joueur):
    """ jeu*nat->int
        Retourne le score du joueur
        Hypothese: le joueur est 1 ou 2
    """
    return jeu[4][joueur-1]

def getCaseVal(jeu, ligne, colonne):
    """ jeu*nat*nat -> nat
        Retourne le contenu de la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    return jeu[0][ligne][colonne]
    
def setCaseVal(jeu,ligne,colonne,nbGraine):
    """ jeu*nat*natunat -> void
        Ecrit le nombre de graines dans la case ligne,colonnne du jeu
    """
    jeu[0][ligne][colonne]=nbGraine


def addCoupJoues(jeu,coup):
    
    jeu[3].append(coup)


