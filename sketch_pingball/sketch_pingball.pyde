# This source code reference is below.
# https://qiita.com/sawamur@github/items/204b93638a4f117c9cc2

# screen
screenW = 400
screenH = 600

# block
blockXCount = 3
blockYCount = 1
blockW = screenW/blockXCount
blockH = 20
blockMargin = 0

blocks = []

# ball properties
x = 300
y = 150
ballR = 30
speedX = 2
speedY = 2

# bar properties
barW = 150
barH = 30
barX = screenW / 2 - barW/2
barY = screenH - 50


def setup():
    size(screenW, screenH)
    createBlocks()
    
def draw():
    background(0)
    # bar
    rect(barX, barY, barW, barH)

    # block
    checkBallHit()
    showBlocks()

    
    # ball
    global x,y, speedX, speedY

    fill(255)
    stroke("#ff0000")
    x+=speedX
    y+=speedY
    ellipse(x, y, ballR, ballR)
    
    if x > screenW or x < 0:
        speedX = speedX * -1
    if y > screenH or y < 0:
        speedY = speedY * -1
    if x > barX and x < barX+barW and y > barY and y < barY+barH:
        speedY = speedY * -1
    
    checkEnd()
    

def createBlocks():
    global blocks
    for i in range(0, blockXCount*blockYCount):
        blockX = (i % blockXCount) * screenW/blockXCount
        blockY = int(i / blockXCount) * (blockH+blockMargin)
        block = {'x':blockX, 'y':blockY, 'ok':True}
        blocks.append(block)
    
def showBlocks():
    fill("#0000ff")
    stroke("#ffffff")
    for block in blocks:
        if block['ok']:
            rect(block['x'], block['y'], blockW, blockH) 

def checkBallHit():
    global speedY
    for block in blocks:
        if block['ok'] and x > block['x'] and x < block['x']+blockW and y > block['y'] and y < block['y'] + blockH:
            block['ok'] = False
            speedY = speedY * -1

def checkEnd():
    if y > screenH:
        textSize(30)
        text("GAME OVER", screenW/2-100, screenH/2)
        noLoop()
    for block in blocks:
        if block['ok']:
            return
    
    textSize(40)
    text("CLEAR!!", screenW/2-100, screenH/2)
    
    redraw()
    noLoop()

def keyPressed():
    global barX, barY
    if keyCode == RIGHT:
        barX += 5
    elif keyCode == LEFT:
        barX -= 5
    if keyCode == UP:
        barY -= 5
    elif keyCode == DOWN:
        barY += 10
