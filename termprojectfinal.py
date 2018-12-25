'''
Maitreyee Deshpande
December 8 2016
Term Project 15-112

Citations: 
I used this framework from the mode demo from cs.cmu.edu/~112
I used the animation framework from cs.cmu.edu/~112
'''


from tkinter import *

####################################
# init
####################################

def init(data):
    # initial mode
    data.mode = "splashScreen"
    
    # new colors
    data.peachtan = "#%02x%02x%02x" % (213, 181, 181)
    data.darkgray = "#%02x%02x%02x" % (96, 96, 96)
    data.lightblack = "#%02x%02x%02x" % (96, 96, 96)
    data.cream = "#%02x%02x%02x" % (233, 228, 228)
    data.gold = "#%02x%02x%02x" % (212, 175, 55)
    data.lightgray = "#%02x%02x%02x" % (176, 170, 170)
    data.lavender = "#%02x%02x%02x" % (194, 186, 219)
    data.lightbrown = "#%02x%02x%02x" % (154, 118, 90)

    #stores the rooms
    data.rectangles = [] 
    
    #used for modes
    data.toggleCreate = False
    data.toggleMove = False 
    
    data.furnitureCreate = False
    data.furnitureMove = False
    
    data.currentRoom = None
    
    
####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "splashScreen"): splashScreenMousePressed(event, data)
    elif (data.mode == "createHouse"):   createHouseMousePressed(event, data)
    elif (data.mode == "moveFurniture"): moveFurnitureMousePressed(event, data)
    elif (data.mode == "helpScreen"): helpScreenMousePressed(event, data)
    elif (data.mode == "doneScreen"): doneScreenMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "splashScreen"): splashScreenKeyPressed(event, data)
    elif (data.mode == "createHouse"):   createHouseKeyPressed(event, data)
    elif (data.mode == "moveFurniture"): moveFurnitureKeyPressed(event, data)
    elif (data.mode == "helpScreen"): helpScreenKeyPressed(event, data)
    elif (data.mode == "doneScreen"): doneScreenKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "splashScreen"): splashScreenTimerFired(data)
    elif (data.mode == "createHouse"):   createHouseTimerFired(data)
    elif (data.mode == "moveFurniture"): moveFurnitureTimerFired(data)
    elif (data.mode == "helpScreen"): helpScreenTimerFired(data)
    elif (data.mode == "doneScreen"): doneScreenTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"): splashScreenRedrawAll(canvas, data)
    elif (data.mode == "createHouse"):   createHouseRedrawAll(canvas, data)
    elif (data.mode == "moveFurniture"): moveFurnitureRedrawAll(canvas, data)
    elif (data.mode == "helpScreen"): helpScreenRedrawAll(canvas, data)
    elif (data.mode == "doneScreen"): doneScreenRedrawAll(canvas, data)



####################################
# splashScreen mode
####################################

def splashScreenMousePressed(event, data):
    
    #"next" pressed
    if (event.x > data.width/2-15 and event.x < data.width/2+15 and 
        event.y > data.height/2-15 and event.y < data.height/2+15):
        data.mode = "createHouse"
        
    #"help" pressed
    elif (event.x < data.width/2+20 and event.y < data.height/2+80 and 
            event.x > data.width/2-20 and event.y > data.height/2+60):
        data.mode = "helpScreen"
        
        
def splashScreenKeyPressed(event, data):
    pass
    

def splashScreenTimerFired(data):
    pass
    
    
