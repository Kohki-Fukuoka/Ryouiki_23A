import json
import tkinter as tk

from ex_5 import TKCanvas

LPI = {"Neck":1, "Right_Sholder":2, "Left_Sholder":5}

def get_x_index(point:int) -> int:
    return point * 3

def get_y_index(point:int) -> int:
    return point * 3 + 1

def get_reliability_index(point:int) -> int:
    return point * 3 + 2

def keyListener(event):
    pass

def get_detail_of_landmark(person_data, landmark_index):
    keypoints = person_data['pose_keypoints_2d']
    res_x = keypoints[get_x_index(landmark_index)]
    res_y = keypoints[get_y_index(landmark_index)]
    res_reliability = keypoints[get_reliability_index(landmark_index)]
    return res_x, res_y, res_reliability

def draw_sholder(canvas:tk.Canvas, p, color):
    bias = 0.25
    ne = get_detail_of_landmark(p, LPI["Neck"])
    rs = get_detail_of_landmark(p, LPI["Right_Sholder"])
    ls = get_detail_of_landmark(p, LPI["Left_Sholder"])
    canvas.create_line(rs[0] * bias, rs[1] * bias, ne[0] * bias, ne[1] * bias, fill=color, width=5)
    canvas.create_line(ne[0] * bias, ne[1] * bias, ls[0] * bias, ls[1] * bias, fill=color, width=5)

def get_color(length, index):
    red = "{:02x}".format(int(255 * index / (length - 1)))
    green = "{:02x}".format(0)
    blue = "{:02x}".format(int(255 * (length - index - 1) / (length - 1)))

    return f"#{red}{green}{blue}"

def main():
    tkc = TKCanvas("ex_6_2", keyListener)
    root, canvas = tkc.get()
    root.geometry("500x500")
    
    with open("kabeposter\kabeposter_000000000000_keypoints.json", "r") as f:
        data = json.load(f)

    for i, p in enumerate(data["people"]):

        l = len(data["people"])

        color = get_color(l, i)

        draw_sholder(canvas, p, color)

    root.mainloop()

if __name__ == "__main__":
    main()