'''
Enhance your lunar lander assignment to work like a version of the classic console game asteroids.
Add a number of moving circles that travel around the screen in random directions.  Have the circles wrap around the screen so they never disappear.
If your lander collides with the asteroid, then the game is over.  A collision occurs when the distance between the two objects is less than the sum of both radii.
Spacecraft:
- Position: XC, YC  (absolute coordinates)
- Move using arrow keys
- Draw a circle of radius RC from the center of the object
Asteroid:
- Position: XA, YA
- Size: RA (radius)
- Move: XM, YM (randomly generated)
- Wrap Around the screen:
if (XA> XMax):
  XA= XMin
---- repeat for XMin, YMax, and TMIN
Collision:
- D= SQRT( (XC-XA)**2 + (YC-YA)**2)
- Collision when D<= RA+RC
'''

import turtle
import random
import math
import time

# Two instances of Turtle to avoid clearing the asteroids when moving the lander
# Asteroid turtle
turast= turtle.Turtle()
turast.speed(0)
turast.hideturtle()

# Lander turtle
turlan = turtle.Turtle()
turlan.speed(0)
turlan.hideturtle()

# Set up the screen
win = turtle.Screen()
win.title("Asteroid")
win.bgcolor("black")
win.setup(width=1000,height=1000)
win.tracer(0)

YMax = 500
YMin = -500
XMax = 500
XMin = -500
XC = 0
YC = 0
speed = [1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3]
size = [50,80,100]
asteroids = []
collision = False
delay = 0.1

class Asteroid(object):
    def __init__(self):
        # Choose direction and size of asteroid
        self.direction = random.randint(0,2)
        self.size = random.choice(size)
        self.speed = random.choice(speed)

        # Determine asteroid starting position
        if(random.randint(0,1)==0):
            # Get X-axis starting position
            self.XA = random.randint(-500,500)
            if(random.randint(0,1)==0):
                # Set Y-axis starting position
                self.YA = -500
                # Set speed and direction
                if self.direction==0:
                    self.XM = 0
                    self.YM = 5*self.speed
                elif self.direction==1:
                    self.XM = 4*self.speed
                    self.YM = 4*self.speed
                elif self.direction==2:
                    self.XM = -4*self.speed
                    self.YM = 4*self.speed
            else:
                # Set Y-axis starting position
                self.YA = 500
                # Set speed and direction
                if self.direction==0:
                    self.XM = 0
                    self.YM = -5*self.speed
                elif self.direction==1:
                    self.XM = 4*self.speed
                    self.YM = -4*self.speed
                elif self.direction==2:
                    self.XM = -4*self.speed
                    self.YM = -4*self.speed
        else:
            # Get Y-axis starting position
            self.YA = random.randint(-500,500)
            if(random.randint(0,1)==0):
                # Set X-axis starting position
                self.XA = -500
                # Set speed and direction
                if self.direction==0:
                    self.XM = 5*self.speed
                    self.YM = 0
                elif self.direction==1:
                    self.XM = 4*self.speed
                    self.YM = 4*self.speed
                elif self.direction==2:
                    self.XM = 4*self.speed
                    self.YM = -4*self.speed
            else:
                # Set X-axis starting position
                self.XA = 500
                # Set speed and direction
                if self.direction==0:
                    self.XM = -5*self.speed
                    self.YM = 0
                elif self.direction==1:
                    self.XM = -4*self.speed
                    self.YM = 4*self.speed
                elif self.direction==2:
                    self.XM = -4*self.speed
                    self.YM = -4*self.speed

    def draw(self):
        # Draw the asteroid
        turast.color("black")
        turast.pu()
        turast.goto(self.XA,self.YA)
        turast.pd()
        turast.fillcolor("gray")
        turast.begin_fill()
        turast.circle(self.size)
        turast.end_fill()

    def move(self):
        # Set X coordinate
        if self.XA>XMax:
            self.XA=XMin
        elif self.XA<XMin:
            self.XA=XMax
        else:
            self.XA+=self.XM
        # Set Y coordinate
        if self.YA>YMax:
            self.YA=YMin
        elif self.YA<YMin:
            self.YA=YMax
        else:
            self.YA+=self.YM
        # Draw asteroid
        self.draw()

    def detectCollision(self):
        # Detect if a collision has occured
        global collision
        # Numbers added to coordinates are so the hitbox is centered on the object
        distance = math.sqrt(((self.XA-(XC+25))**2)+(((self.YA+self.size)-(YC+35))**2))
        minimum = self.size + 37.5
        if(distance<=minimum):
            collision = True

    def speedIncrease(self):
        # Increase movement speed
        self.XM*=1.25
        self.YM*=1.25

