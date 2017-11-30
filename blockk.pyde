global gseq
global px, py, pw, ph
px = 200
py = 420
pw = 40
ph = 20
global bx, by, spdx, spdy
global bw, bh
bw=7
bh=7
global phit
phit = 0
global blw, blh
blw = 78
blh = 30
global blf
#int[] blf = new int[25] wo python de kakiktai
blf = new blf[25]

def setup():
    size(400, 500)
    noStroke()
    colorMode(HSB, 100, 100, 100)
    gameInit()

def draw():
    global gseq
    gseq = 1
    background(0)
    if gseq == 0:
        gameTitle()
    elif gseq ==1:
        gamePlay()
    else:
        gameOver()
        
def gameInit():
    global gseq, bx, by, spdx, spdy, phit
    gseq = 0
    bx = 100
    by = 250
    spdx = 2
    spdy = 2
    phit = 0
    for i in range (25):
        blf[i] = 1
    
def gameTitle():
    global gseq
    gseq = 1

def gamePlay():
    playerMove()
    playerDisp()
    ballMove()
    ballDisp()
    blockDisp()

def gameOver():
    textSize(50)

def playerDisp():
    global px, py, pw, ph
    fill(0,0,100)
    rect(px, py, pw, ph, 5)

def playerMove():
    global px, py, pw, ph
    px = mouseX
    if ((px + pw) > width):
        px = width - pw

def ballDisp():
    global bx, by, bw, bh
    imageMode(CENTER)
    fill(0, 100, 100)
    rect(bx, by, bw, bh)
    imageMode(CORNER)

def ballMove():
    global bx, by, spdx, spdy, px, py, ph, pw, phit
    bx += spdx
    by += spdy
    if (by > height):
        spdy = - spdy
    if (by < 0):
        spdy = - spdy
    if ((bx < 0) or (bx > width)):
        spdx = -spdx
    if ((phit == 0) and (px < bx) and (px+pw > bx) and (py < by) and (py+ph > by)):
            spdy = -spdy
            phit = 1
    if (by < py - 30):
        phit = 0

def blockDisp():
    for i in range(25):
        if(blf[i] == 1):
            fill((i/5)*15, 100, 100)
            xx = (i%5)*(blw+2)
            yy = 50 + (i/5)* (blh+2)
            blockHitCheck(i, xx, yy)
            if (blf[i] == 1):
                rect(xx, yy, blw, blh, 2)

def blockHitCheck(ii, xx, yy):
    if(!((xx < bx) and(xx + blw > bx) and (yy < by) and(yy+blh > by))):
        return
    blf[ii] = 0
            