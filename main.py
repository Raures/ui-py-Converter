import os
import sys

from PyQt5.QtWidgets import QApplication
from widgets.main_window import MainWindow

save_path = ""
SETTINGS_FILE = "settings.txt"
DEFAULT_PATH = os.environ["HOMEPATH"] + "\\Desktop\\"

if not os.path.exists(SETTINGS_FILE):

    save_path = DEFAULT_PATH

    with open(SETTINGS_FILE, "w") as f:
        f.write(save_path)

else:
    with open(SETTINGS_FILE, "r") as f:
        save_path = f.readline()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow(save_path, SETTINGS_FILE)
    sys.exit(app.exec_())
