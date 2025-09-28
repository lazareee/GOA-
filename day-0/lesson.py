from turtle import*

#we want to paint a house

#step 1: draw a squeare
speed(30)

width(4)
color("black")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of squeare


#start of door

forward(70)
left(90)

color("orange")
begin_fill()
forward(80)
right(90)
forward(60)         #height of the door
right(90)
forward(80)
end_fill()

#end of the door

#start of the roof

penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of roof

#start of window

penup()
goto(0, 0)
pendown()

color("black")
right(150)
forward(100)

begin_fill()

color("white")
right(90)
forward(20)

color("blue")
left(90)
forward(50)

right(90)
forward(40)

right(90)
forward(50)

right(90)
forward(40)

end_fill()

color("white")
forward(20)

penup()
goto(200, 200)
pendown()

color("black")
left(90)
forward(100)

begin_fill()

color("white")
right(90)
forward(20)

color("blue")
forward(40)
right(90)
forward(50)

right(90)
forward(40)

right(90)
forward(50)

end_fill()

exitonclick()