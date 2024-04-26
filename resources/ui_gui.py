# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiIlGfLV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.upper_frame = QFrame(self.main_frame)
        self.upper_frame.setObjectName(u"upper_frame")
        self.upper_frame.setMinimumSize(QSize(0, 70))
        self.upper_frame.setMaximumSize(QSize(16777215, 70))
        self.upper_frame.setFrameShape(QFrame.StyledPanel)
        self.upper_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.upper_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.action_config_btn = QPushButton(self.upper_frame)
        self.action_config_btn.setObjectName(u"action_config_btn")
        self.action_config_btn.setMaximumSize(QSize(30, 16777215))
        self.action_config_btn.setCursor(QCursor(Qt.UpArrowCursor))

        self.horizontalLayout_2.addWidget(self.action_config_btn)

        self.heading_lbl = QLabel(self.upper_frame)
        self.heading_lbl.setObjectName(u"heading_lbl")
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(16)
        self.heading_lbl.setFont(font)
        self.heading_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.heading_lbl)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.upper_frame)

        self.lower_frame = QFrame(self.main_frame)
        self.lower_frame.setObjectName(u"lower_frame")
        self.lower_frame.setFrameShape(QFrame.StyledPanel)
        self.lower_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.lower_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.lower_frame)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(250, 0))
        self.left_frame.setMaximumSize(QSize(250, 16777215))
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.left_frame)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.snapshot_btn = QPushButton(self.left_frame)
        self.snapshot_btn.setObjectName(u"snapshot_btn")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(12)
        self.snapshot_btn.setFont(font1)
        self.snapshot_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.snapshot_btn)

        self.start_stop_btn = QPushButton(self.left_frame)
        self.start_stop_btn.setObjectName(u"start_stop_btn")
        self.start_stop_btn.setFont(font1)
        self.start_stop_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.start_stop_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.left_frame)

        self.mid_fram = QFrame(self.lower_frame)
        self.mid_fram.setObjectName(u"mid_fram")
        self.mid_fram.setFrameShape(QFrame.StyledPanel)
        self.mid_fram.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mid_fram)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.display_lbl = QLabel(self.mid_fram)
        self.display_lbl.setObjectName(u"display_lbl")
        self.display_lbl.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.display_lbl)

        self.video_source_btn = QPushButton(self.mid_fram)
        self.video_source_btn.setObjectName(u"video_source_btn")
        self.video_source_btn.setFont(font1)
        self.video_source_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.video_source_btn)


        self.horizontalLayout.addWidget(self.mid_fram)

        self.right_frame = QFrame(self.lower_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(250, 0))
        self.right_frame.setMaximumSize(QSize(250, 16777215))
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.right_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.listWidget = QListWidget(self.right_frame)
        self.listWidget.setObjectName(u"listWidget")
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(11)
        self.listWidget.setFont(font2)

        self.verticalLayout_5.addWidget(self.listWidget)


        self.horizontalLayout.addWidget(self.right_frame)


        self.verticalLayout_2.addWidget(self.lower_frame)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_config_btn.setText("")
        self.heading_lbl.setText(QCoreApplication.translate("MainWindow", u"Cow monitoring", None))
        self.snapshot_btn.setText(QCoreApplication.translate("MainWindow", u"Snapshot", None))
        self.start_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.display_lbl.setText("")
        self.video_source_btn.setText(QCoreApplication.translate("MainWindow", u"Video source", None))
    # retranslateUi

