# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 17:39:13 2018

@author: SzékelyLégió
"""

import turtle 
wn = turtle.Screen()
wn.title("Migráns invázió 2")
wn.bgcolor("orange")
wn.setup(width=800, height = 600)




player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"


def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"


wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right") 

while True:
    wn.update()
   
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)
        
    
    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)
        



wn.mainloop()
