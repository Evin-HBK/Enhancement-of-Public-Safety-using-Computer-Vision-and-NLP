# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Color_Tweak_Tool.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Color_Tweaker(object):
    def setupUi(self, Color_Tweaker):
        Color_Tweaker.setObjectName("Color_Tweaker")
        Color_Tweaker.resize(541, 564)
        Color_Tweaker.setStyleSheet("background-color: rgb(64, 62, 62);")
        self.centralwidget = QtWidgets.QWidget(Color_Tweaker)
        self.centralwidget.setObjectName("centralwidget")
        self.Y_Cb_LB = QtWidgets.QGroupBox(self.centralwidget)
        self.Y_Cb_LB.setGeometry(QtCore.QRect(40, 40, 461, 81))
        self.Y_Cb_LB.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.Y_Cb_LB.setObjectName("Y_Cb_LB")
        self.slider_y_cb_lb = QtWidgets.QSlider(self.Y_Cb_LB)
        self.slider_y_cb_lb.setGeometry(QtCore.QRect(20, 50, 421, 20))
        self.slider_y_cb_lb.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.slider_y_cb_lb.setOrientation(QtCore.Qt.Horizontal)
        self.slider_y_cb_lb.setObjectName("slider_y_cb_lb")
        self.label = QtWidgets.QLabel(self.Y_Cb_LB)
        self.label.setGeometry(QtCore.QRect(20, 30, 21, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Y_Cb_LB)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Y_Cb_LB)
        self.label_3.setGeometry(QtCore.QRect(430, 30, 16, 16))
        self.label_3.setObjectName("label_3")
        self.value_y_cb_lb = QtWidgets.QLabel(self.Y_Cb_LB)
        self.value_y_cb_lb.setGeometry(QtCore.QRect(356, 0, 101, 20))
        self.value_y_cb_lb.setObjectName("value_y_cb_lb")
        self.Y_Cb_UB = QtWidgets.QGroupBox(self.centralwidget)
        self.Y_Cb_UB.setGeometry(QtCore.QRect(40, 150, 461, 81))
        self.Y_Cb_UB.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.Y_Cb_UB.setObjectName("Y_Cb_UB")
        self.slider_y_cb_ub = QtWidgets.QSlider(self.Y_Cb_UB)
        self.slider_y_cb_ub.setGeometry(QtCore.QRect(20, 50, 421, 20))
        self.slider_y_cb_ub.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.slider_y_cb_ub.setOrientation(QtCore.Qt.Horizontal)
        self.slider_y_cb_ub.setObjectName("slider_y_cb_ub")
        self.label_5 = QtWidgets.QLabel(self.Y_Cb_UB)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 21, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Y_Cb_UB)
        self.label_6.setGeometry(QtCore.QRect(230, 30, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.Y_Cb_UB)
        self.label_7.setGeometry(QtCore.QRect(430, 30, 16, 16))
        self.label_7.setObjectName("label_7")
        self.value_y_cb_ub = QtWidgets.QLabel(self.Y_Cb_UB)
        self.value_y_cb_ub.setGeometry(QtCore.QRect(356, 0, 101, 20))
        self.value_y_cb_ub.setObjectName("value_y_cb_ub")
        self.Cr_Cb_LB = QtWidgets.QGroupBox(self.centralwidget)
        self.Cr_Cb_LB.setGeometry(QtCore.QRect(40, 260, 461, 81))
        self.Cr_Cb_LB.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.Cr_Cb_LB.setObjectName("Cr_Cb_LB")
        self.slider_cr_cb_lb = QtWidgets.QSlider(self.Cr_Cb_LB)
        self.slider_cr_cb_lb.setGeometry(QtCore.QRect(20, 50, 421, 20))
        self.slider_cr_cb_lb.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.slider_cr_cb_lb.setOrientation(QtCore.Qt.Horizontal)
        self.slider_cr_cb_lb.setObjectName("slider_cr_cb_lb")
        self.label_8 = QtWidgets.QLabel(self.Cr_Cb_LB)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 21, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Cr_Cb_LB)
        self.label_9.setGeometry(QtCore.QRect(230, 30, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Cr_Cb_LB)
        self.label_10.setGeometry(QtCore.QRect(430, 30, 16, 16))
        self.label_10.setObjectName("label_10")
        self.value_cr_cb_lb = QtWidgets.QLabel(self.Cr_Cb_LB)
        self.value_cr_cb_lb.setGeometry(QtCore.QRect(356, 0, 101, 20))
        self.value_cr_cb_lb.setObjectName("value_cr_cb_lb")
        self.Cr_Cb_UB = QtWidgets.QGroupBox(self.centralwidget)
        self.Cr_Cb_UB.setGeometry(QtCore.QRect(40, 370, 461, 81))
        self.Cr_Cb_UB.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.Cr_Cb_UB.setObjectName("Cr_Cb_UB")
        self.slider_cr_cb_ub = QtWidgets.QSlider(self.Cr_Cb_UB)
        self.slider_cr_cb_ub.setGeometry(QtCore.QRect(20, 50, 421, 20))
        self.slider_cr_cb_ub.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.slider_cr_cb_ub.setOrientation(QtCore.Qt.Horizontal)
        self.slider_cr_cb_ub.setObjectName("slider_cr_cb_ub")
        self.label_11 = QtWidgets.QLabel(self.Cr_Cb_UB)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 21, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Cr_Cb_UB)
        self.label_12.setGeometry(QtCore.QRect(230, 30, 16, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Cr_Cb_UB)
        self.label_13.setGeometry(QtCore.QRect(430, 30, 16, 16))
        self.label_13.setObjectName("label_13")
        self.value_cr_cb_ub = QtWidgets.QLabel(self.Cr_Cb_UB)
        self.value_cr_cb_ub.setGeometry(QtCore.QRect(356, 0, 101, 20))
        self.value_cr_cb_ub.setObjectName("value_cr_cb_ub")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 480, 131, 41))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        Color_Tweaker.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Color_Tweaker)
        self.statusbar.setObjectName("statusbar")
        Color_Tweaker.setStatusBar(self.statusbar)

        self.retranslateUi(Color_Tweaker)
        QtCore.QMetaObject.connectSlotsByName(Color_Tweaker)

    def retranslateUi(self, Color_Tweaker):
        _translate = QtCore.QCoreApplication.translate
        Color_Tweaker.setWindowTitle(_translate("Color_Tweaker", "MainWindow"))
        self.Y_Cb_LB.setTitle(_translate("Color_Tweaker", "Y_Cb Lower Bound"))
        self.label.setText(_translate("Color_Tweaker", "-1"))
        self.label_2.setText(_translate("Color_Tweaker", "0"))
        self.label_3.setText(_translate("Color_Tweaker", "1"))
        self.value_y_cb_lb.setText(_translate("Color_Tweaker", "Value  :  -1.00"))
        self.Y_Cb_UB.setTitle(_translate("Color_Tweaker", "Y_Cb Upper Bound"))
        self.label_5.setText(_translate("Color_Tweaker", "-1"))
        self.label_6.setText(_translate("Color_Tweaker", "0"))
        self.label_7.setText(_translate("Color_Tweaker", "1"))
        self.value_y_cb_ub.setText(_translate("Color_Tweaker", "Value  :  -1.00"))
        self.Cr_Cb_LB.setTitle(_translate("Color_Tweaker", "Cr_Cb Lower Bound"))
        self.label_8.setText(_translate("Color_Tweaker", "-1"))
        self.label_9.setText(_translate("Color_Tweaker", "0"))
        self.label_10.setText(_translate("Color_Tweaker", "1"))
        self.value_cr_cb_lb.setText(_translate("Color_Tweaker", "Value  :  -1.00"))
        self.Cr_Cb_UB.setTitle(_translate("Color_Tweaker", "Cr_Cb Upper Bound"))
        self.label_11.setText(_translate("Color_Tweaker", "-1"))
        self.label_12.setText(_translate("Color_Tweaker", "0"))
        self.label_13.setText(_translate("Color_Tweaker", "1"))
        self.value_cr_cb_ub.setText(_translate("Color_Tweaker", "Value  :  -1.00"))
        self.pushButton.setText(_translate("Color_Tweaker", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Color_Tweaker = QtWidgets.QMainWindow()
    ui = Ui_Color_Tweaker()
    ui.setupUi(Color_Tweaker)
    Color_Tweaker.show()
    sys.exit(app.exec_())