def drawTitleScreen(canvas, data):
    #Background
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.peachtan, 
                            width = 0)
    
    #Diagonal lines
    for i in range(0, data.width+20, 20):
        for j in range(0, data.height+20, 20):
            canvas.create_line(i-10, j-10, i+10, j+10, width = 1, 
                                fill = data.lightblack)
    for i in range(0, data.width+20, 20):
        for j in range(0, data.height+20, 20):
            canvas.create_line(i+10, j-10, i-10, j+10, width = 1, 
                                fill = data.lightblack)
            
    #text- title
    title = "InDesigner" 
    canvas.create_text(data.width/2, data.height/8, text = title, 
                        font = "Helvetica 40 bold", fill = data.cream)
    
    #border
    canvas.create_rectangle(data.width/2-120, data.height/8-30,data.width/2+120, 
                            data.height/8+30, width = 2, outline = data.cream)
    canvas.create_rectangle(data.width/2-130, data.height/8-40,data.width/2+130, 
                            data.height/8+40, width = 2, outline = data.cream)
    
    #text- start
    start =  "-Enter your design studio by clicking on the cross-"
    canvas.create_text(data.width/2, data.height-40, text = start, 
                        fill = data.cream, font = "sansserif 18")
    
    #help 
    canvas.create_rectangle(data.width/2-20, data.height/2+60, data.width/2+20, 
                            data.height/2+80, fill = data.cream, outline = 
                                data.lightblack)
    canvas.create_text(data.width/2, data.height/2+70, text = "help", 
                        font = "sansserif 14", fill = data.lightblack)
    
    #cross
        #vertical line
    canvas.create_line(data.width/2, data.height/2-15, data.width/2, 
                        data.height/2+15, width = 3, fill = data.cream)
        #horizontal line
    canvas.create_line(data.width/2-15, data.height/2, data.width/2+15,
                        data.height/2, width = 3, fill = data.cream)
    
    #additional graphics
    canvas.create_rectangle(5, 5, data.width, data.height, width = 2, 
                            outline = data.darkgray)

def splashScreenRedrawAll(canvas, data):
    drawTitleScreen(canvas, data)
    
    
    
####################################
# create house mode
####################################
class Rectangle(object):
    
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        self.width = 100
        self.height = 50
        self.clicked = False 
        self.pieces = []
        
        
        
    def draw(self, canvas):
        canvas.create_rectangle(250-self.width, 250-self.height, 
                                250+self.width, 250+self.height,width =2)
        
    def containsPoint(self, x, y):
        if (x > self.x - self.width and x < self.x + self.width and 
            y > self.y - self.height and y < self.y + self.height): return True 

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

def createHouseMousePressed(event, data):
    
    if data.toggleCreate == True:
    
        data.toggleMove = False
        data.rectangles.append(Rectangle(event.x, event.y))
        
        
    else:
        data.toggleMove = True 
        data.toggleCreate = False
        currentIndex = 0
        for i in range(len(data.rectangles)):
            room = data.rectangles[i]
            if room.containsPoint(event.x, event.y):
                for room in data.rectangles:
                    if room.clicked==True:
                        room.clicked = False
                data.rectangles[i].clicked = True
                currentIndex = i
                data.currentRoom = data.rectangles[i]
                
        for j in range(len(data.rectangles)):
            if j == currentIndex: continue
            else: data.rectangles[j].clicked = False 
        
    # clicked on a toggle button
    
        #create mode
    if (event.x < data.width*.75+30 and event.x > data.width*.75-30 and 
        event.y < data.height-20 and event.y > data.height-60):
        
        data.toggleCreate = False
        data.toggleMove = True
    
    elif (event.x < data.width/4+30 and event.x > data.width/4-30 and 
            event.y < data.height-20 and event.y > data.height-60):
        
        
        data.toggleMove = False
        data.toggleCreate = True
    #back
    elif (event.x < 60 and event.y < 30 and event.x > 20 and event.y > 10):
        data.mode = "splashScreen"
    
    #next
    elif (event.x < data.width-20 and event.y < 30 and 
            event.x > data.width-60 and event.y > 10):
        data.mode = "moveFurniture"
        


        
def createHouseKeyPressed(event, data):
    
    for room in reversed(data.rectangles):
        if room.clicked: 
            if event.keysym == "Up": room.y -= 5
            elif event.keysym == "Down": room.y +=5
            elif event.keysym == "Left": room.x -= 5
            elif event.keysym == "Right": room.x += 5
            elif event.char == 'd': 
                room.width += 5
                
            elif event.char == 'a':
                room.width -= 5 
            
            elif event.char == 'w':
                room.height += 5
            
            elif event.char == 's':
                room.height -= 5
                 

