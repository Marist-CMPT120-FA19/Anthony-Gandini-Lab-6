#Anthony Gandini

from graphics import *

def drawTrafficLight(x , y):
    drawLightBody(x , y , 900 , 700)
    drawLamp("green" , 500 , 750 , 100)
    drawLamp("yellow" , 500 , 500 , 100)
    drawLamp("red" , 500 , 250 , 100)
    
def drawLamp(color , x , y , radius):
    lamp = Circle(Point(x , y) , radius)
    lamp.setFill(color)
    lamp.draw(win)
    
def drawLightBody(x , y , length , width):
    body = Rectangle(Point(x , y) , Point(width , length))
    body.setFill("white")
    body.draw(win)
    
win = GraphWin("Traffic Light" , 1000 , 1000)    
drawTrafficLight(300 , 100)