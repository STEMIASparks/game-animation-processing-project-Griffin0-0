mouseDown = False
onCanvas = False
run = True
Color = color(0, 0, 0)
brushsize = 50
brushtype = "circle"
sizeslider = 50
typeinput = " "
ontypeinput = False
rgbinput = ""
onrgbinput = False


def setup():
    global spacing
    size(1280, 720)
    frameRate(120)
    noStroke()
    background(255, 255, 255)

def mousePressed():
    global mouseDown, onCanvas
    mouseDown = True
    
def mouseReleased():
    global mouseDown
    mouseDown = False

def keyPressed():
    global brushtype, typeinput, ontypeinput, onrgbinput, rgbinput, Color
    if ontypeinput == True:
        if key == ENTER or key == RETURN:
            if typeinput == " square":
                brushtype = "square"
                typeinput = " "
            elif typeinput == " circle":
                brushtype = "circle"
                typeinput = " "
            else:
                typeinput = " "
        elif key == "" or key == DELETE:
            typeinput = " "
        elif len(typeinput) < 7:
            typeinput = (typeinput + key)
            
    if onrgbinput == True:
        if key == ENTER or key == RETURN:
            Color = color(unhex(rgbinput))
        elif key == "" or key == DELETE:
            rgbinput = ""
        elif len(rgbinput) <= 11:
            rgbinput = (rgbinput + key)
    
def draw():
    global mouseDown, onCanvas, Darkgreen, Green, Color, brushsize, brushtype, typeinput, ontypeinput, rgbinput, onrgbinput
    
    fill(100, 100, 100)
    rect(0, 600, 1280, 120)
    rect(0, 0, 200, 720)
    fill(255, 255, 255)
    textSize(15)
    fill(200, 200, 200)
    rect(20, 50, brushsize, 20)
    rect(20, 105, 150, 20)
    rect(20, 670, 165, 20)
    rect(20, 165, 150, 150)
    fill(0, 0, 0)
    text("Brush Size: " + str(brushsize), 25, 65)
    text("Brush Type: " + typeinput, 25, 120)
    textSize(20)
    text("Brush: " + brushtype, 25, 190)
    text("Brush Types: \n circle \n square", 25, 230)
    text("Custom Color (RGB)", 20, 650)
    textSize(15)
    text(rgbinput, 25, 685)
    
    fill(255, 255, 255)
    rect(1180, 620, 85, 85)
    textSize(30)
    fill(0, 0, 0)
    text("Clear", 1190, 670)
    
    fill(0, 255, 0)
    rect(250, 620, 35, 35)
    
    fill(34, 139, 34)
    rect(250, 670, 35, 35)
    
    fill(0, 255, 255)
    rect(300, 620, 35, 35)
    
    fill(0, 0, 255)
    rect(300, 670, 35, 35)
    
    fill(178, 102, 255)
    rect(350, 620, 35, 35)
    
    fill(100, 0, 200)
    rect(350, 670, 35, 35)
    
    fill(255, 0, 255)
    rect(400, 620, 35, 35)
    
    fill(255, 100, 255)
    rect(400, 670, 35, 35)
    
    fill(255, 0, 127)
    rect(450, 620, 35, 35)
    
    fill(255, 155, 204)
    rect(450, 670, 35, 35)
    
    fill(255, 0, 0)
    rect(500, 620, 35, 35)
    
    fill(255, 102, 102)
    rect(500, 670, 35, 35)
    
    fill(255, 128, 0)
    rect(550, 620, 35, 35)
    
    fill(255, 178, 102)
    rect(550, 670, 35, 35)
    
    fill(255, 255, 0)
    rect(600, 620, 35, 35)
    
    fill(255, 255, 103)
    rect(600, 670, 35, 35)
    
    fill(96, 96, 96)
    rect(650, 620, 35, 35)
    
    fill(192, 192, 192)
    rect(650, 670, 35, 35)
    
    fill(0, 0, 0)
    rect(700, 620, 35, 35)
    
    fill(255, 255, 255)
    rect(700, 670, 35, 35)
    
    if mouseDown == True and mouseX > 20 and mouseX <= 170 and mouseY > 50 and mouseY < 70:
        brushsize = (mouseX - 20)
        
    if mouseX >= 20 and mouseY >= 105 and mouseX <= 170 and mouseY <= 125:
        ontypeinput = True
    elif mouseX >= 20 and mouseY >= 670 and mouseX <= 185 and mouseY <= 690:
        onrgbinput = True
    else:
        ontypeinput = False
        onrgbinput = False
    
    if mouseDown == True and onCanvas == True:
        fill(Color)
        if brushtype == "circle":
            circle(mouseX, mouseY, brushsize)
        if brushtype == "square":
            rect(mouseX - (brushsize/2), mouseY - (brushsize/2), brushsize, brushsize)
        
    if mouseY < 600 and mouseX > 200:
        onCanvas = True
    else:
        onCanvas = False
        
    if mouseDown == True:
        if mouseY >= 620 and mouseY <= 655 and mouseX >= 250 and mouseX <= 735:
            if mouseX >= 250 and mouseX <= 285:
                Color = color(0, 255, 0)
            if mouseX >= 300 and mouseX <= 335:
                Color = color(0, 255, 255)
            if mouseX >= 350 and mouseX <= 385:
                Color = color(178, 102, 255)
            if mouseX >= 400 and mouseX <= 435:
                Color = color(255, 0, 255)
            if mouseX >= 450 and mouseX <= 485:
                Color = color(255, 0, 127)
            if mouseX >= 500 and mouseX <= 535:
                Color = color(255, 0, 0)
            if mouseX >= 550 and mouseX <= 585:
                Color = color(255, 128, 0)
            if mouseX >= 600 and mouseX <= 635:
                Color = color(255, 255, 0)
            if mouseX >= 650 and mouseX <= 685:
                Color = color(96, 96, 96)
            if mouseX >= 700 and mouseX <= 735:
                Color = color(0, 0, 0)
        if mouseY >= 670 and mouseY <= 705 and mouseX >= 250 and mouseX <= 735:
            if mouseX >= 250 and mouseX <= 285:
                Color = color(34, 139, 34)
            if mouseX >= 300 and mouseX <= 335:
                Color = color(0, 0, 255)
            if mouseX >= 350 and mouseX <= 385:
                Color = color(100, 0, 200)
            if mouseX >= 400 and mouseX <= 435:
                Color = color(255, 100, 255)
            if mouseX >= 450 and mouseX <= 485:
                Color = color(255, 155, 204)
            if mouseX >= 500 and mouseX <= 535:
                Color = color(255, 102, 102)
            if mouseX >= 550 and mouseX <= 585:
                Color = color(255, 178, 102)
            if mouseX >= 600 and mouseX <= 635:
                Color = color(255, 255, 103)
            if mouseX >= 650 and mouseX <= 685:
                Color = color(192, 192, 192)
            if mouseX >= 700 and mouseX <= 735:
                Color = color(255, 255, 255)
                
        if mouseX >= 1180 and mouseX <= 1265 and mouseY >= 620 and mouseY <= 705:
            fill(255, 255, 255)
            rect(200, 0, 1080, 600)