def createHouseTimerFired(data):
    pass
    


def createHouseRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.peachtan)
    canvas.create_rectangle(100, 10, 400, 50, width = 2, fill = data.cream)
    canvas.create_text(250, 30, text = "Build Your Rooms", 
                        font = "sansserif 18 bold")
    canvas.create_rectangle(30, 60, 420, 400, width = 3, 
                            outline = data.lightblack)
    
    #toggle buttons
    #create
    canvas.create_rectangle(data.width/4-30, data.height-60, data.width/4+30, 
                            data.height-20, width = 2, fill = data.cream)
    canvas.create_text(data.width*.25, data.height-40, text = "create", 
                        font = "Sansserif 14 bold")
    #move
    canvas.create_rectangle(data.width*.75-30, data.height-60, 
                            data.width*.75+30, data.height-20, width = 2, 
                            fill = data.cream)
    canvas.create_text(data.width*.75, data.height-40, text = "move", 
                        font = "Sansserif 14 bold")
    
    for i in range (0, len(data.rectangles)):
        rect = data.rectangles[i]
        rect.draw(canvas)
    
    #back
    canvas.create_polygon(20, 10, 60, 10, 60, 30, 20, 30, 10, 20, 
                            fill = data.cream, outline = "black", width = 2)
    canvas.create_text(40, 20, text = "back", font = "sansserif 10 bold")
    
    #next
    canvas.create_polygon(data.width-60, 10, data.width-20, 10, data.width-10, 
                            20, data.width-20, 30, data.width-60, 30, 
                            fill = data.cream, outline = "black", width = 2)
    canvas.create_text(data.width-40, 20, text = "next", 
                        font = "sansserif 10 bold")
    
    #increase height 
    canvas.create_rectangle(data.width-70, 150, data.width-10, 190, 
                            fill = data.cream, width = 2)
    canvas.create_line(data.width-30, 155, data.width-30, 169, 
                        arrow = FIRST, width = 2)
    canvas.create_line(data.width-30, 171, data.width-30, 185, 
                        arrow = LAST, width = 2)
    canvas.create_text(data.width-60, 170, text = "w", 
                        font = "sansserif 14 bold")
    
    
    #decrease height
    canvas.create_rectangle(data.width-70, 200, data.width-10, 240, 
                            fill = data.cream, width = 2)
    canvas.create_line(data.width-30, 205, data.width-30, 219, 
                        arrow = LAST, width = 2)
    canvas.create_line(data.width-30, 221, data.width-30, 235, 
                        arrow = FIRST, width = 2)
    canvas.create_text(data.width-60, 220, text = "s", 
                        font = "sansserif 14 bold")
    
    
    #increase width 
    canvas.create_rectangle(data.width-70, 250, data.width-10, 290, 
                            fill = data.cream, width = 2)
    canvas.create_line(data.width-45, 270, data.width-32, 270, 
                        arrow = FIRST, width = 2)
    canvas.create_line(data.width-28, 270, data.width-15, 270, 
                        arrow = LAST, width = 2)
    canvas.create_text(data.width-60, 270, text = "d", 
                        font = "sansserif 14 bold")
    
    #decrease width 
    canvas.create_rectangle(data.width-70, 300, data.width-10, 340, 
                            fill = data.cream, width = 2)
    canvas.create_line(data.width-45, 320, data.width-31, 320, 
                        arrow = LAST, width = 2)
    canvas.create_line(data.width-29, 320, data.width-15, 320, 
                        arrow = FIRST, width = 2)
    canvas.create_text(data.width-60, 320, text = "a", 
                        font = "sansserif 14 bold")



####################################
# move furniture mode
####################################

