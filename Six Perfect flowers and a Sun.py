import turtle as tu
x = 0
y = 0
c1=""
c2=""
c3=""
c4=""
tu.bgcolor("Light Blue")
tu.hideturtle()


#Drawing of the flowers
def flower(x, y, c1):
    tu.pu()
    tu.goto(x, y)
    tu.pd()
    counter= 0
    tu.speed(75)
    tu.begin_fill()
    tu.seth(0)
    while counter < 4:
        tu.color(c1, c1)
        tu.right(30)
        tu.forward(45)
        tu.left(60)
        tu.forward(50)
        tu.right(30)
        tu.forward(45)
        tu.left(60)
        tu.forward(50)
        tu.right(30)
        tu.forward(45)
        tu.left(60)
        tu.forward(50)
        tu.right(30)
        tu.forward(45)
        tu.left(60)
        tu.forward(50)
        counter = counter+1
    tu.end_fill()
    

#Drawing of the stems
def stem(x, y, c2):
    tu.pu()
    tu.setpos(x,y)
    tu.pd()
    tu.pensize(20)
    tu.pencolor(c2)
    tu.seth(270)
    tu.forward(500)


#Drawing of the majestic dots
def dot(x, y, c3):
    tu.pu()
    tu.setpos(x,y)
    tu.pd()
    tu.pensize(70)
    tu.pencolor(c3)
    tu.forward(1)


#Drawing of the high quality sun
def sun(x, y, c4):
    tu.pu()
    tu.setpos(x,y)
    tu.pd()
    tu.pensize(200)
    tu.pencolor(c4)
    tu.forward(1)


#The coordinates of where the objects are drawn
stem(x, y, "Light Green")
flower(x, y, "Violet")
dot(40, 150, "Black")
stem(275, -100, "Light Green")
flower(222, -100, "Gold")
dot(260, 50, "Black")
stem(-375, -23, "Light Green")
flower(-400, -23, "Red")
dot(-365, 127, "Black")
stem(-197, -200, "Light Green")
flower(-197, -200,"Orange")
dot(-160, -50, "Black")
stem(450, -250, "Light Green")
flower(420, -275, "Navy")
dot(460, -125, "Black")
stem(-525, -250, "Light Green")
flower(-545, -250, "Pink")
dot(-500, -100, "Black")
sun(550, 300, "Yellow")
