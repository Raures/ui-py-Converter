from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import os

savePath = ""
settingsFilePath = Path("settings.txt")

if not settingsFilePath.is_file():

    # If the "settings.txt" file does not exist it will be created
    # with the default *.ui file saving path set to user's Destop.
    
    f = open("settings.txt", "w")
    savePath = os.environ["HOMEPATH"] + "\\Desktop\\"
    f.write(savePath)
    f.close()
else:
    
    # If the "settings.txt" exists it will be read to pick the
    # *.ui file saving path that has been set by the user.
    
    f = open("settings.txt", "r")
    savePath = f.readline()
    f.close()

def convertToPy(target):

    # This function runs a command prompt command using 'pyuic5'
    # to convert the *.ui file to a *.py file.
    
    os.system('pyuic5 -o "' + savePath + '/convertedfile.py" "' + target + '"')

class Label(QtWidgets.QLabel):

    # This is a custom label created to be able to drag-and-drop
    # the *.ui file.
    
    def __init__(self):
        super(Label, self).__init__()

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("text/uri-list"):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        convertToPy(e.mimeData().text()[8:])

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.windowTitle = "ui/py Converter"
        self.windowSize = (438, 348)

        self.setupUi(self)

    def setupUi(self, Form):

        # Main Window:
        Form.setWindowTitle(self.windowTitle)
        Form.resize(self.windowSize[0], self.windowSize[1])

        # Fonts:
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        
        # Frames:
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        
        # Labels: 
        self.labelInfo = QtWidgets.QLabel(self.frame)
        self.labelInfo.setWordWrap(True)
        self.labelInfo.setText("Before converting, please make sure that you have PyQt5 installed. To install PyQt5, you can visit <a href='https://sourceforge.net/projects/pyqt/'>this link</a> to download it, or run the following command in <b>cmd</b>: <font face='Consolas'>pip3 install PyQt5</font>")
        self.labelInfo.setOpenExternalLinks(True)

        self.labelTarget = Label()
        self.labelTarget.setFont(font)
        self.labelTarget.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTarget.setText("Drag and drop the <b>user interface</b> (<b>*.ui</b>) file here")
        self.labelTarget.setStyleSheet("QLabel { border: 1px dotted black; }")
        self.labelTarget.setMinimumHeight(150)
        self.labelTarget.setAcceptDrops(True)

        self.labelQuestion = QtWidgets.QLabel(self.frame_3)
        self.labelQuestion.setText("Where should the <b>python</b> file be saved?")

        # LineEdit:
        self.inputDirectory = QtWidgets.QLineEdit(self.frame_4)
        self.inputDirectory.setText(savePath)
        self.inputDirectory.setStyleSheet("QLineEdit { padding-bottom: 2px; padding-left: 2px; }")

        # Buttons:
        self.buttonBrowse = QtWidgets.QPushButton(self.frame_4)
        self.buttonBrowse.setText("Browse")

        # Layouts:
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.horizontalLayout.addWidget(self.labelInfo)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()

        self.verticalLayout_5.addWidget(self.labelTarget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout.addWidget(self.frame_2)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()

        self.verticalLayout_3.addWidget(self.labelQuestion)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)

        self.horizontalLayout_5.addWidget(self.inputDirectory)

        self.horizontalLayout_5.addWidget(self.buttonBrowse)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        # --- 

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.buttonBrowse.clicked.connect(self.browsePath)

    def browsePath(self):

        # This method allows the user to select where to place
        # the *.py file once it's converted. The path is then
        # saved in the "settings.txt" file to be used in the
        # future.
        
        savePath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select directory"))
        self.inputDirectory.setText(savePath)
        with open(settingsFilePath, "w") as f:
            f.write(savePath)

if __name__ == "__main__":

    # The main program.
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hGUI = QtWidgets.QWidget()
    ui = MainWindow()
    ui.setupUi(hGUI)
    hGUI.show()
    sys.exit(app.exec_())