class Furniture(object):
    
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        self.selected = False
        self.relativeX = None
        self.relativeY = None
    
    def draw(self, canvas):
        pass
        
    def containsPoint(self, x, y):
        pass
    
        
class Couch(Furniture):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 100
        self.height = 50
        self.color = "blue"
        
    def draw(self, canvas):
        canvas.create_rectangle(self.x-self.width, self.y-self.height, 
                                self.x+self.width, self.y+self.height, 
                                fill = "brown")
        canvas.create_oval(self.x-self.width-25, self.y-self.height, 
                            self.x-self.width, self.y+self.height, 
                            fill = "white")
        canvas.create_oval(self.x+self.width, self.y-self.height, 
                            self.x+self.width+25, self.y+self.height, 
                            fill = "white")
        
    def containsPoint(self, x, y):
        if (x > self.x - self.width and x < self.x + self.width and 
            y > self.y - self.height and y < self.y + self.height): return True

    def __repr__(self):
        return "(x%d, y%d)"%(self.x, self.y)

class Table(Furniture):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 25
        self.height = 25
        self.color = "green"
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x-self.width,self.y-self.height, 
                                self.x+self.width, self.y+self.height, 
                                fill = "gray", width = 2)
    
    def containsPoint(self, x, y):
        if (x > self.x - self.width and x < self.x + self.width and 
            y > self.y - self.height and y < self.y + self.height): return True

    def __repr__(self):
        return "(x%d, y%d)"%(self.x, self.y)

class Rug(Furniture):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 40
        self.height = 25
        self.color = "pink"
    def draw(self, canvas):
        canvas.create_rectangle(self.x-self.width,self.y-self.height, 
                                self.x+self.width, self.y+self.height, 
                                fill = "pink", width = 2)
        
    def containsPoint(self, x, y):
        if (x > self.x - self.width and x < self.x + self.width and 
            y > self.y - self.height and y < self.y + self.height): return True
    
    def __repr__(self):
        return "(x%d, y%d)"%(self.x, self.y)

    
def moveFurnitureMousePressed(event, data):
    
    if data.furnitureCreate == True:
        data.furnitureMove = False
    
        #couch 
        if (event.x < data.width/3 and event.x > 0 and event.y < 100 and 
            event.y > 50):
        
            data.currentRoom.pieces.append(Couch(event.x, event.y))
            
        #table 
        elif (event.x < data.width*(2/3) and event.x > data.width/3 and 
                event.y < 100 and event.y > 50):
          
            data.currentRoom.pieces.append(Table(event.x, event.y))
        #rug 
        elif (event.x < data.width and event.x > data.width*(2/3) and 
                event.y < 100 and event.y > 50):
            
            data.currentRoom.pieces.append(Rug(event.x, event.y))
    
    else:
        data.furnitureMove = True 
        currentTrueIndex = 0
        for i in range(len(data.currentRoom.pieces)):
            piece = data.currentRoom.pieces[i]
            if piece.containsPoint(event.x, event.y):
                data.currentRoom.pieces[i].selected = True
                currentTrueIndex = i
                
        for j in range(len(data.currentRoom.pieces)):
            if j == currentTrueIndex: continue
            else: data.currentRoom.pieces[j].selected = False 
                
    
    #if the buttons are pressed 
    if (event.x < data.width*.75+30 and event.x > data.width*.75-30 and 
        event.y < data.height-20 and event.y > data.height-60):
        
        data.furnitureCreate = False
        data.furnitureMove = True
    
    elif (event.x < data.width/4+30 and event.x > data.width/4-30 and 
            event.y < data.height-20 and event.y > data.height-60):
        
        data.furnitureCreate = True
        data.furnitureMove = False
        
    elif (event.x < 60 and event.y < 30 and event.x > 20 and event.y > 10):
        
        data.mode = "createHouse"
    
    elif (event.x < data.width-20 and event.y < 30 and event.x > data.width-60 
            and event.y > 10):
        
        data.mode = "doneScreen"
        
    
        
        
