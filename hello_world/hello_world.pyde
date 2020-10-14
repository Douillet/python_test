ballx = 0
bally = 0
ballspeedx = 5
ballspeedy = 2
ballradius = 7.5

racketx = 0
rackety = 0
sizeracketx = 50
sizerackety = 10

#dièse pour faire des commentaires
def setup():
    global ballx, bally, sizeracketx, sizerackety, racketx, rackety
    
    size(400, 400)
    clear()
    frameRate(60)
    ballx= width/2
    bally= height/2
    
    #racketx = mouseX - sizeracketx/2
    #rackety = height - 20
    
def draw():
    clear()
    drawracket()
    drawball()
    
def drawracket():
    global sizeracketx, sizerackety, racketx, rackety
    fill(255)
    racketx = mouseX - sizeracketx/2
    rect(racketx, rackety, sizeracketx, sizerackety)
    #code pour la raquette, height donne la variable de la hauteur de l'écran
    
def drawball():
    global ballx, bally, ballspeedx, ballspeedy, ballradius, sizeracketx, sizerackety, racketx, rackety
   
    #ballx = ballx + ballspeedx
    #bally = bally + ballspeedy <=> bally += ballspeedy
    ballx += ballspeedx
    bally += ballspeedy
    racketx = mouseX - sizeracketx/2
    rackety = height -20
    
    #droite puis #gauche
    if(ballx > width):
        ballspeedx *= -1
        ballx = width - ballradius
    elif(ballx < 0):
        ballspeedx *= -1
        ballx = ballradius 
    
    #haut puis #bas
    if(bally < 0):
        ballspeedy *= -1
        bally = ballradius
    elif(bally > height):
        ballspeedy *= -1
        bally = height - ballradius
        sizeracketx += -5 #cette condition réduit la taille de la raquette à caue fois que la balle touche le bord bas de la fenêtre
        print"Attention! La raquette diminue de taille!"
    #hitbox de la racket
    if(rackety + sizerackety > bally + ballradius > rackety and ballspeedy > 0):
        if(racketx < ballx < racketx + sizeracketx):
            ballspeedy *= -1
            bally = rackety - ballradius        
    #if(rackety < bally < rackety + sizerackety and ballx - ballradius = racketx + sizeracketx):
        #ballspeedx *= -1
    
    fill(255, 0, 190)
    circle(ballx, bally , ballradius * 2)
    
