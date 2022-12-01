from PyQt5.QtWidgets import *
from gui import *


class Television(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 1
    MAX_CHANNEL = 3


    def __init__(self,*args, **kwargs):
        self.cpics = ["NoSignal.jpg", "beingSports.jpg", "CN.png", "CNN.jpeg"]

        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.muteButton.clicked.connect(lambda: self.mute())
        self.powerButton.clicked.connect(lambda: self.power())
        self.channelUpButton.clicked.connect(lambda: self.channel_up())
        self.channelDownButton.clicked.connect(lambda: self.channel_down())
        self.volumeDownButton.clicked.connect(lambda: self.volume_down())
        self.volumeUpButton.clicked.connect(lambda: self.volume_up())

        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.channelLabel.setText("1")
        self.volumeLabel.setText("1")
        self.__currentChannel = self.cpics[1]

    def __str__(self):
        if self.__muted == True:
            return f"TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

    def power(self):

        if self.__status == False:
            self.__status = True
            self.ImageLabel.setPixmap(QtGui.QPixmap(self.__currentChannel))
        else:
            self.__status = False
            self.ImageLabel.setPixmap(QtGui.QPixmap("NoSignal.jpg"))




    def mute(self):

        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.volumeLabel.setText(str(0))
            else:
                temp_volume = self.__volume
                self.__muted = False
                self.volumeLabel.setText(str(temp_volume))

    def channel_up(self):
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

            else:
                self.__channel += 1

            self.__currentChannel = self.cpics[self.__channel]
            self.channelLabel.setText(str(self.__channel))
            self.ImageLabel.setPixmap(QtGui.QPixmap(self.__currentChannel))


    def channel_down(self):

        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

            else:
                self.__channel -= 1


            self.__currentChannel = self.cpics[self.__channel]
            self.channelLabel.setText(str(self.__channel))
            self.ImageLabel.setPixmap(QtGui.QPixmap(self.__currentChannel))


    def volume_up(self):
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.volumeLabel.setText(str(self.__volume))
                self.progressBar.setValue(self.__volume)

    def volume_down(self):
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.volumeLabel.setText(str(self.__volume))
                self.progressBar.setValue(self.__volume)


