from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import os
import sys

# Variable that holds the path where the .py file will be placed
savePath = ""

# Variable that holds the path/name of the settings file
settingsFilePath = Path("settings.txt")

# Check if settingsFilePath is present
if not settingsFilePath.is_file():
    
    # If it isn't, create it
    f = open("settings.txt", "w")

    # Set the savePath to default
    savePath = os.environ["HOMEPATH"] + "\\Desktop\\"
    f.write(savePath)
    
    # Very important to close opened files
    f.close()
else:
    
    # If it is, open it for reading
    f = open("settings.txt", "r")

    # Read the savePath from settingsFilePath
    savePath = f.readline()
    
    # Very important to close opened files
    f.close()

def convertToPy(target):
    """ Function that calls a command in cmd and converts .ui to .py
        Link for more info on commands:
        https://doc.bccnsoft.com/docs/PyQt5/designer.html#pyuic5
    """

    # Get the file name of target
    filename = os.path.basename(target[:-3])
    
    # Use os module to call pyuic5 and convert the file
    os.system("pyuic5 -o {}/{}.py {}".format(savePath, filename, target))

class DragAndDropLabel(QtWidgets.QLabel):
    """ Custom QLabel that accepts drag-and-drop files """
    def __init__(self):
        super(DragAndDropLabel, self).__init__()

        self.setAcceptDrops(True)
        
    # Register file drag event
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("text/uri-list"):
            e.accept()
        else:
            e.ignore()
            
    # Register file drop event
    def dropEvent(self, e):
        # Call the function to convert the file
        convertToPy(e.mimeData().text()[8:])

class MainWindow(QtWidgets.QWidget):
    """ The MainWindow that holds all the controls """
    def __init__(self):
        super().__init__()
        
        # Set MainWindow configuration
        self.windowTitle = "Converter: User Interface to Python"
        self.windowSize = (440, 350)

        # Set ./Frame 1/labelInfo download link and text
        self.linkPyQt = "https://sourceforge.net/projects/pyqt/"
        self.textLabelInfo = """Before converting, please make sure that you have PyQt5 installed. To install PyQt5, you can visit <a href='{}'>this link</a>
                                to download it, or run the following command in <b>cmd</b>: <font face='Consolas'>pip3 install PyQt5</font>""".format(self.linkPyQt)
        
        # Set ./Frame 2/labelTarget text, style and font
        self.textLabelDragAndDrop = "Drag and drop the <b>user interface</b> (<b>*.ui</b>) file here"
        self.styleLabelDragAndDrop = "QLabel { border: 1px dotted black; }"
        self.fontLabelDragAndDrop = "Myanmar Text"
        
        # Set ./Frame 3/labelQuestion text
        self.textLabelQuestion = "Where should the <b>python</b> file be saved at?"

        # Set ./Frame 4/inputDirectory style
        self.styleLineEdit = "QLineEdit { padding-bottom: 2px; padding-left: 2px; }"

        # Set ./Frame 4/buttonBrowse text
        self.textBrowseButton = "Browse"

    def setupUi(self):
        
        # Set the Window Title and Window Size
        self.setWindowTitle(self.windowTitle)
        self.resize(self.windowSize[0], self.windowSize[1])

        # Create a Frame 1 to hold the Label with instructions
        self.frame_1 = QtWidgets.QFrame(self)
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)

        # Create a Label on Frame 1 to hold the instructions
        self.labelInfo = QtWidgets.QLabel(self.frame_1)
        self.labelInfo.setWordWrap(True)
        self.labelInfo.setText(self.textLabelInfo)
        self.labelInfo.setOpenExternalLinks(True)

        # Create a Frame 2 to hold DragAndDropLabel
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        
        # Create a Label that accepts files by drag-and-drop (see DragAndDropLabel above)
        self.labelTarget = DragAndDropLabel()
        self.labelTarget.setFont(QtGui.QFont(self.fontLabelDragAndDrop))
        self.labelTarget.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTarget.setText(self.textLabelDragAndDrop)
        self.labelTarget.setStyleSheet(self.styleLabelDragAndDrop)
        self.labelTarget.setMinimumHeight(150)
        self.labelTarget.setAcceptDrops(True)

        # Create a Frame 3 to hold Label with information about the path
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        
        # Create a Label in Frame 3 with information about the path
        self.labelQuestion = QtWidgets.QLabel(self.frame_3)
        self.labelQuestion.setText(self.textLabelQuestion)

        # Create a Frame 4 to hold LineEdit and PushButton
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        
        # Create a LineEdit in Frame 4 that shows the saving path
        self.inputDirectory = QtWidgets.QLineEdit(self.frame_4)
        self.inputDirectory.setText(savePath)
        self.inputDirectory.setStyleSheet(self.styleLineEdit)
        
        # Create a PushButton in Frame 4 to browse the saving path
        self.buttonBrowse = QtWidgets.QPushButton(self.frame_4)
        self.buttonBrowse.setText(self.textBrowseButton)
        
        # Create & Set Vertical Layouts 
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.addWidget(self.frame_1)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_3)
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.addWidget(self.labelQuestion)
        self.verticalLayout_3.addWidget(self.frame_4)
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.addWidget(self.labelTarget)

        # Create & Set Horizontal Layouts 
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.addWidget(self.labelInfo)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.addWidget(self.inputDirectory)
        self.horizontalLayout_5.addWidget(self.buttonBrowse)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        # Connect the Browse PushButton to browsePath function
        self.buttonBrowse.clicked.connect(self.browsePath)

        # Display the MainWindow with its Widgets on the screen
        self.show()

    def browsePath(self):
        
        # Create a Select Folder Dialog and return the path
        savePath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select directory"))

        # Set the path in ./Frame 4/inputDirectory
        self.inputDirectory.setText(savePath)

        # Save the path to settings.txt (if it doesn't exist then it will be created)
        with open(settingsFilePath, "w") as f:
            f.write(savePath)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.setupUi()
    sys.exit(app.exec_())
