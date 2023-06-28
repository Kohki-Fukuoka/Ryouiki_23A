import json
import tkinter as tk
import os
import time

from ex_5 import TKCanvas

# landmark's binding dictionaly
bind_dic = []

isActive = True

def get_x_index(point:int) -> int:
    # landmark index to json's list index about x
    return point * 3

def get_y_index(point:int) -> int:
    # landmark index to json's list index about y
    return point * 3 + 1

def get_reliability_index(point:int) -> int:
    # landmark index to json's list index about reliability
    return point * 3 + 2

def keyListener(event):
    global isActive
    match event.keycode:
        case 27:
            isActive = False

def get_detail_of_landmark(person_data, landmark_index):
    # get landmark's x, y, reliability
    keypoints = person_data['pose_keypoints_2d']
    res_x = keypoints[get_x_index(landmark_index)]
    res_y = keypoints[get_y_index(landmark_index)]
    res_reliability = keypoints[get_reliability_index(landmark_index)]
    return res_x, res_y, res_reliability


def draw_human(canvas:tk.Canvas, p, color):
    # draw human
    # canvas size / capture size
    adj = 0.25

    for bind in bind_dic:
        # binding
        # get start point and end point
        x0, y0, _ = get_detail_of_landmark(p, bind[0])
        x1, y1, _ = get_detail_of_landmark(p, bind[1])

        # show only not lost data
        if (x0 != 0) & (y0 != 0) & (x1 != 0) & (y1 != 0):
            canvas.create_line(x0 * adj, y0 * adj, x1 * adj, y1 * adj, fill=color, width=5)

def get_color(length, index):
    # get personal color
    red = "{:02x}".format(int(255 * index / (length - 1)))
    green = "{:02x}".format(0)
    blue = "{:02x}".format(int(255 * (length - index - 1) / (length - 1)))

    return f"#{red}{green}{blue}"

def load_bind_dic():
    # load landmark's binding
    with open("bind_dic.text", "r") as dic_f:
        bd_sp_nl = dic_f.read().split("\n")
        for dline in bd_sp_nl:
            if dline != "":
                bind_dic.append([int(i) for i in dline.split(",")])
    

def main():
    # prepare tk
    tkc = TKCanvas("ex_6_3", keyListener)
    root, canvas = tkc.get()
    root.geometry("500x500")

    load_bind_dic()
    
    frame_i = 0

    while isActive:
        # counter start
        stt = time.time()

        # make path
        number = "{:012}".format(frame_i)
        path = f"kabeposter\kabeposter_{number}_keypoints.json"

        if not os.path.exists(path):
            # json file is not exists
            # restart animation
            frame_i = 0
            continue

        # reflesh canvas
        canvas.delete("all")

        # load json
        with open(path, "r") as f:
            data = json.load(f)

        for i, p in enumerate(data["people"]):
            # each person
            # num of landmarks
            l = len(data["people"])

            # make personal color
            color = get_color(l, i)

            # draw
            draw_human(canvas, p, color)
        
        # counter stop
        ent = time.time()

        # wait
        dt = ent - stt
        if dt < 0.03:
            time.sleep(0.03 - dt)

        # update graphics
        root.update()
    
        frame_i += 1

if __name__ == "__main__":
    main()