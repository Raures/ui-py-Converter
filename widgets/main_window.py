from PyQt5.QtWidgets import QWidget, QFrame, QLabel
from PyQt5.QtWidgets import QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from widgets.drag_and_drop_label import DragAndDropLabel


class MainWindow(QWidget):
    """ Return a MainWindow object """

    def __init__(self, path, settings):
        super().__init__()

        self.save_path = path
        self.settings_file = settings

        # Set MainWindow configuration
        self.windowTitle = "Converter: User Interface to Python"
        self.windowSize = (440, 350)

        # Set ./Frame 1/labelInfo download link and text
        self.linkPyQt = "https://sourceforge.net/projects/pyqt/"
        self.textLabelInfo = "Before converting, please make sure that you have PyQt5 installed. \
                             To install PyQt5, you can visit <a href='{}'>this link</a> to download it, \
                             or run the following command in <b>cmd</b>: \
                             <font face='Consolas'> pip3 install PyQt5</font>".format(self.linkPyQt)

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

        # Widgets
        self.frame_1 = QFrame(self)
        self.labelInfo = QLabel(self.frame_1)

        self.frame_2 = QFrame(self)
        self.labelTarget = DragAndDropLabel(self.save_path)

        self.frame_3 = QFrame(self)
        self.labelQuestion = QLabel(self.frame_3)

        self.frame_4 = QFrame(self.frame_3)
        self.inputDirectory = QLineEdit(self.frame_4)
        self.buttonBrowse = QPushButton(self.frame_4)

        self.setup_ui()

    def setup_ui(self):
        # Set the Window Title and Window Size
        self.setWindowTitle(self.windowTitle)
        self.resize(self.windowSize[0], self.windowSize[1])

        # Create a Frame 1 to hold the Label with instructions
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)

        # Create a Label on Frame 1 to hold the instructions
        self.labelInfo.setWordWrap(True)
        self.labelInfo.setText(self.textLabelInfo)
        self.labelInfo.setOpenExternalLinks(True)
        # self.labelInfo.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Create a Frame 2 to hold DragAndDropLabel
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        # Create a Label that accepts files by drag-and-drop (see DragAndDropLabel above)
        self.labelTarget.setFont(QFont(self.fontLabelDragAndDrop))
        self.labelTarget.setAlignment(Qt.AlignCenter)
        self.labelTarget.setText(self.textLabelDragAndDrop)
        self.labelTarget.setStyleSheet(self.styleLabelDragAndDrop)
        self.labelTarget.setMinimumHeight(150)
        self.labelTarget.setAcceptDrops(True)

        # Create a Frame 3 to hold Label with information about the path
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        # Create a Label in Frame 3 with information about the path
        self.labelQuestion.setText(self.textLabelQuestion)

        # Create a Frame 4 to hold LineEdit and PushButton
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        # Create a LineEdit in Frame 4 that shows the saving path
        self.inputDirectory.setText(self.save_path)
        self.inputDirectory.setStyleSheet(self.styleLineEdit)

        # Create a PushButton in Frame 4 to browse the saving path
        self.buttonBrowse.setText(self.textBrowseButton)

        # Create & Set Vertical Layouts
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.frame_1)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_3)

        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.addWidget(self.labelQuestion)
        self.verticalLayout_3.addWidget(self.frame_4)

        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.addWidget(self.labelTarget)

        # Create & Set Horizontal Layouts
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.addWidget(self.labelInfo)

        self.horizontalLayout_2 = QHBoxLayout(self.frame_1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()

        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.addWidget(self.inputDirectory)
        self.horizontalLayout_5.addWidget(self.buttonBrowse)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        # Connect the Browse PushButton to browsePath function
        self.buttonBrowse.clicked.connect(self.browse_path)

        # Display the MainWindow with its Widgets on the screen
        self.show()

    def browse_path(self):
        # Create a Select Folder Dialog and return the path
        self.save_path = str(QFileDialog.getExistingDirectory(self, "Select directory"))

        # Set the path in ./Frame 4/inputDirectory
        self.inputDirectory.setText(self.save_path)

        # Save the path to settings.txt (if it doesn't exist then it will be created)
        with open(self.settings_file, "w") as f:
            f.write(self.save_path)

