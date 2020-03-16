import GUI
import heatMapCreator as hmc
from PySide2 import QtWidgets, QtCore
from PySide2 import QtMultimedia as Media
from PySide2.QtGui import QPixmap
import os
import glob


class App(GUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)

        self.mediaPlayer = Media.QMediaPlayer(None, Media.QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.VideoPlayer)
        self.pathToFile = None
        self.pathToCSV = None
        self.pausedPosition = 0
        self.currentVideoDuration = 0
        self.heatMapIndex = 0
        self.mediaControl = Media.QMediaControl(self.mediaPlayer)

        self.PlayButton.clicked.connect(self.play)
        self.PauseButton.clicked.connect(self.pause)
        self.StopButton.clicked.connect(self.stop)
        self.actionAdd_video.triggered.connect(self.addVideo)
        self.actionAdd_heatmap.triggered.connect(self.addHeatMap)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.error.connect(self.handleError)

        self.ProgressBar.sliderMoved.connect(self.progressChange)
        self.ProgressBar.sliderReleased.connect(self.progressBarValueChange)


    def progressChange(self):
        pass

    def progressBarValueChange(self):
        newPos = self.ProgressBar.value()
        self.mediaPlayer.setPosition(newPos)
        if self.mediaPlayer.state() == Media.QMediaPlayer.PausedState:
            self.pausedPosition = newPos

    def changeHeatMapdisplay(self):
        hmc.plot_pressure(self.df, self.heatMapIndex)
        self.heatMap.setPixmap(QPixmap("pics/HM{index}.svg".format(index=self.heatMapIndex)))

    def generateDF(self):
        self.df = hmc.createDF(self.pathToCSV)

    def positionChanged(self, position):
        self.ProgressBar.setValue(position)
        absSec = int(position/1000)
        posSec = absSec
        posMin = 0
        posH = 0
        if posSec >= 60:
            posMin = int(posSec/60)
            posSec = posSec % 60
        if posMin >= 60:
            posH = int(posMin/60)
            posMin = posMin % 60

        durSec = int(self.currentVideoDuration/1000)
        durMin = 0
        durH = 0
        if durSec >= 60:
            durMin = int(durSec/60)
            durSec = durSec % 60
        if durMin >= 60:
            durH = int(durMin/60)
            durMin = durMin % 60
        self.progressLabel.setText("{posH}:{posMin}:{posSec}/{durH}:{durMin}:{durSec}".
                                   format(posH=posH, posMin=posMin, posSec=posSec, durH=durH, durMin=durMin, durSec=durSec))
        self.heatMapIndex = absSec
        self.changeHeatMapdisplay()

        if position == self.currentVideoDuration:
            for i in range(0,absSec+1):
                os.remove("pics/HM{index}.svg".format(index=i))

    def durationChanged(self, duration):
        self.ProgressBar.setRange(0, duration)
        self.currentVideoDuration = duration

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())


    def tr(self,text):
        return QtCore.QObject.tr(self, text)

    def addVideo(self):
        self.pathToFile = QtWidgets.QFileDialog.getOpenFileName(self,self.tr("Choose Video file"), self.tr("~/Desktop/"), self.tr("Videos (*.mp4)"))[0]


    def play(self):
        if self.pathToCSV is None:
            self.addHeatMap()

        if self.pathToFile is None:
            self.addVideo()
            self.video = Media.QMediaContent(QtCore.QUrl.fromLocalFile(self.pathToFile))
            self.mediaPlayer.setMedia(self.video)

        else:
            self.video = Media.QMediaContent(QtCore.QUrl.fromLocalFile(self.pathToFile))
            self.mediaPlayer.setMedia(self.video)

        self.mediaPlayer.setPosition(self.pausedPosition)
        self.mediaPlayer.play()

    def pause(self):
        self.mediaPlayer.pause()
        self.pausedPosition = self.mediaPlayer.position()

    def stop(self):
        self.mediaPlayer.stop()
        self.pausedPosition = 0
        self.positionChanged(0)

    def addHeatMap(self):
        self.pathToCSV = QtWidgets.QFileDialog.getOpenFileName(self,self.tr("Choose a csv file"), self.tr("~/Desktop/"), self.tr("CSV (*.csv)"))[0]
        self.generateDF()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qtApp = App()
    qtApp.show()
    quit = app.exec_()
    if quit == 0:
        for x in list(glob.glob("pics/*.svg")):
            os.remove(x)
