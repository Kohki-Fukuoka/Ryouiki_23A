import tkinter as tk

def main():
    root = tk.Tk()
    root.title("04")
    root.geometry("500x500")
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.place(x=0, y=0)

    # head
    canvas.create_oval(200, 100, 300, 200)
    # body
    canvas.create_line(250, 200, 250, 300)
    # arms
    canvas.create_line(150, 250, 250, 225)
    canvas.create_line(350, 250, 250, 225)
    # legs
    canvas.create_line(175, 350, 250, 300)
    canvas.create_line(325, 350, 250, 300)

    canvas.mainloop()

if __name__ == "__main__":
    main()