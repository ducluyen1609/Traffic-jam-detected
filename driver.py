import cv2

# nhập ảnh
def img_input(img):
  img = cv2.imread(img)
  hwc = img.shape
  return img, hwc

# show ảnh không bị chiếm màn hình
def show_img(img_list):
    max_size = 600
    for i,img in enumerate(img_list):
        maxx = max(img.shape[0], img.shape[1])
        if max_size < maxx: 
            scale= min(max_size/maxx, 1)
            img = cv2.resize(img, (int(img.shape[1]*scale), int(img.shape[0]*scale)))
        cv2.imshow(f"{i}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# HEX To RGB
def HRGB(hex_value):
    rgb_value = tuple(int(hex_value[i:i+2], 16) for i in (1, 3, 5))
    return rgb_value

# HEX To BGR
def HBGR(hex_value):
    r, g, b = (int(hex_value[i:i+2], 16) for i in range(1, 7, 2))
    bgr_value = (b, g, r)
    return bgr_value

# Load the cascade
def cascade(img, data, scale, color):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    model = cv2.CascadeClassifier(data).detectMultiScale(gray, scaleFactor=scale)
    for (x, y, w, h) in model: 
        detected_area = img[y:y+h, x:x+w]
        cv2.rectangle(img, (x, y), (x+w, y+h), HBGR(color), 2)
    return model, img, detected_area

# cắt ảnh lớn thành 10 ảnh nhỏ
def split_image(img):
    small_imgs = []
    hwc = img.shape
    cut_size = round((hwc[0]*hwc[1])/10)

    for r in range(0, hwc[0], cut_size):
        for c in range(0, hwc[1], cut_size):
            small_imgs.append(img[r:r+cut_size, c:c+cut_size])

    return small_imgs
