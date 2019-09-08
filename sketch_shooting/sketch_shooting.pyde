import random

x = 200
y = 500
shipW = 30
shipH = 40
screenW = 400
screenH = 600
photons = []
photonSetting = {'w': 10, 'h': 10, 'speed': 10, 'color': color(0, 255, 255)}
enemies = []
enemySetting = {'w': 30, 'h': 30, 'life': 3,
                'generateInterval': 180, 'speed': 1, 'color': color(255, 0, 0)}
timer = 0


def setup():
    size(screenW, screenH)

def draw():
    global timer
    background(0)
    showShip()
    showPhotons()
    calcPhotonCollision()
    if timer % enemySetting['generateInterval'] == 0:
        addEnemy()
    showEnemies()
    timer += 1

def showShip():
    fill(255)
    noStroke()
    triangle(x, y, x + (shipW / 2), y + shipH, x - (shipW / 2), y + shipH)

def shootPhoton():
    global photons
    photon = {'x': x, 'y': y, 'hit': False}
    photons.append(photon)

def showPhotons():
    global photons
    fill(photonSetting['color'])
    for p in photons:
        ellipse(p['x'], p['y'], photonSetting['w'], photonSetting['h'])
        p['y'] -= photonSetting['speed']
    # remove photons if they are out of screen
    photons = [p for p in photons if p['y'] > 0 and p['hit'] == False]

def addEnemy():
    global enemies
    x = random.random() * width
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    enemy = {'x': x, 'y': 0, 'life': enemySetting[
        'life'], 'color': color(r, g, b)}
    enemies.append(enemy)

def showEnemies():
    global enemies
    w = enemySetting['w']
    h = enemySetting['h']
    for e in enemies:
        fill(e['color'])
        triangle(e['x'], e['y'], e['x'] + (w / 2),
                 e['y'] - h, e['x'] - (w / 2), e['y'] - h)
        e['y'] += enemySetting['speed']
    enemies = [e for e in enemies if e['y'] < height and e['life'] > 0]

def calcPhotonCollision():
    global photons, enemies
    ew = enemySetting['w']
    eh = enemySetting['h']
    pw = photonSetting['w']
    ph = photonSetting['h']
    for e in enemies:
        for p in photons:
            if p['x'] > e['x'] - ew / 2 and p['x'] < e['x'] + ew / 2 and p['y'] > e['y'] - eh and p['y'] < e['y']:
                e['life'] -= 1
                p['hit'] = True

def mouseClicked():
    shootPhoton()

def mouseMoved():
    global x, y
    x = mouseX
    y = mouseY

def keyPressed():
    if key == ' ':  # Space key
        shootPhoton()
