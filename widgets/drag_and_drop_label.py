from PyQt5.QtWidgets import QLabel
from func.converter import to_py


class DragAndDropLabel(QLabel):
    """ Return a QLabel object that accepts drag-and-drop files """

    def __init__(self, path: str):
        super(DragAndDropLabel, self).__init__()

        self.save_path = path

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/uri-list"):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):

        to_py(event.mimeData().text()[8:], self.save_path)  # [8:] is used to remove "file:///" from mimeData().text()
