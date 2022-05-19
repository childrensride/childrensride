import os
import json
import cv2
from shutil import copyfile

def json_open(file):
    jsonfilenames = []
    for root, dirs, files in os.walk(file):
        for f in files:
            if '.json' in f:
                count = 0
                a = -1
                with open(os.path.join(root, f), 'r') as load_f:
                    load_dict = json.load(load_f)
                    for group in load_dict['groups']:
                        a +=1
                        if group['class'] == 1:
                            b = a
                            count += 1
                        else:
                            pass
                if count == 0:
                    pass
                if count == 1:
                    with open(os.path.join(root, f), 'r') as edit_f:
                        edit_dict = json.load(edit_f)
                        edit_dict['groups'][b]['class'] = 8
                        with open(os.path.join(root,f),'w') as finish_f:
                            json.dump(edit_dict,finish_f)
                if count >= 2:
                    jsonfilenames.append(f)
                    open(os.path.join(root, f), 'r').close()
                    # image = cv2.imread(root+'\\'+load_dict['imagePath'])
                    # for i in range(len(load_dict['groups'])):
                    #     x, y, w, h = load_dict['groups'][i]['bbox']
                    #     x, y, w, h = int(x), int(y), int(w), int(h)
                    #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), thickness=1)
                    #     cv2.imwrite('E:\\else\\json\\picture\\{}{}.jpg'.format(f[:-5]+'_',i), image)
                        # img = cv2.imread('E:\\else\\json\\picture\\' + str_num + '.jpg')
                        # cv2.imshow('people', img)
                        # wait = cv2.waitKey(0)
                        # print(wait)
                        # cv2.destroyAllWindows()
                    copyfile(root+'\\'+f,destination_file+'\\'+f)
                    copyfile(root+'\\'+load_dict['imagePath'],destination_file+'\\'+load_dict['imagePath'])
                    if os.path.exists(root+'\\'+f):
                        os.remove(root+'\\'+f)
                        os.remove(root+'\\'+load_dict['imagePath'])
                    else:
                        print("The file does not exist")
    return jsonfilenames


if __name__ == '__main__':
    file = "E:\\else\\json\\test\\202204281702171"
    destination_file = "E:\\else\\json\\multi_people\\202204281702171"
    print(json_open(file))
