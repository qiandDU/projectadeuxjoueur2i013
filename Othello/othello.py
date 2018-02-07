import sys
sys.path.append("..")
import game
sys.path.append("./Joueurs")
import joueur_humain

def init():
    #plateau : List[List[int]]
    
    plateau = [[0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,1,2,0,0,0],
               [0,0,0,2,1,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]
    #joueur j : int 
    j = 1
    #l1 : List[coup] La liste des coups possibles pour le joueur a qui c'est le tour de jouer
    #l2 : List[coup] La liste des coups joues jusqu'a present dans le jeu
    l1 = None
    l2 = []
    #score = Pair[nat nat]
    score = [0,0]
    #jeu: N-UPLET[plateau nat List[coup] List[coup] Pair[nat nat]]
    jeu = [plateau,j,l1,l2,score]
    return jeu
    
    
def joueCoup(jeu,coup):
    
    

    


def getCoupValides(jeu):
    c=coups(jeu)
    return [x for x in c if len(encardement(jeu,x,False))>0]
    
def coups(jeu):
    c = []
    a = game.getJoueur(jeu)
    a = a%1+1
    for i in range (8):
        for j in range(8):
            if(jeu[0][i][j]==0):
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        if( (i+k)>=0 and (i+k)<8 and (j+l)>=0 and (j+l)<8 ):
                            if(jeu[0][i+k][i+l]==a):
                                 c.append([i,j])
    return c
    
def encardement(jeu,c,tous = True):
    set = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i==0 and j==0:
                continue
            if checkDirection(jeu,c,[i,j]):
                set.apprend([i,j])
                if not tous:
                    return set
                    
                    
def checkDirection(jeu,c,d):
    j = jeu[1]
    i = 0
    while True:
        c = [c[0]+d[0],c[i]+d[1]]
        if c[0]<0 or c[0]>=8 or c[i]<0 or c[i]>=8:
            return False
        if jeu[0][c[0]][c[1]]==0:
            return False
            if jeu[0][c[0],c[1]]==j:
                return i>1
                
    

