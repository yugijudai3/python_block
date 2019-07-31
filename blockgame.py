from tkinter import *

ball = {
    "dirx": 5, #xDirection
    "diry": -5, #yDirection
    "x": 350, #ballPosition
    "y": 300,
    "w": 10 #ballWidth
}

win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

#LoadWindow
def draw_object():
    cv.delete("all") #reset
    #drawBall
    cv.create_oval(
        ball["x"] - ball["w"], ball["y"] - ball["w"],
        ball["x"] + ball["w"], ball["y"] + ball["w"],
        fill="red"
    )
    
#moveBall
def move_ball():
    #aftermove
    bx = ball["x"] + ball["dirx"]
    by = ball["y"] + ball["diry"]

    #Collision
    if bx < 0 or bx > 600:
        ball["dirx"] *= -1

    if by < 0 or by > 400:
        ball["diry"] *= -1
    
    #move
    if 0 <= bx <= 600:
        ball["x"] = bx

    if 0 <= by <= 400:
        ball["y"] = by

def game_loop():
    draw_object()
    move_ball()
    win.after(50, game_loop)

game_loop()
win.mainloop()