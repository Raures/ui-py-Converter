import os
import sys

from PyQt5.QtWidgets import QApplication
from widgets.main_window import MainWindow

save_path = ""
SETTINGS_PATH = "settings.txt"

if not SETTINGS_PATH.path.exists():

    save_path = os.environ["HOMEPATH"] + "\\Desktop\\"

    with open("settings.txt", "w") as f:
        f.write(save_path)

else:
    with open("settings.txt", "r") as f:
        save_path = f.readline()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow(save_path, SETTINGS_PATH)
    sys.exit(app.exec_())
