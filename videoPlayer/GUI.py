# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WinGUI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from PySide2.QtMultimediaWidgets import QVideoWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 800))
        self.actionAdd_heatmap = QAction(MainWindow)
        self.actionAdd_heatmap.setObjectName(u"actionAdd_heatmap")
        self.actionAdd_video = QAction(MainWindow)
        self.actionAdd_video.setObjectName(u"actionAdd_video")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(400, 300))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.VideoPlayer = QVideoWidget(self.frame)
        self.VideoPlayer.setObjectName(u"VideoPlayer")
        sizePolicy.setHeightForWidth(self.VideoPlayer.sizePolicy().hasHeightForWidth())
        self.VideoPlayer.setSizePolicy(sizePolicy)
        self.VideoPlayer.setMinimumSize(QSize(400, 300))
        self.VideoPlayer.setFocusPolicy(Qt.NoFocus)
        self.VideoPlayer.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_2.addWidget(self.VideoPlayer)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(400, 300))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.heatMap = QLabel(self.frame_2)
        self.heatMap.setObjectName(u"heatMap")
        sizePolicy.setHeightForWidth(self.heatMap.sizePolicy().hasHeightForWidth())
        self.heatMap.setSizePolicy(sizePolicy)
        self.heatMap.setMinimumSize(QSize(400, 300))
        self.heatMap.setLayoutDirection(Qt.LeftToRight)
        self.heatMap.setScaledContents(True)
        self.heatMap.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.heatMap, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ProgressBar = QSlider(self.frame_3)
        self.ProgressBar.setObjectName(u"ProgressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ProgressBar.sizePolicy().hasHeightForWidth())
        self.ProgressBar.setSizePolicy(sizePolicy1)
        self.ProgressBar.setMinimumSize(QSize(0, 0))
        self.ProgressBar.setMaximumSize(QSize(16777215, 400))
        self.ProgressBar.setOrientation(Qt.Horizontal)
        self.ProgressBar.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout.addWidget(self.ProgressBar)

        self.progressLabel = QLabel(self.frame_3)
        self.progressLabel.setObjectName(u"progressLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressLabel.sizePolicy().hasHeightForWidth())
        self.progressLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.progressLabel)


        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PlayButton = QPushButton(self.frame_3)
        self.PlayButton.setObjectName(u"PlayButton")
        sizePolicy1.setHeightForWidth(self.PlayButton.sizePolicy().hasHeightForWidth())
        self.PlayButton.setSizePolicy(sizePolicy1)
        self.PlayButton.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_2.addWidget(self.PlayButton)

        self.StopButton = QPushButton(self.frame_3)
        self.StopButton.setObjectName(u"StopButton")
        sizePolicy1.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy1)
        self.StopButton.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_2.addWidget(self.StopButton)

        self.PauseButton = QPushButton(self.frame_3)
        self.PauseButton.setObjectName(u"PauseButton")
        sizePolicy1.setHeightForWidth(self.PauseButton.sizePolicy().hasHeightForWidth())
        self.PauseButton.setSizePolicy(sizePolicy1)
        self.PauseButton.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_2.addWidget(self.PauseButton)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stabilityLabel = QLabel(self.frame_3)
        self.stabilityLabel.setObjectName(u"stabilityLabel")
        sizePolicy1.setHeightForWidth(self.stabilityLabel.sizePolicy().hasHeightForWidth())
        self.stabilityLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.stabilityLabel)

        self.poseLabel = QLabel(self.frame_3)
        self.poseLabel.setObjectName(u"poseLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.poseLabel.sizePolicy().hasHeightForWidth())
        self.poseLabel.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.poseLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 39))
        self.menuAdd_video = QMenu(self.menubar)
        self.menuAdd_video.setObjectName(u"menuAdd_video")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAdd_video.menuAction())
        self.menuAdd_video.addAction(self.actionAdd_heatmap)
        self.menuAdd_video.addAction(self.actionAdd_video)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_heatmap.setText(QCoreApplication.translate("MainWindow", u"Add heatmap", None))
        self.actionAdd_video.setText(QCoreApplication.translate("MainWindow", u"Add video", None))
        self.heatMap.setText("")
        self.progressLabel.setText(QCoreApplication.translate("MainWindow", u"0:0:0/0:0:0", None))
        self.PlayButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.StopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.PauseButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.stabilityLabel.setText(QCoreApplication.translate("MainWindow", u"stability", None))
        self.poseLabel.setText(QCoreApplication.translate("MainWindow", u"pose", None))
        self.menuAdd_video.setTitle(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

