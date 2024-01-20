import os
import cv2
from driver import *

class Human_Density():
    def __init__(self):
        self.database = {
            "full"     : r"data\full.txt",
            "not_full" : r"data\not_full.txt"
        }
        self.image_train = {
            "full"     : r"data\full",
            "not_full" : r"data\not_full"
        }
        self.model = {
            "eye_base"    : r"haarcascades\haarcascades\haarcascade_eye.xml",
            "eye_glasses" : r"haarcascades\haarcascades\haarcascade_eye_tree_eyeglasses.xml",
            "body_full"   : r"haarcascades\haarcascades\haarcascade_fullbody.xml",
            "body_upper"  : r"haarcascades\haarcascades\haarcascade_upperbody.xml"
        }

    # nhập vào 1 ảnh rồi lấy thông tin của nó
    def image_input(self, img_dir):
        self.img, self.hwc = img_input(img_dir)
        self.base_img = self.img.copy()
        self.size = self.hwc[0] * self.hwc[1]

    # Đếm số lượng khuôn mặt và tính tỷ lệ diện tích của nó với ảnh tông thể
    def counting(self):
        cropped_imgs = split_image(self.img)

        num_faces = face_area = 0
        for cimg in cropped_imgs:
            model_3, cimg, darea = cascade(cimg, self.model["body_upper"], 1.0079, "#43FF78") #GREEN
            num_faces += len(model_3)
            face_area += sum([w * h for (x, y, w, h) in model_3])
            
        face_area_ratio = face_area / self.size
        return f'{num_faces} - {face_area_ratio}'

    # ghi data train ra database
    def training(self, image_train, database):
        jpg_files = [f for f in os.listdir(image_train) if f.endswith('.jpg')]
        for image in jpg_files:
            self.image_input(rf"{image_train}\{image}")
            data = self.counting()
            with open(database, 'a') as f: f.write(data + "\n")

    # nhận diện ảnh mới
    def run(self, image_dir):
        self.image_input(image_dir)
        return self.counting()

# HD = Human_Density()
# HD.training(HD.image_train["not_full"], HD.database["not_full"])