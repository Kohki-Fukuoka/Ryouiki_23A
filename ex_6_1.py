import json

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

def main():
    with open("kabeposter\kabeposter_000000000000_keypoints.json", "r") as f:
        data = json.load(f)
    
    LPI = {"鼻":0, "首":1}

    for p in data["people"]:

        # show personid
        print(f"person_id = {p['person_id']}")

        # show detail
        for key, value in LPI.items():
            x, y, r = get_detail_of_landmark(p, value)
            print(f"{key} : x = {x}, y = {y}, reliability = {r}")

if __name__ == "__main__":
    main()