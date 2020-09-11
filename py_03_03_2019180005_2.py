
import turtle
turtle

count = 0
i=0
while(i<2):
        count=0
        while (count <=5):
                turtle.penup()
                if(i==0):
                        turtle.goto(count*100,500)
                        turtle.pendown()
                        turtle.goto(count*100,0)
                else:
                        turtle.goto(0,count*100)
                        turtle.pendown()
                        turtle.goto(500,count*100)
                count = count+1       
        i=i+1

turtle.exitonclick()
