import pgzrun
WIDTH = 500
HEIGHT = 500
def draw():
    w = WIDTH
    h = HEIGHT-200
    screen.fill("white")
    for i in range(30):
        r1 = Rect(250,250,w,h)
        r1.center = (250,250)
        screen.draw.rect(r1,"red")
        w = w - 17
        h = h + 17
    
    
    
    #screen.draw.filled_rect(r1,"red")
pgzrun.go()