def moveFurnitureKeyPressed(event, data):
    
    if data.furnitureMove == True: 
        for piece in data.currentRoom.pieces:
            if piece.selected == True:
                if event.keysym == "Up": 
                    piece.y -= 10
                    
                elif event.keysym == "Down": 
                    piece.y +=10
                    
                elif event.keysym == "Left": 
                    piece.x -= 10
                    
                elif event.keysym == "Right": 
                    piece.x += 10
                    
                elif event.char == '+': 
                    piece.width += 10
                    piece.height += 10
                elif event.char == '-':
                    piece.width -= 10 
                    piece.height -= 10 
                elif event.char == 'b':
                    data.mode = "createHouse"
                
        
def moveFurnitureRedrawAll(canvas, data):
    #background
    
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.lavender)
    
    canvas.create_rectangle(data.width/2-2*(data.currentRoom.width), 
                            data.height/2 -2*(data.currentRoom.height), 
                            data.width/2+2*(data.currentRoom.width), 
                            data.height/2 +2*(data.currentRoom.height),width=2)
                            
    canvas.create_rectangle(150, 10, 350, 40, fill = data.cream, width = 2)
    canvas.create_text(250, 25, text = "Add Your Furniture", 
                        font = "sansserif 16 bold")
    
    #couch
    canvas.create_rectangle(0, 50, data.width/3, 100, width = 2, 
                            fill = data.cream)
    canvas.create_text(data.width*.165, 75, text = "couch", 
                        font = "sansserif 16 bold")
    #table
    canvas.create_rectangle(data.width/3, 50, data.width*(2/3), 100, 
                            width = 2, fill = data.cream)
    canvas.create_text(data.width*.495, 75, text = "table", 
                        font = "sansserif 16 bold")
    #rug 
    canvas.create_rectangle(data.width*(2/3), 50, data.width, 100,
                            width = 2, fill = data.cream)
    canvas.create_text(data.width*.832, 75, text = "rug", 
                        font = "sansserif 16 bold")
    
    #buttons
    
    #create
    canvas.create_rectangle(data.width/4-30, data.height-60, data.width/4+30, 
                            data.height-20, width = 2, fill = data.cream)
    canvas.create_text(data.width*.25, data.height-40, text = "create", 
                        font = "Sansserif 14")
    #move
    canvas.create_rectangle(data.width*.75-30, data.height-60, 
                            data.width*.75+30, data.height-20, width = 2, 
                            fill = data.cream)
    canvas.create_text(data.width*.75, data.height-40, text = "move", 
                        font = "Sansserif 14")
    
    
    
    
    
    #back
    canvas.create_polygon(20, 10, 60, 10, 60, 30, 20, 30, 10, 20, 
                            fill = data.cream, outline = "black", width = 2)
    canvas.create_text(40, 20, text = "back", font = "sansserif 10 bold")
    
    #done
    canvas.create_polygon(data.width-60, 10, data.width-20, 10,data.width-10,20, 
                            data.width-20, 30, data.width-60, 30, 
                            fill = data.cream, outline = "black", width = 2)
    canvas.create_text(data.width-40, 20, text = "done", 
                        font = "sansserif 10 bold")
    
    for piece in data.currentRoom.pieces:
        piece.draw(canvas)

        
    
def moveFurnitureTimerFired(data):
    for furniture in data.currentRoom.pieces:
        print(furniture)
    updateRelativePosition(data)

def updateRelativePosition(data):
    for room in data.rectangles:
        if room==data.currentRoom: 
            for furniture in room.pieces:
                furniture.relativeX = (furniture.x-data.width/2)/2
                furniture.relativeY = (furniture.y-data.height/2)/2
                
                
    
    
######################
# done screen
#######################

def doneScreenMousePressed(event,data):
    if (event.x < 60 and event.y < 30 and event.x > 20 and event.y > 10):
        
        data.mode = "moveFurniture"
    
def doneScreenKeyPressed(event, data):
    pass

def doneScreenTimerFired(data):
    pass
    
