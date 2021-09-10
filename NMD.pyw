import turtle
import json
import winsound
from random import *
import tkinter
import os
import time

# Window
win = turtle.Screen()
win.title('No More Dots !')
win.setup(width=800, height=600)
win.bgpic("Data/Assets/background.png")
win.tracer(0)
win.bgcolor("#6abe30")
icon = "Data\Assets\icon.png"
win.cv._rootwindow.resizable(False, False)
img = tkinter.Image("photo", file="Data/Assets/icon.png")
turtle._Screen._root.iconphoto(True, img)

# User Name
username = open('Data/username.json','r')
get_name = username.read()
obj = json.loads(get_name)
user_name = str(obj['username'])

# User Name Viewer
player_name = turtle.Turtle()
player_name.speed(0)
player_name.color("#6abe30")
player_name.penup()
player_name.hideturtle()
player_name.goto(-310, 230)
player_name.write(user_name, align="left", font=("System", 30, "bold")) 

# Score 
score = 0
score_viewer = turtle.Turtle()
score_viewer.speed(0)
score_viewer.color("white")
score_viewer.penup()
score_viewer.hideturtle()
score_viewer.goto(359, 225)
score_viewer.write(score, align="center", font=("System", 40, "bold"))

# Shows Score After Game Ends 
score = 0
EndScore = turtle.Turtle()
EndScore.speed(0)
EndScore.color("#6abe30")
EndScore.penup()
EndScore.hideturtle()
EndScore.goto(0,0)


# Menu Function
def leave(x, y):
    winsound.PlaySound("Data\Sounds\close.wav", winsound.SND_ASYNC)
    win.bye()

# Menu
menupic = 'Data\Assets\menu.gif'
menu = turtle.Turtle()
menu.speed(0)
menu.penup()
menu.goto(-360, 260)
win.addshape(menupic)
menu.shape('Data\Assets\menu.gif')
menu.onclick(fun=leave)

# Bit
bitpic = 'Data/Assets/bit.gif'
bit = turtle.Turtle()
bit.speed(0)
bit.penup()
bit.goto(randint(-373,373),randint(-250,216))
win.addshape(bitpic)
bit.shape("Data/Assets/bit.gif")

# Player
playerpic1 = 'Data\Assets\player\player1.gif'
playerpic2 = 'Data\Assets\player\player2.gif'
playerpic3 = 'Data\Assets\player\player3.gif'
playerpic4 = 'Data\Assets\player\player4.gif'
win.addshape(playerpic1)
win.addshape(playerpic2)
win.addshape(playerpic3)
win.addshape(playerpic4)
player = turtle.Turtle()
player.penup()
player.goto(0,-210)
player.speed(0)
player.shape('Data\Assets\player\player1.gif')

# Player Animation
player.frame = 0
player.frames = ["Data\Assets\player\player1.gif", "Data\Assets\player\player2.gif", "Data\Assets\player\player3.gif", "Data\Assets\player\player4.gif"]
def player_animate():
	player.frame += 1
	if player.frame >= len(player.frames):
		player.frame = 0
	player.shape(player.frames[player.frame])
	# Set timer
	win.ontimer(player_animate, 500)
player_animate()

# Player Move Functions
def player_up():
    y = player.ycor()
    y += 20
    player.sety(y)
def player_down():
    y = player.ycor()
    y -= 20
    player.sety(y)
def player_right():
    x = player.xcor()
    x -= 20
    player.setx(x)
def player_left():
    x = player.xcor()
    x += 20
    player.setx(x) 

# Keyboard Binding
win.onkeypress(player_up, "w")
win.onkeypress(player_down, "s")
win.onkeypress(player_right, "a")
win.onkeypress(player_left, "d")
win.listen()
# Pause Game
is_paused = False

def toggle_pause():
    global is_paused

# time Limit
time_limit = 30
start_time = time.time()

# Game's Loops
while True:
    if not is_paused:
        win.update()
        # Player and Bit Touch Detector
        if player.distance(bit) <30  :
            bit.goto(randint(-373,373),randint(-250,216))
            score +=1
            score_viewer.clear()
            score_viewer.write("{}".format(score), align="center", font=("System", 40, "bold"))
        # Make Player Be Inside Canvas
        if player.xcor() < -375:
            player.setx(player.xcor() + 20 )
        if player.xcor() > 375:
            player.setx(player.xcor() - 20 )
        if player.ycor() < -250:
            player.sety(player.ycor() + 20 )
        if player.ycor() > 220:
            player.sety(player.ycor() - 20 )     
        
        # Timer
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            # After Timer Ends
            score_viewer.hideturtle()
            player_name.hideturtle()
            bit.hideturtle()
            player.hideturtle()
            bit.goto(1000,1000)
            EndScore.write("{} has made new record :  {} ".format(user_name,score), align="center", font=("System", 25, "bold"))
        start_time = time.time() - elapsed_time
        win.update()
win.mainloop()
