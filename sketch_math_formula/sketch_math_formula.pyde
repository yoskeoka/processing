w = 800
h = 800
size(800, 800)

background(255)

# グラフの線
stroke("#0000ff")

strokeWeight(1)
line(0,h/2,w,h/2) # x軸
line(w/2,0,w/2,h) # y軸

stroke("#000000")

def y(x):
    # return 100.0*sin(x/20.0/PI)
    
    # 円
    r = 200
    return sqrt(r*r - x*x)
    

for x in range(-w/2,w/2):
    ellipse(x+w/2,-y(x)+h/2, 1,1)
    ellipse(-x+w/2,y(x)+h/2, 1,1) # 円のとき用