def drawCouch(canvas, couch, x, y):
    canvas.create_rectangle(x-couch.width/2, y-couch.height/2, x+couch.width/2, 
                            y+couch.height/2, fill = "brown")
    canvas.create_oval(x-(couch.width+25)/2, y-couch.height/2, x-couch.width/2, 
                            y+couch.height/2, fill = "white")
    canvas.create_oval(x+couch.width/2, y-couch.height/2, x+(couch.width+25)/2,
                        y+couch.height/2, fill = "white")

def drawTable(canvas, table, x, y):
    canvas.create_rectangle(x-table.width/2,y-table.height/2,x+table.width/2, 
                            y+table.height/2, fill = "gray", width = 2)

def drawRug(canvas, rug, x, y):
    canvas.create_rectangle(x-rug.width/2,y-rug.height/2, x+rug.width/2, 
                            y+rug.height/2, fill = "pink", width = 2)

def doneScreenRedrawAll(canvas,data):
    
    canvas.create_rectangle(0,0, data.width, data.height, fill = data.peachtan)
    canvas.create_rectangle(150, 10, 350, 50, width = 2, fill = data.cream)
    canvas.create_text(250, 30, text = "Final Creation", 
                        font = "sansserif 16 bold")
    canvas.create_rectangle(30, 60, 420, 400, width = 3, 
                            outline = data.lightblack)
    
    for i in range (0, len(data.rectangles)):
        rect = data.rectangles[i]
        rect.draw(canvas)
    
    for room in data.rectangles:
        for furniture in room.pieces:
            if type(furniture)==Couch:
                drawCouch(canvas, furniture, room.x+furniture.relativeX, 
                            room.y+furniture.relativeY)
            elif type(furniture)==Table:
                drawTable(canvas, furniture, room.x+furniture.relativeX, 
                            room.y+furniture.relativeY)
            elif type(furniture)==Rug:
                drawRug(canvas, furniture, room.x+furniture.relativeX, 
                            room.y+furniture.relativeY)
    
   
        
    #back
    canvas.create_polygon(20, 10, 60, 10, 60, 30, 20, 30, 10, 20, 
                            fill = data.cream, outline = "black", width = 2)
    canvas.create_text(40, 20, text = "back", font = "sansserif 10 bold")
    
    
####################################
# help screen mode 
#####################################

def helpScreenMousePressed(event, data):
    if (event.x < 60 and event.y < 30 and event.x > 20 and event.y > 10):
        data.mode = "splashScreen"
    

def helpScreenKeyPressed(event, data):
    pass

def helpScreenTimerFired(data):
    pass

def helpScreenRedrawAll(canvas, data):
    #Background
    canvas.create_rectangle(0, 0, data.width, data.height, 
                                fill = data.lavender, width = 0)
    
    description = '''
    Welcome to your personal interior designer! 
    Here, you will be able to design your dream 
    home and arrange furniture to your liking. 
    '''

    instructions = '''
    Press create to make a new room. 
    Press move to adjust the room.
    Use the arrow keys to move the room.
    Use the given keys to adjust its size.
    When you are finished, press next to continue, 
    or back to return to the previous screen.
    
    
    
    Press create to add a furniture. 
    Choose your furniture from the menu above. 
    Press move and then click the furniture you want to move.
    After you are finished, press done, 
    or back to return to the previous screen.
    
    Press done to view your entire creation!
    '''
    
    
    canvas.create_text(data.width/2, 75, text = description, 
                        font = "sansserif 18 bold")
    canvas.create_text(data.width/2, 300, text = instructions, 
                            font = "sansserif 14")
    
    
    #back
    canvas.create_polygon(20, 10, 60, 10, 60, 30, 20, 30, 10, 20, 
                            fill = data.cream, outline = "black", width = 2)
    canvas.create_text(40, 20, text = "back", font = "sansserif 10 bold")
    

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("Thank you for using InDesigner!")

run(500, 500)





    
    
    