def drawLander():
    # Draw lander
    turlan.color("silver")
    turlan.pu()
    turlan.goto(XC,YC)
    turlan.pd()
    turlan.fillcolor("silver")
    turlan.begin_fill()
    turlan.setheading(0)
    for i in range(4):
        turlan.forward(50)
        turlan.left(90)
    turlan.setheading(215)
    turlan.forward(25)
    turlan.back(25)
    turlan.setheading(0)
    turlan.forward(50)
    turlan.setheading(325)
    turlan.forward(25)
    turlan.back(25)
    turlan.setheading(90)
    turlan.forward(50)
    turlan.setheading(135)
    turlan.forward(35.35)
    turlan.setheading(225)
    turlan.forward(35.35)
    turlan.setheading(270)
    turlan.forward(50)
    turlan.end_fill()
    turlan.pu()

    win.update()

def down():
    # On down move down and to max if min is reached
    if not collision:
        global YC
        if (YC<YMin):
            YC = YMax
        else:
            YC-=25
        turlan.clear()
        drawLander()
   
def up():
    # On up key press move up and to min if max is reached
    if not collision:
        global YC
        if (YC>YMax):
            YC = YMin
        else:
            YC+=25
        turlan.clear()
        drawLander()

def left():
    # On left key press move the object left and to max if min is reached
    if not collision:
        global XC
        if (XC<XMin):
            XC = XMax
        else:
            XC-=25
        turlan.clear()
        drawLander()

def right():
    # On right key press move the object right and to min if max is reached
    if not collision:
        global XC
        if (XC>XMax):
            XC = XMin
        else:
            XC+=25
        turlan.clear()
        drawLander()

def reset():
    # Reset game
    turtle.clear()
    global collision
    global asteroids
    global XC
    global YC
    XC = 0
    YC = 0
    asteroids = []
    collision = False
    turlan.clear()
    drawLander()
    mainloop()

def mainloop():
    i = 0
    # Main game loop again
    while not collision:
        # Inform player of increase in speed
        if i%350==0 and i!=0:
            turtle.pu()
            turtle.hideturtle()
            turtle.goto(0,0)
            turtle.color("red")
            turtle.write("25% Speed Increase", font=("Verdana", 50, "bold"), align="center")
            time.sleep(2.5)
            turtle.clear()
        # Clear asteroids
        turast.clear()
        # Create new asteroid every 20 cycles until there are 12
        if i%20==0 and i<=280:
            asteroids.append(Asteroid())
            asteroids[-1].draw()

        # Move asteroids and detect collisions
        for x in asteroids:
            # Increase speed every 350 cycles
            if i%350==0 and i!=0:
                x.speedIncrease()
            x.move()
            x.detectCollision()
        # Update screen
        win.update()
        time.sleep(delay)
        i+=1

    turast.clear()
    turlan.clear()
    turtle.pu()
    turtle.hideturtle()
    turtle.goto(0,0)
    turtle.color("silver")
    turtle.write("Game Over", font=("Verdana", 50, "bold"), align="center")
    turtle.goto(0,-25)
    turtle.write("'r' to restart", font=("Verdana", 25, "bold"), align="center")

drawLander()

# Key press listeners
win.listen()
win.onkey(down, "Down")
win.onkey(up, "Up")
win.onkey(left, "Left")
win.onkey(right, "Right")
win.onkey(reset, "r")

# Call main loop
mainloop()

win.exitonclick()