# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
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
        MainWindow.resize(2114, 1636)
        self.actionAdd_heatmap = QAction(MainWindow)
        self.actionAdd_heatmap.setObjectName(u"actionAdd_heatmap")
        self.actionAdd_video = QAction(MainWindow)
        self.actionAdd_video.setObjectName(u"actionAdd_video")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.VideoPlayer = QVideoWidget(self.centralwidget)
        self.VideoPlayer.setObjectName(u"VideoPlayer")
        self.VideoPlayer.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.VideoPlayer.sizePolicy().hasHeightForWidth())
        self.VideoPlayer.setSizePolicy(sizePolicy1)
        self.VideoPlayer.setMaximumSize(QSize(1080, 1920))
        self.VideoPlayer.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_2.addWidget(self.VideoPlayer)

        self.heatmap = QWidget(self.centralwidget)
        self.heatmap.setObjectName(u"heatmap")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.heatmap.sizePolicy().hasHeightForWidth())
        self.heatmap.setSizePolicy(sizePolicy2)
        self.heatmap.setMaximumSize(QSize(1920, 1080))
        self.heatmap.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_2.addWidget(self.heatmap)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ProgressBar = QSlider(self.centralwidget)
        self.ProgressBar.setObjectName(u"ProgressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ProgressBar.sizePolicy().hasHeightForWidth())
        self.ProgressBar.setSizePolicy(sizePolicy3)
        self.ProgressBar.setMaximumSize(QSize(16777215, 400))
        self.ProgressBar.setOrientation(Qt.Horizontal)
        self.ProgressBar.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_3.addWidget(self.ProgressBar)

        self.progressLabel = QLabel(self.centralwidget)
        self.progressLabel.setObjectName(u"progressLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.progressLabel.sizePolicy().hasHeightForWidth())
        self.progressLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.progressLabel)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PlayButton = QPushButton(self.centralwidget)
        self.PlayButton.setObjectName(u"PlayButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.PlayButton.sizePolicy().hasHeightForWidth())
        self.PlayButton.setSizePolicy(sizePolicy5)
        self.PlayButton.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout.addWidget(self.PlayButton)

        self.StopButton = QPushButton(self.centralwidget)
        self.StopButton.setObjectName(u"StopButton")
        sizePolicy5.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy5)
        self.StopButton.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout.addWidget(self.StopButton)

        self.PauseButton = QPushButton(self.centralwidget)
        self.PauseButton.setObjectName(u"PauseButton")
        sizePolicy5.setHeightForWidth(self.PauseButton.sizePolicy().hasHeightForWidth())
        self.PauseButton.setSizePolicy(sizePolicy5)
        self.PauseButton.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout.addWidget(self.PauseButton)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stabilityLabel = QLabel(self.centralwidget)
        self.stabilityLabel.setObjectName(u"stabilityLabel")
        sizePolicy5.setHeightForWidth(self.stabilityLabel.sizePolicy().hasHeightForWidth())
        self.stabilityLabel.setSizePolicy(sizePolicy5)

        self.verticalLayout.addWidget(self.stabilityLabel)

        self.poseLabel = QLabel(self.centralwidget)
        self.poseLabel.setObjectName(u"poseLabel")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.poseLabel.sizePolicy().hasHeightForWidth())
        self.poseLabel.setSizePolicy(sizePolicy6)

        self.verticalLayout.addWidget(self.poseLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2114, 39))
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
        self.progressLabel.setText(QCoreApplication.translate("MainWindow", u"0:0:0/0:0:0", None))
        self.PlayButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.StopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.PauseButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.stabilityLabel.setText(QCoreApplication.translate("MainWindow", u"stability", None))
        self.poseLabel.setText(QCoreApplication.translate("MainWindow", u"pose", None))
        self.menuAdd_video.setTitle(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi
