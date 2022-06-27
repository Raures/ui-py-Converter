import os


def to_py(file_to_convert: str, save_to_path: str):
    """ Run 'pyuic5 -o output.py input.ui' in command prompt

        Converts the .ui file to .py and keeps its original name.

        Link for more info on commands:
        https://doc.bccnsoft.com/docs/PyQt5/designer.html#pyuic5
    """

    filename = os.path.basename(file_to_convert[:-3])

    os.system("pyuic5 -o {}/{}.py {}".format(save_to_path, filename, file_to_convert))
