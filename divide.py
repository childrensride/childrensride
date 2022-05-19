import cv2
import json
import os
file = 'E:\\else\\json\\test\\202204251830450'
point_size = 1
point_color,line_color,rec_color = (0, 0, 255),(0,255,0),(0, 255, 255)
cir_thickness,line_thickness,rec_thickness = 4,1,2



def create_xylist(i):
    list_1 = [chr(i) for i in range(120, 122)]
    list_2 = []
    for a in range(len(load_dict['groups'][i]['keypoints'])):
        list_2.append(str(load_dict['groups'][i]['keypoints'][a]['label']))
    if len(list_2)<25:
        print("请补足25个骨骼点！")
    list = []
    for i in range(len(list_1)):
        x = list_1[i]
        for a in range(len(list_2)):
            y = list_2[a]
            list.append(x + '_' + y)
    return list
def create_pointlist():
    points_list = []
    for a in range(len(load_dict['groups'][i]['keypoints'])):
        points_list.append(load_dict['groups'][i]['keypoints'][a]['points'])
    return points_list

def create_xypointdict(i):
    plist = create_pointlist()
    xylist = create_xylist(i)
    xp_list = []
    yp_list = []
    for h in range(len(plist)):
        x = plist[h][0]
        y = plist[h][1]
        xp_list.append(x)
        yp_list.append(y)
    # print(111, yp_list)
    xp_list.extend(yp_list)
    p_dict = dict(zip(xylist, xp_list))
    # print(222,p_dict)
    return p_dict

