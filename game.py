import turtle
playerAscore=0
playerBscore=0
win = turtle.Screen()
win.title("Let's play pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# player1
player_1=turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("blue")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350,0)

#player_2
player_2=turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("blue")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350,0)

#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("White")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2 
ballydirection=0.2

pen=turtle.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align="center",font=("Arial",24,"normal"))
# Macanisim 
def player_1_up():
    y= player_1.ycor()
    y+=20
    player_1.sety(y)
    
    
def player_1_down():
    y= player_1.ycor()
    y-=20
    player_1.sety(y)
    
    
    
def player_2_up():
    y= player_2.ycor()
    y+=20
    player_2.sety(y)
    
    
def player_2_down():
    y= player_2.ycor()
    y-=20
    player_2.sety(y)
#keyboard controls
win.listen()
win.onkeypress(player_1_up, "w")
win.onkeypress(player_1_down, "s")

win.onkeypress(player_2_up, "Up")
win.onkeypress(player_2_down, "Down")
while True:
    win.update()
    
    
    #move the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)
    
    #border checking 
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection*=-1
        
    if ball.ycor()>-290:
        ball.sety(-290)
        ballydirection*=-1
        
    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        playerAscore+=1
        pen.clear()
        pen.write("playerA:{}        playerB:{}".format(playerAscore,playerBscore),align="center",font=("Arial",24,"normal"))
        
    if ((ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<player_1.ycor()+20)and ball.ycor()>player_1.ycor()>player_1.ycor()-20):
        ball.setx(340)
        ballxdirection=ballxdirection*-1
        
    if ((ball.xcor()>-340)and(ball.xcor()<-350)and(ball.ycor()<player_2.ycor()+20)and ball.ycor()>player_2.ycor()>player_2.ycor()-20):
        ball.setx(-340)
        ballxdirection=ballxdirection*-1