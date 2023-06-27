import tkinter as tk
import time

class TKCanvas:

    def __init__(self, title, keyListener) -> None:
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("500x500")
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.place(x=0, y=0)
        self.root.bind("<KeyPress>", keyListener)
    
    def get(self):
        return self.root, self.canvas

class Human:

    def __init__(self) -> None:
        self.x = 250
        self.y = 100
        self.vx = 10

    def draw(self, canvas) -> None:
        # head
        canvas.create_oval(self.x - 50, self.y, self.x + 50, self.y + 100)
        # body
        canvas.create_line(self.x, self.y + 100, self.x, self.y + 200)
        # arms
        canvas.create_line(self.x - 100, self.y + 150, self.x, self.y + 125)
        canvas.create_line(self.x + 100, self.y + 150, self.x, self.y + 125)
        # legs
        canvas.create_line(self.x - 75, self.y + 250, self.x, self.y + 200)
        canvas.create_line(self.x + 75, self.y + 250, self.x, self.y + 200)
    
    def move(self) -> None:
        if self.border_check_x():
            self.reflecte_x()
        self.x += self.vx
    
    def border_check_x(self) -> bool:
        return (self.x + self.vx < 100) | (self.x + self.vx > 400)
    
    def reflecte_x(self) -> None:
        self.vx *= (-1)

isActive = True

def keyListener(event):
    global isActive
    match event.keycode:
        case 27:
            isActive = False

def main():
    tkc = TKCanvas("ex_5", keyListener)
    root, canvas = tkc.get()
    human = Human()
    while(isActive):
        canvas.delete("all")
        human.move()
        human.draw(canvas)
        root.update()
        time.sleep(0.1)

if __name__ == "__main__":
    main()