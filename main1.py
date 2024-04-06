#створи тут фоторедактор Easy Editor!
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageColor
from main import Ui_MainWindow
import os

class ImageEditor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.original = None
        self.workdir = ""
        self.ui.btn_folder.clicked.connect(self.show_files)
        self.ui.list_files.clicked.connect(self.clicks)
        self.ui.btn_B_W.clicked.connect(self.bw_filter)
        self.ui.btn_doleft.clicked.connect(self.left_filter)
        self.ui.btn_doright.clicked.connect(self.right_filter)
        self.ui.btn_mirror.clicked.connect(self.mirror_filter)
        self.ui.btn_sharp.clicked.connect(self.sharpen_filter)
        self.ui.btn_blur.clicked.connect(self.blur_filter)
        self.ui.btn_contrast.clicked.connect(self.contrast_filter)
        self.ui.btn_smooth.clicked.connect(self.smooth_filter)
        self.ui.btn_path.clicked.connect(self.outline)
        # self.ui.btn_green.clicked.connect(self.green)
        self.ui.btn_save.clicked.connect(self.to_save)
        self.ui.btn_enchamnet.clicked.connect(self.enchantment)
        self.ui.btn_boundaries.clicked.connect(self.borders)
        self.ui.btn_relief.clicked.connect(self.relief)
        self.ui.btn_brightness.clicked.connect(self.brightness_filter)
        self.ui.btn_saturation.clicked.connect(self.saturation_filter)
        self.ui.btn_detal.clicked.connect(self.detail_filter)
        self.ui.btn_invert.clicked.connect(self.invert_filter)

        self.ui.sl_1red.valueChanged.connect(self.update_color)
        self.ui.sl_2green.valueChanged.connect(self.update_color)
        self.ui.sl_3blue.valueChanged.connect(self.update_color)


        
        
        

    def sort_files(self, files):
        exentions = [".jpg", ".png", ".bmp", ".jpeg"]
        result = []
        for file in files:
            for ex in exentions:
                if file.endswith(ex):
                    result.append(file)
            return result
    def open(self):
        self.workdir = QtWidgets.QFileDialog.getExistingDirectory()

    def show_files(self):
        self.open()
        if self.workdir:  # Check if workdir is not empty
            filename = os.listdir(self.workdir)
            filename = self.sort_files(filename)
            self.ui.list_files.clear()
            for filee in filename:
                self.ui.list_files.addItem(filee)
        else:
            print("Error: No directory selected.")


    def load_image(self, file_name):
        self.path = os.path.join(self.workdir,file_name)
        self.original = Image.open(self.path)

    def show_image(self):
        photo = QtGui.QPixmap(self.path)
        w, h = self.ui.image.width(), self.ui.image.height()
        photo = photo.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.ui.image.setPixmap(photo)

    def clicks(self):
        if self.ui.list_files.currentRow() >= 0:
            file = self.ui.list_files.currentItem().text()
            self.load_image(file)
            self.show_image()

    def save_image(self):
        self.path = os.path.join(self.workdir, "new_image.jpg")
        self.original.save(self.path)
        
    def to_save(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        name,ok = QtWidgets.QInputDialog.getText( "Збереження", "Назвіть свій файл")
        if ok == True and name != '': 
            name = name+".png"
            new_path = os.path.join(path, name)
            self.original.save(new_path)
            print(new_path)
    

    def bw_filter(self):
        if self.original:
            self.original = self.original.convert("L")
            self.save_image()
            self.show_image()
    def left_filter(self):
        if self.original:
            self.original = self.original.rotate(90)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()
    def right_filter(self):
        if self.original:
            self.original = self.original.rotate(-90)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()
    def mirror_filter(self):
        if self.original:
            self.original = self.original.transpose(Image.FLIP_LEFT_RIGHT)
            self.save_image()
            self.show_image()
    def sharpen_filter(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.SHARPEN)
            self.save_image()
            self.show_image()
    def blur_filter(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.BLUR)
            self.save_image()
            self.show_image()
    def contrast_filter(self):
        if self.original:
            self.original = ImageEnhance.Contrast(self.original)
            self.original = self.original.enhance(1.5)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()
    def smooth_filter(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.SMOOTH)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()
    # def green(self):
    #     if self.original:
    #         green = self.original.split()
    #         zeroed_band = green[1].point(lambda _: 0)
    #         self.original = Image.merge("RGB", (zeroed_band, green[1], zeroed_band))
    #         self.save_image()
    #         self.show_image()
    def outline(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.CONTOUR)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()
    def enchantment(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.EDGE_ENHANCE)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()
    def borders(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.SMOOTH)
            self.original = self.original.filter(ImageFilter.FIND_EDGES)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()
    def relief(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.EMBOSS)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()

    def brightness_filter(self):
        if self.original:
            enhancer = ImageEnhance.Brightness(self.original)
            self.original = enhancer.enhance(1.5)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()

    def saturation_filter(self):
        if self.original:
            enhancer = ImageEnhance.Color(self.original)
            self.original = enhancer.enhance(2.0)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()

    def detail_filter(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.DETAIL)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image() 
    
    def invert_filter(self):
        try:
            if self.original:
                self.original = ImageOps.invert(self.original)
                self.original = self.original.convert('RGB')
                self.save_image()
                self.show_image()
        except IOError:
            print("Формат зображення не підтримується.")

    def update_color(self):
        if self.original:
            r = self.ui.sl_1red.value() if self.ui.sl_1red.value() != 255 else 255
            g = self.ui.sl_2green.value() if self.ui.sl_2green.value() != 255 else 255
            b = self.ui.sl_3blue.value() if self.ui.sl_3blue.value() != 255 else 255
            self.original = self.original.convert('RGB')
            data = list(self.original.getdata())
            new_data = [(r if red == 255 else red, g if green == 255 else green, b if blue == 255 else blue) for (red, green, blue) in data]
            self.original.putdata(new_data)
            self.save_image()
            self.show_image()



            
app = QtWidgets.QApplication([])
win = ImageEditor()
win.show()
app.exec()
