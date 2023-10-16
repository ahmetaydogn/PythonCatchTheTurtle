import turtle
from random import randint
import time


isTurtleClicked = False


drawing_board = turtle.Screen()
drawing_board.title("Catch The Turtle")
drawing_board.bgcolor("light blue")

_x, _y = drawing_board.screensize()
style1 = ("Calibri", 20, "normal")
style2 = ("Calibri", 24, "bold", "underline")
score = 0

counter = 0
timer_text = f"Time: {20}"
score_text = f"Score: {score}"



# Helper Functions
def TurtleNewPositionCoordinats():
    global _x
    global _y
    _x,_y = drawing_board.screensize()
    turtle_x_pos = randint(-_x + 30, _x - 30)
    turtle_y_pos = randint(-_y + 25, _y - 25)
    #print(f"{turtle_x_pos} - {turtle_y_pos}")
    return turtle_x_pos, turtle_y_pos

def ClickedTurtle():
    global score
    global score_text

    score += 1
    score_text = f"Score: {score}"
    score_instance.clear()
    score_instance.write(score_text, align="center", font=style2)

    turtle_instance.goto(TurtleNewPositionCoordinats())
    print(score)

def ChangeIsTurtleClickedSituation(x, y):
    global isTurtleClicked
    isTurtleClicked = True

# Score Turtle Instance and Timer Instance Creating
score_instance = turtle.Turtle()
score_instance.speed(0)
timer_instance = turtle.Turtle()
timer_instance.speed(0)

# Score Instance Turtle Settings
score_instance.color("dark blue")
score_instance.penup()
score_instance.hideturtle()
score_instance.goto(0, _y - 10)
score_instance.pendown()
score_instance.write(score_text, align="center", font=style2)

# Timer Instance Turtle Settings
timer_instance.penup()
timer_instance.hideturtle()
timer_instance.goto(0, _y - 50)
timer_instance.write("Time: 20", align="center", font=style1)
timer_instance.pendown()


# Main Turtle Instance and some settings
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("dark green")
turtle_instance.pencolor(drawing_board.bgcolor())
turtle_instance.turtlesize(2.2)
turtle_instance.speed(0)


while counter <= 20:
    timer_instance.clear()
    turtle_instance.onclick(ChangeIsTurtleClickedSituation)
    if isTurtleClicked:
        ClickedTurtle()
        print("true")
    else:
        turtle_instance.goto(TurtleNewPositionCoordinats())
        print("false")

    counter += 1
    timer_instance.write(timer_text, align="center", font=style1)
    timer_text = f"Time: {20 - counter}"
    isTurtleClicked = False

    time.sleep(1)

    if counter == 20:
        timer_instance.clear()
        timer_instance.write("Game Over!", align="center", font=style1)
        break


drawing_board.mainloop()


"""
Turtle click olayı çözüldü,
1 - Kodu okunabilir bir hale getirdikten sonra dokunma algoritmasını daha iyi hale getir + 
2 - Score sistemini ekle + 
3 - Sayacı ve Game Over olayını ekle +
4 - Oyun zorluğu seçimini ekle / İptal
5 - Oyun başlarken ekrana 3 - 2 - 1 diye saydır / İptal
6 - Restart tuşu ve bir kaç ekstra özellik ekle (turtle renk değiştirme falan -> bir tuşa ata) / İptal
7 - Proje bittii
"""