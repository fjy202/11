import turtle
t=turtle.Pen()
def zzt(list,color):
    t.speed(10)
    t.pensize(11)

    for x in list:
        t.pencolor(color[x%len(color)])
        t.forward(x)
        turtle.up()
        t.backward(x)
        t.left(90)
        turtle.down()
        t.forward(20)
        t.right(90)
    input("按回车退出")
zzt([100,200,300,400,500,600,700,800],['yellow','blue','black','green',"red","brown",'pink'])
