import sys
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
from PyQt6.QtWidgets import QApplication, QFileDialog

from counting import *
from bayes import *

class App_Display():
    def __init__(self):
        self.screen = Tk()
        self.screen.geometry("1000x500")
        self.screen.title("PHẦN MỀM ĐIỀU TIẾT GIAO THÔNG DỰA TRÊN MỨC ĐỘ KẸT XE")
        self.app = QApplication(sys.argv)

    def file_explore(self):
        fname = QFileDialog.getOpenFileName(None, 'Chọn ảnh', '', 'Image files (*.jpg *.png *.bmp)')
        self.app.quit()
        return fname[0]
        
    def main(self):
        Tk().withdraw()
        HD = Human_Density()                                                
        Bayes = Crowded(HD.database["full"], HD.database["not_full"])

        fname = self.file_explore()
        image_data = HD.run(fname)
        
        final_image = cv2.resize(cv2.vconcat([HD.img, HD.base_img]), (0, 0), fx=0.7, fy=0.7)
        cv2.imshow('So Sánh 2 Ảnh', final_image) 
        self.kq.config(text=f"Kết quả: {Bayes.filterr(image_data)}")


    def display(self, command):
        self.kq = Label(self.screen, text = f"", font=("Times New Roman", 16))
        self.kq.place(x=125, y=290)

        mon = Label(self.screen, text=" Môn học: COMPUTER VISION ".upper(), font=("Times New Roman", 24))
        gv = Label(self.screen, text="Giáo viên hướng dẫn: Nguyễn Văn Thành", font=("Times New Roman", 16))
        hs = Label(self.screen, text="Nhóm thực hiện: Nhóm 2", font=("Times New Roman", 16))
        dt = Label(self.screen, text="ĐỀ TÀI: NHẬN DIỆN KẸT XE TẠI MỘT KHU VỰC ", font=("Times New Roman", 20))
        mon.place(x=300)
        hs.place(x=380, y=110)
        gv.place(x=320, y=75)
        dt.place(x=230, y=40)
        btn = Button(text="Tìm hình ảnh", width=20, height=3, command=command)
        btn.place(x=420, y=185)

        img_import = Image.open(r"picture/fira.png")
        resize = img_import.resize((130, 130))
        img = ImageTk.PhotoImage(resize)
        images = Label(self.screen, image=img)
        images.place(x=10, y=10)

        self.screen.mainloop()

AD = App_Display()
AD.display(AD.main)