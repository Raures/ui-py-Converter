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

        self.window_title = "Converter: User Interface to Python"
        self.window_size = (440, 350)

        self.link_pyqt5 = "https://sourceforge.net/projects/pyqt/"
        self.text_label_info = "Before converting, please make sure that you have PyQt5 installed. \
                             To install PyQt5, you can visit <a href='{}'>this link</a> to download it, \
                             or run the following command in <b>cmd</b>: \
                             <font face='Consolas'> pip3 install PyQt5</font>".format(self.link_pyqt5)

        self.text_label_drag_and_drop = "Drag and drop the <b>user interface</b> (<b>*.ui</b>) file here"
        self.style_label_drag_and_drop = "QLabel { border: 1px dotted black; }"
        self.font_label_drag_and_drop = "Myanmar Text"

        self.text_label_question = "Where should the <b>python</b> file be saved at?"

        self.style_line_edit = "QLineEdit { padding-bottom: 2px; padding-left: 2px; }"

        self.text_browse_button = "Browse"

        self.frame_1 = QFrame(self)
        self.label_info = QLabel(self.frame_1)

        self.frame_2 = QFrame(self)
        self.label_target = DragAndDropLabel(self.save_path)

        self.frame_3 = QFrame(self)
        self.label_question = QLabel(self.frame_3)

        self.frame_4 = QFrame(self.frame_3)
        self.input_directory = QLineEdit(self.frame_4)
        self.button_browse = QPushButton(self.frame_4)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout_2 = QVBoxLayout(self)
        self.vertical_layout_3 = QVBoxLayout()
        self.vertical_layout_4 = QVBoxLayout(self.frame_3)
        self.vertical_layout_5 = QVBoxLayout()

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout_2 = QHBoxLayout(self.frame_1)
        self.horizontal_layout_3 = QHBoxLayout(self.frame_2)
        self.horizontal_layout_4 = QHBoxLayout()
        self.horizontal_layout_5 = QHBoxLayout(self.frame_4)

        self.setup_ui()

    def setup_ui(self):
        # Set the Window Title and Window Size
        self.setWindowTitle(self.window_title)
        self.resize(self.window_size[0], self.window_size[1])

        # Create a Frame 1 to hold the Label with instructions
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)

        # Create a Label on Frame 1 to hold the instructions
        self.label_info.setWordWrap(True)
        self.label_info.setText(self.text_label_info)
        self.label_info.setOpenExternalLinks(True)
        self.label_info.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Create a Frame 2 to hold DragAndDropLabel
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        # Create a Label that accepts files by drag-and-drop (see DragAndDropLabel above)
        self.label_target.setFont(QFont(self.font_label_drag_and_drop))
        self.label_target.setAlignment(Qt.AlignCenter)
        self.label_target.setText(self.text_label_drag_and_drop)
        self.label_target.setStyleSheet(self.style_label_drag_and_drop)
        self.label_target.setMinimumHeight(150)
        self.label_target.setAcceptDrops(True)

        # Create a Frame 3 to hold Label with information about the path
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        # Create a Label in Frame 3 with information about the path
        self.label_question.setText(self.text_label_question)

        # Create a Frame 4 to hold LineEdit and PushButton
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        # Create a LineEdit in Frame 4 that shows the saving path
        self.input_directory.setText(self.save_path)

        # Create a PushButton in Frame 4 to browse the saving path
        self.button_browse.setText(self.text_browse_button)

        # Set Vertical Layouts
        self.vertical_layout.addWidget(self.frame_1)
        self.vertical_layout.addWidget(self.frame_2)
        self.vertical_layout.addWidget(self.frame_3)

        self.vertical_layout_2.addLayout(self.vertical_layout)

        self.vertical_layout_3.addWidget(self.label_question)
        self.vertical_layout_3.addWidget(self.frame_4)

        self.vertical_layout_4.addLayout(self.vertical_layout_3)

        self.vertical_layout_5.addWidget(self.label_target)

        # Set Horizontal Layouts
        self.horizontal_layout.addWidget(self.label_info)

        self.horizontal_layout_2.addLayout(self.horizontal_layout)

        self.horizontal_layout_3.addLayout(self.vertical_layout_5)

        self.horizontal_layout_5.addWidget(self.input_directory)
        self.horizontal_layout_5.addWidget(self.button_browse)
        self.horizontal_layout_5.addLayout(self.horizontal_layout_4)

        # Connect the Browse PushButton to browsePath function
        self.button_browse.clicked.connect(self.browse_path)

        # Display the MainWindow with its Widgets on the screen
        self.show()

    def browse_path(self):
        # Create a Select Folder Dialog and return the path
        self.save_path = str(QFileDialog.getExistingDirectory(self, "Select directory"))

        # Set the path in ./Frame 4/input_directory
        self.input_directory.setText(self.save_path)

        # Save the path to settings.txt (if it doesn't exist then it will be created)
        with open(self.settings_file, "w") as f:
            f.write(self.save_path)

