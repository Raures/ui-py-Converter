import os
import sys

from pathlib import Path
from widget.widget import MainWindow
from PyQt5.QtWidgets import QApplication

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow(savePath, settingsFilePath)
    sys.exit(app.exec_())
