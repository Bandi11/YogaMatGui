import GUI
from PySide2 import QtWidgets, QtCore
from PySide2 import QtMultimedia as Media


class App(GUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)

        self.mediaPlayer = Media.QMediaPlayer(None, Media.QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.VideoPlayer)
        self.pathToFile = None
        self.pausedPosition = 0
        self.currentVideoDuration = 0
        self.mediaControl = Media.QMediaControl(self.mediaPlayer)

        self.PlayButton.clicked.connect(self.play)
        self.PauseButton.clicked.connect(self.pause)
        self.StopButton.clicked.connect(self.stop)
        self.actionAdd_video.triggered.connect(self.addVideo)
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

    def positionChanged(self, position):
        self.ProgressBar.setValue(position)
        posSec = int(position/1000)
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
                                   format(posH=posH,posMin=posMin, posSec=posSec, durH=durH,durMin=durMin, durSec=durSec))
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


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qtApp = App()
    qtApp.show()
    app.exec_()