from PyQt5.QtWidgets import QLabel
from converter import to_py


class DragAndDropLabel(QLabel):
    """ Return a QLabel object that accepts drag-and-drop files """

    def __init__(self, save_path):
        super(DragAndDropLabel, self).__init__()

        self.save_path = save_path

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
        to_py(e.mimeData().text()[8:], self.save_path)
