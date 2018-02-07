import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain


def joue():
    jeu = game.initialiseJeu()
    while(not game.finJeu(jeu)):
        game.affiche(jeu)
        c=game.saisieCoup(game.getCopieJeu(jeu))
        jeu=game.joueCoup(jeu,c)
    g=game.getGagnant(jeu)
    return g
    
Victoires=[0,0,0]
for i in range (50):
    g=joue()
    Victoires[g]+=1
print(str(Victoires))
j=game.joueur2
game.joueur2=game.joueur1
game.joueur1=j
for i in range (50):
    g=joue()
    if g==1:
        g=2
    if g==2:
        g=1
    Victoires[g]+=1