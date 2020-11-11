# -*- coding: utf-8 -*-
from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt, QPoint)
from PySide2.QtGui import (QBrush, QColor, QFont,
                           QIcon, QPalette, QPixmap)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1473, 764)
        MainWindow.setMinimumSize(QSize(1035, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(66, 73, 90))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        brush = QBrush(QColor(55, 61, 75))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush)
        brush = QBrush(QColor(29, 32, 40))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush)
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(210, 210, 210, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(66, 73, 90))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        brush = QBrush(QColor(55, 61, 75))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        brush = QBrush(QColor(29, 32, 40))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush)
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(210, 210, 210, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(66, 73, 90))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        brush = QBrush(QColor(55, 61, 75))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        brush = QBrush(QColor(29, 32, 40))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush = QBrush(QColor(51, 153, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush)
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(210, 210, 210, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(27, 29, 35, 160);\n"
"    border: 1px solid rgb(40, 40, 40);\n"
"    border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QSize(1035, 720))
        self.centralwidget.setStyleSheet("background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_36 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("/* LINE EDIT */\n"
"QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"    background-image: url(icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(icons/16x16/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(85, 170, 255);    \n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet("background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet("QPushButton {\n"
"    background-image: url(icons/24x24/cil-menu.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_toggle_menu.setText("")
        self.btn_toggle_menu.setObjectName("btn_toggle_menu")
        self.verticalLayout_3.addWidget(self.btn_toggle_menu)
        self.horizontalLayout_3.addWidget(self.frame_toggle)
        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setStyleSheet("background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.frame_top_right.setObjectName("frame_top_right")
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.frame_top_btns.setObjectName("frame_top_btns")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet("background: transparent;\n"
"background-image: url(icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)
        self.frame_icon_top_bar.setObjectName("frame_icon_top_bar")
        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)
        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setLayoutDirection(Qt.LeftToRight)
        self.label_title_bar_top.setStyleSheet("background: transparent;\n"
"")
        self.label_title_bar_top.setObjectName("label_title_bar_top")
        self.horizontalLayout_10.addWidget(self.label_title_bar_top)
        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QFrame(self.frame_top_btns)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_minimize = QPushButton(self.frame_btns_right)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_minimize.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/16x16/cil-window-minimize.png"), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_5.addWidget(self.btn_minimize)
        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_maximize_restore.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("icons/16x16/cil-window-maximize.png"), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)
        self.btn_maximize_restore.setObjectName("btn_maximize_restore")
        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)
        self.btn_close = QPushButton(self.frame_btns_right)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_close.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("icons/16x16/cil-x.png"), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setFlat(False)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_5.addWidget(self.btn_close)
        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_top_btns)
        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setMaximumSize(QSize(16777215, 100))
        self.frame_top_info.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.frame_top_info.setObjectName("frame_top_info")
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_info_1.setFont(font)
        self.label_top_info_1.setStyleSheet("color: #ffffff; ")
        self.label_top_info_1.setObjectName("label_top_info_1")
        self.horizontalLayout_8.addWidget(self.label_top_info_1)
        self.verticalLayout_2.addWidget(self.frame_top_info)
        self.horizontalLayout_3.addWidget(self.frame_top_right)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_center = QFrame(self.frame_main)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QFrame(self.frame_center)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.frame_menus.setObjectName("frame_menus")
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setContentsMargins(0, 0, 0, 0)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName("layout_menus")
        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)
        self.frame_extra_menus = QFrame(self.frame_left_menu)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.frame_extra_menus.setObjectName("frame_extra_menus")
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName("layout_menu_bottom")
        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.frame_content_right.setObjectName("frame_content_right")
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setStyleSheet("background: transparent;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_report = QWidget()
        self.page_report.setObjectName("page_report")
        self.verticalLayout_6 = QVBoxLayout(self.page_report)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QFrame(self.page_report)
        self.frame.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableCornerButton::section{    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::title{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(11)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 3, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 4, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 5, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 6, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 7, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 8, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 9, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(0, 10, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidget.setItem(1, 8, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(4, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(5, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(6, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(7, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(8, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(9, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(10, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.verticalLayout_6.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_report)
        self.page_bill = QWidget()
        self.page_bill.setObjectName("page_bill")
        self.verticalLayout_17 = QVBoxLayout(self.page_bill)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_2 = QFrame(self.page_bill)
        self.frame_2.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label = QLabel(self.frame_4)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_11.addWidget(self.label)
        self.verticalLayout_8.addWidget(self.frame_4)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tableWidget_2 = QTableWidget(self.frame_3)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableCornerButton::section{    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::title{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(11)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(1, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(1, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(2, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(2, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(3, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(3, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(4, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(4, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(5, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(5, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(6, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(6, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(7, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(7, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(8, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(8, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(9, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(9, 1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(10, 0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(10, 1, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.verticalLayout_10.addWidget(self.tableWidget_2)
        self.verticalLayout_8.addWidget(self.frame_3)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_2 = QLabel(self.frame_6)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_12.addWidget(self.label_2)
        self.label_3 = QLabel(self.frame_6)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_12.addWidget(self.label_3)
        self.label_4 = QLabel(self.frame_6)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setMaximumSize(QSize(150, 16777215))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_13.addWidget(self.lineEdit)
        self.lineEdit_6 = QLineEdit(self.frame_9)
        self.lineEdit_6.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_13.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QLineEdit(self.frame_9)
        self.lineEdit_7.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_7.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_13.addWidget(self.lineEdit_7)
        self.horizontalLayout_6.addWidget(self.frame_9)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_6 = QLabel(self.frame_8)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_14.addWidget(self.label_6)
        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_14.addWidget(self.lineEdit_2)
        self.pushButton = QPushButton(self.frame_8)
        font = QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_14.addWidget(self.pushButton)
        self.label_7 = QLabel(self.frame_8)
        font = QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_14.addWidget(self.label_7)
        self.horizontalLayout_6.addWidget(self.frame_8)
        self.horizontalLayout.addWidget(self.frame_7)
        self.verticalLayout_8.addWidget(self.frame_5)
        self.verticalLayout_17.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page_bill)
        self.page = QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_26 = QFrame(self.page)
        self.frame_26.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_23 = QVBoxLayout(self.frame_26)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_26 = QVBoxLayout(self.frame_28)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_5 = QLabel(self.frame_28)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_26.addWidget(self.label_5)
        self.plainTextEdit = QPlainTextEdit(self.frame_28)
        font = QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_26.addWidget(self.plainTextEdit)
        self.label_28 = QLabel(self.frame_28)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_26.addWidget(self.label_28)
        self.plainTextEdit_2 = QPlainTextEdit(self.frame_28)
        font = QFont()
        font.setPointSize(10)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_26.addWidget(self.plainTextEdit_2)
        self.label_29 = QLabel(self.frame_28)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_26.addWidget(self.label_29)
        self.plainTextEdit_3 = QPlainTextEdit(self.frame_28)
        font = QFont()
        font.setPointSize(10)
        self.plainTextEdit_3.setFont(font)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.verticalLayout_26.addWidget(self.plainTextEdit_3)
        self.verticalLayout_23.addWidget(self.frame_28)
        self.gridLayout_2.addWidget(self.frame_26, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout_9.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.frame_content)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout.addWidget(self.frame_center)
        self.verticalLayout_36.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setGeometry(QRect(0, 0, 1473, 26))
        self.menuBar.setStyleSheet("background-color: rgb(27, 29, 35);\n"
"color: #ffffff;")
        self.menuBar.setDefaultUp(True)
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName("action_3")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        MainWindow.setTabOrder(self.btn_maximize_restore, self.btn_close)
        MainWindow.setTabOrder(self.btn_close, self.btn_toggle_menu)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("MainWindow", "Переодичность ТО АТ"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize_restore.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.label_top_info_1.setText(_translate("MainWindow", "Таблица расчетов"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Новый столбец"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Границы интервала"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Середина интервала"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Число отказов"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Относительная частота"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Эмпирическая надежность"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Эмпирическая интенсивность"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Интенсивность отказа"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Вероятность безотказной работы на интервале"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Вероятность отказа на интервале"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Плотность распределения"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "№ интервала"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Границы интервала"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Середина интервала"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Число отказов"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "Относительная частота"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "Эмпирическая надежность"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "Эмпирическая интенсивность"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("MainWindow", "Интенсивность отказов"))
        item = self.tableWidget.item(0, 8)
        item.setText(_translate("MainWindow", "Вероятность безотказной работы на интервале"))
        item = self.tableWidget.item(0, 9)
        item.setText(_translate("MainWindow", "Вероятность отказа на интервале"))
        item = self.tableWidget.item(0, 10)
        item.setText(_translate("MainWindow", "Плотность распределения"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("MainWindow", "10"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Количество запасных агрегатов на интервале"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Новый столбец"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Новый столбец"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(10, 0)
        item.setText(_translate("MainWindow", "Всего:"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "Число контролируемых изделий:"))
        self.label_3.setText(_translate("MainWindow", "Средняя наработка на отказ:"))
        self.label_4.setText(_translate("MainWindow", "Периодичность ТО:"))
        self.label_6.setText(_translate("MainWindow", "Введите количество часов до отказа:"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
        self.label_7.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "Инструкция"))
        self.label_28.setText(_translate("MainWindow", "О программе:"))
        self.label_29.setText(_translate("MainWindow", "Об авторе:"))
        self.action.setText(_translate("MainWindow", "Выход"))
        self.action_2.setText(_translate("MainWindow", "О программе"))
        self.action_3.setText(_translate("MainWindow", "Об авторе"))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
