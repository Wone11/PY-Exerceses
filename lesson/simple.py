import turtle
import random

#simple design in turtle...
t = turtle.Turtle()
turtle.color('black')
arr =['violet','blue','green','red','yellow','maroon','olive']
turtle.bgcolor('black')

for i in range(1000):
    x= random.randint(0,len(arr)-1)
    t.speed(200)
    t.color(arr[x])
    t.forward(100*3)  
    t.right(190)

turtle.done()  
    
