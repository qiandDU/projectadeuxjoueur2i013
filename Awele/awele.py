import sys
sys.path.append("..")
import game
sys.path.append("./Joueurs")

def init():
    #plateau : List[List[int]]
    plateau = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
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
    v=game.getCaseVal(jeu,coup[0],coup[1])
    game.setCaseVal(jeu,coup[0],coup[1],0)
    distribue(jeu,coup,v)
    game.addCoupJoues(jeu,coup)
    jeu[2]=None
    game.changeJoueur(jeu)
    
def distribue(jeu,coup,v):
    case= coup
    while(v>0):
        coup=nextCase(jeu,coup)
        if(coup==case):
            continue
        game.setCaseVal(jeu,coup[0],coup[1],game.getCaseVal(jeu,coup)+1)
        v=v-1
    
        
def nextCase(jeu,coup):
    nxtCase=coup
    if coup[0]==0:
        if coup[1]==0:
            nxtCase[0]=coup[0]+1
        else :
            nxtCase[1]=coup[1]-1
    if coup[0]==1:
        if coup[1]==5:
            nxtCase[0]=coup[0]-1
        else :
            nxtCase[1]=coup[1]+1
    return nxtCase

def getCoupValides(jeu):
    def coupValide(jeu,coup,checknourrit):
        v=game.getCaseVal(jeu,coup[0],coup[1])
        if v==0:
            return False
        if checknourrit:
            if coup[0]==0:
                return v>coup[1]
            else:
                return v>5-coup[1]
        return True
    j=game.getJoueur(jeu)
    a=estaffame(jeu,j%2+1)
    return [[j-1,c]for c in range(6) if coupValide(jeu,[j-1,c],a)]

def estaffame(jeu,joueur) :
    testjeu = game.getCopieJeu(jeu)
    if joueur==1:
        for i in range (6):
            coup = [1,i]
            game.joueCoup(testjeu,coup)
            if ((game.getCaseVal(testjeu,0,i)!=2) and (game.getCaseVal(testjeu,0,i)!=3)):
                return False
        return True
    if joueur==2:
        for i in range (6):
            coup = [0,i]
            game.joueCoup(testjeu,coup)
            if ((game.getCaseVal(testjeu,1,i)!=2) and (game.getCaseVal(testjeu,1,i)!=3)):
                return False
        return True
    