def draw_line():
    if 'x_1'and'y_6' in xy_dict:
        cv2.line(image, (int(xy_dict['x_1']), int(xy_dict['y_1'])), (int(xy_dict['x_6']), int(xy_dict['y_6'])), line_color,line_thickness)
    if 'y_7' and 'x_6' in xy_dict:
        cv2.line(image, (int(xy_dict['x_6']), int(xy_dict['y_6'])), (int(xy_dict['x_7']), int(xy_dict['y_7'])), line_color,line_thickness)
    if 'y_1' and 'x_6' in xy_dict:
        cv2.line(image, (int(xy_dict['x_3']), int(xy_dict['y_3'])), (int(xy_dict['x_5']), int(xy_dict['y_5'])), line_color,line_thickness)
    if 'y_3' and 'x_7' in xy_dict:
        cv2.line(image, (int(xy_dict['x_3']), int(xy_dict['y_3'])), (int(xy_dict['x_7']), int(xy_dict['y_7'])), line_color,line_thickness)
    if 'y_2' and 'x_7' in xy_dict:
        cv2.line(image, (int(xy_dict['x_2']), int(xy_dict['y_2'])), (int(xy_dict['x_7']), int(xy_dict['y_7'])), line_color,line_thickness)
    if 'x_2' and 'y_4' in xy_dict:
        cv2.line(image, (int(xy_dict['x_2']), int(xy_dict['y_2'])), (int(xy_dict['x_4']), int(xy_dict['y_4'])), line_color,line_thickness)
    if 'x_9' and 'y_11' in xy_dict:
        cv2.line(image, (int(xy_dict['x_9']), int(xy_dict['y_9'])), (int(xy_dict['x_11']), int(xy_dict['y_11'])), line_color,line_thickness)
    if 'x_11' and 'y_13' in xy_dict:
        cv2.line(image, (int(xy_dict['x_11']), int(xy_dict['y_11'])), (int(xy_dict['x_13']), int(xy_dict['y_13'])), line_color,line_thickness)
    if 'x_13' and 'y_15' in xy_dict:
        cv2.line(image, (int(xy_dict['x_13']), int(xy_dict['y_13'])), (int(xy_dict['x_15']), int(xy_dict['y_15'])), line_color,line_thickness)
    if 'x_8' and 'x_10' in xy_dict:
        cv2.line(image, (int(xy_dict['x_8']), int(xy_dict['y_8'])), (int(xy_dict['x_10']), int(xy_dict['y_10'])), line_color,line_thickness)
    if 'x_10' and 'y_12' in xy_dict:
        cv2.line(image, (int(xy_dict['x_10']), int(xy_dict['y_10'])), (int(xy_dict['x_12']), int(xy_dict['y_12'])), line_color,line_thickness)
    if 'x_12' and 'y_14' in xy_dict:
        cv2.line(image, (int(xy_dict['x_12']), int(xy_dict['y_12'])), (int(xy_dict['x_14']), int(xy_dict['y_14'])), line_color,line_thickness)
    if 'x_19' and 'y_17' in xy_dict:
        cv2.line(image, (int(xy_dict['x_17']), int(xy_dict['y_17'])), (int(xy_dict['x_19']), int(xy_dict['y_19'])), line_color,line_thickness)
    if 'x_19' and 'x_21' in xy_dict:
        cv2.line(image, (int(xy_dict['x_19']), int(xy_dict['y_19'])), (int(xy_dict['x_21']), int(xy_dict['y_21'])), line_color,line_thickness)
    if 'x_21' and 'x_24' in xy_dict:
        cv2.line(image, (int(xy_dict['x_21']), int(xy_dict['y_21'])), (int(xy_dict['x_24']), int(xy_dict['y_24'])), line_color,line_thickness)
    if 'x_21' and 'x_25' in xy_dict:
        cv2.line(image, (int(xy_dict['x_21']), int(xy_dict['y_21'])), (int(xy_dict['x_25']), int(xy_dict['y_25'])), line_color,line_thickness)
    if 'x_16' and 'x_18' in xy_dict:
        cv2.line(image, (int(xy_dict['x_16']), int(xy_dict['y_16'])), (int(xy_dict['x_18']), int(xy_dict['y_18'])), line_color,line_thickness)
    if 'x_18' and 'x_20' in xy_dict:
        cv2.line(image, (int(xy_dict['x_18']), int(xy_dict['y_18'])), (int(xy_dict['x_20']), int(xy_dict['y_20'])), line_color,line_thickness)
    if 'x_20' and 'x_22' in xy_dict:
        cv2.line(image, (int(xy_dict['x_20']), int(xy_dict['y_20'])), (int(xy_dict['x_22']), int(xy_dict['y_22'])), line_color,line_thickness)
    if 'x_20' and 'x_23' in xy_dict:
        cv2.line(image, (int(xy_dict['x_20']), int(xy_dict['y_20'])), (int(xy_dict['x_23']), int(xy_dict['y_23'])), line_color,line_thickness)
    print("Drawing picture is finished!")
for root,dirs,files in os.walk(file):
    for f in files:
        if '.json' in f :
            with open(os.path.join(root,f),'r') as load_f:
                load_dict = json.load(load_f)
                image = root+'\\'+load_dict['imagePath']
                image = cv2.imread(image)
                for i in range(load_dict['groups'][-1]['group_id']):
                    x, y, w, h = load_dict['groups'][i]['bbox']
                    x, y, w, h = int(x), int(y), int(w), int(h)
                    cv2.rectangle(image, (x, y), (x + w, y + h), rec_color, rec_thickness)
                for i in range(load_dict['groups'][-1]['group_id']):
                    keypoints = load_dict['groups'][i]['keypoints']
                    if len(keypoints) ==0:
                        i += 1
                    elif len(keypoints) !=0:
                        xy_point = create_pointlist()
                        xy_dict = create_xypointdict(i)
                        # xy_dict = dict([(k,str(v).replace(" ","")) for k,v in xy_dict.items()])
                        for j in range(len(xy_point)):
                            cv2.circle(image, (int(xy_point[j][0]), int(xy_point[j][1])), point_size, point_color, cir_thickness)
                        # print(f, int(xy_dict['x_15']))
                        draw_line()
                cv2.imshow('img',image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

