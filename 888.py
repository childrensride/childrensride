import cv2
import json
import os
kpjson_file = 'E:\\else\\json\\eval\\zheng\\val_points.json'
point_size = 1
point_color,line_color,rec_color = (0, 0, 255),(0,255,0),(0, 255, 255)
cir_thickness,line_thickness,rec_thickness = 4,1,2


def draw_line():
    if xy_dict['x_1'] and xy_dict['y_6'] != 0:
        cv2.line(image, (int(xy_dict['x_1']), int(xy_dict['y_1'])), (int(xy_dict['x_6']), int(xy_dict['y_6'])), line_color,line_thickness)
    if xy_dict['x_6'] and xy_dict['y_7'] != 0:
        cv2.line(image, (int(xy_dict['x_6']), int(xy_dict['y_6'])), (int(xy_dict['x_7']), int(xy_dict['y_7'])), line_color,line_thickness)
    if xy_dict['x_3'] and xy_dict['y_5'] != 0:
        cv2.line(image, (int(xy_dict['x_3']), int(xy_dict['y_3'])), (int(xy_dict['x_5']), int(xy_dict['y_5'])), line_color,line_thickness)
    if xy_dict['x_3'] and xy_dict['y_7'] != 0:
        cv2.line(image, (int(xy_dict['x_3']), int(xy_dict['y_3'])), (int(xy_dict['x_7']), int(xy_dict['y_7'])), line_color,line_thickness)
    if xy_dict['x_2'] and xy_dict['y_7'] != 0:
        cv2.line(image, (int(xy_dict['x_2']), int(xy_dict['y_2'])), (int(xy_dict['x_7']), int(xy_dict['y_7'])), line_color,line_thickness)
    if xy_dict['x_2'] and xy_dict['y_4'] != 0:
        cv2.line(image, (int(xy_dict['x_2']), int(xy_dict['y_2'])), (int(xy_dict['x_4']), int(xy_dict['y_4'])), line_color,line_thickness)
    if xy_dict['x_9'] and xy_dict['y_11'] != 0:
        cv2.line(image, (int(xy_dict['x_9']), int(xy_dict['y_9'])), (int(xy_dict['x_11']), int(xy_dict['y_11'])), line_color,line_thickness)
    if xy_dict['x_11'] and xy_dict['y_13'] != 0:
        cv2.line(image, (int(xy_dict['x_11']), int(xy_dict['y_11'])), (int(xy_dict['x_13']), int(xy_dict['y_13'])), line_color,line_thickness)
    if xy_dict['x_13'] and xy_dict['y_15'] != 0:
        cv2.line(image, (int(xy_dict['x_13']), int(xy_dict['y_13'])), (int(xy_dict['x_15']), int(xy_dict['y_15'])), line_color,line_thickness)
    if xy_dict['x_8'] and xy_dict['y_10'] != 0:
        cv2.line(image, (int(xy_dict['x_8']), int(xy_dict['y_8'])), (int(xy_dict['x_10']), int(xy_dict['y_10'])), line_color,line_thickness)
    if xy_dict['x_10'] and xy_dict['y_12'] != 0:
        cv2.line(image, (int(xy_dict['x_10']), int(xy_dict['y_10'])), (int(xy_dict['x_12']), int(xy_dict['y_12'])), line_color,line_thickness)
    if xy_dict['x_12'] and xy_dict['y_14'] != 0:
        cv2.line(image, (int(xy_dict['x_12']), int(xy_dict['y_12'])), (int(xy_dict['x_14']), int(xy_dict['y_14'])), line_color,line_thickness)
    if xy_dict['x_17'] and xy_dict['y_19'] != 0:
        cv2.line(image, (int(xy_dict['x_17']), int(xy_dict['y_17'])), (int(xy_dict['x_19']), int(xy_dict['y_19'])), line_color,line_thickness)
    if xy_dict['x_19'] and xy_dict['y_21'] != 0:
        cv2.line(image, (int(xy_dict['x_19']), int(xy_dict['y_19'])), (int(xy_dict['x_21']), int(xy_dict['y_21'])), line_color,line_thickness)
    if xy_dict['x_21'] and xy_dict['y_24'] != 0:
        cv2.line(image, (int(xy_dict['x_21']), int(xy_dict['y_21'])), (int(xy_dict['x_24']), int(xy_dict['y_24'])), line_color,line_thickness)
    if xy_dict['x_21'] and xy_dict['y_25'] != 0:
        cv2.line(image, (int(xy_dict['x_21']), int(xy_dict['y_21'])), (int(xy_dict['x_25']), int(xy_dict['y_25'])), line_color,line_thickness)
    if xy_dict['x_16'] and xy_dict['y_18'] != 0:
        cv2.line(image, (int(xy_dict['x_16']), int(xy_dict['y_16'])), (int(xy_dict['x_18']), int(xy_dict['y_18'])), line_color,line_thickness)
    if xy_dict['x_18'] and xy_dict['y_20'] != 0:
        cv2.line(image, (int(xy_dict['x_18']), int(xy_dict['y_18'])), (int(xy_dict['x_20']), int(xy_dict['y_20'])), line_color,line_thickness)
    if xy_dict['x_20'] and xy_dict['y_22'] != 0:
        cv2.line(image, (int(xy_dict['x_20']), int(xy_dict['y_20'])), (int(xy_dict['x_22']), int(xy_dict['y_22'])), line_color,line_thickness)
    if xy_dict['x_20'] and xy_dict['y_23'] != 0:
        cv2.line(image, (int(xy_dict['x_20']), int(xy_dict['y_20'])), (int(xy_dict['x_23']), int(xy_dict['y_23'])), line_color,line_thickness)
    print("Drawing picture is finished!")

with open(kpjson_file,'r') as load_f:
    load_dict = json.load(load_f)
    for i in range(len(load_dict['annotations'])):
        keypoints = load_dict['annotations'][i]['keypoints']
        image = 'E:\\else\\json\\eval\\zheng\\val\\' + str(load_dict['annotations'][i]['image_id']) +'.jpg'
        image = cv2.imread(image)
        x, y, w, h = load_dict['annotations'][i]['bbox']
        x, y, w, h = int(x), int(y), int(w), int(h)
        cv2.rectangle(image, (x, y), (x + w, y + h), rec_color, rec_thickness)
        if len(keypoints) == 0 :
            i += 1
        elif len(keypoints) != 0 :
            xpoints_list = load_dict['annotations'][i]['keypoints'][::3]
            ypoints_list = load_dict['annotations'][i]['keypoints'][1::3]
            points_list = xpoints_list + ypoints_list
            list_1 = [chr(i) for i in range(120, 122)]
            list_2 = [str(i) for i in range(1,(len(load_dict['annotations'][i]['keypoints'])//3)+1)]
            list = []
            for i in range(len(list_1)):
                x = list_1[i]
                for a in range(len(list_2)):
                    y = list_2[a]
                    list.append(x + '_' + y)
            xy_dict = dict(zip(list, points_list))
            for j in range(len(xpoints_list)):
                cv2.circle(image, (int(xpoints_list[j]), int(ypoints_list[j])), point_size, point_color, cir_thickness)
            draw_line()
        cv2.imshow('img', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
