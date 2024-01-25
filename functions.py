import cv2


def orig_count_boxes(name):
    name = name.split(".jpg")[0]
    lis = open("/kaggle/input/one-class-pole/valid/labels/" + name + ".txt", "r").readlines()
    return len(lis)


def draw_orig(name):
    name = name.split(".jpg")[0]
    lis = open("/kaggle/input/one-class-pole/valid/labels/" + name + ".txt", "r").readlines()
    if len(lis):
        img = cv2.imread("/kaggle/input/one-class-pole/valid/images/" + name + ".jpg")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        for i in range(len(lis)):
            li = lis[i].split()
            xc, yc, nw, nh = float(li[1]), float(li[2]), float(li[3]), float(li[4])

            h, w = img.shape[0], img.shape[1]

            xc *= w
            yc *= h
            nw *= w
            nh *= h
            top_left = (int(xc - nw/2), int(yc - nh/2))
            bottom_right = (int(xc + nw/2), int(yc + nh/2))

            img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
        return img
    else:
        img = cv2.imread("/kaggle/input/one-class-pole/valid/images/" + name + ".jpg")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img
