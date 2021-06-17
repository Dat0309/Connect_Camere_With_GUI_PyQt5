import sys
import cv2 as cv
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import resource

class UI_Dialog(QDialog):
    def __init__(self):
        super(UI_Dialog, self).__init__()

        loadUi("tutol.ui", self)

        self.logic = 0
        self.value = 1

        self.showBtn.clicked.connect(self.onClicked)

        self.CaptureBtn.clicked.connect(self.CaptureClicked)


    @pyqtSlot()
    def onClicked(self):
        cap = cv.VideoCapture(0)

        while (cap.isOpened()): 
            ret, frame = cap.read()
            if ret == True:
                #print("Here")
                self.displayImage(frame, 1)
                
                if cv.waitKey(20) & 0xFF == ord('q'):
                    break

                if(self.logic==2):

                    self.value = self.value + 1
                    #path = r'D:\TỰ HỌC\Face-Recogntion-PyQt\Face_Detection_PyQt_base\ImagesAttendance\%s.png'%(self.value)
                    cv.imwrite('%s.png'%(self.value),frame)

                    self.logic = 1


            else:
                print("return not found")
        cap.release()
        cv.destroyAllWindows()

    def CaptureClicked(self):
        self.logic = 2

    def exitClicked(self):
        self.logic = 3

    def displayImage(self, img, window = 1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) ==3:
            if (img.shape[2]) ==4:
                qformat = QImage.Format_RGBA888

            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.label.setPixmap(QPixmap.fromImage(img))
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI_Dialog()
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        print('Exiting')

