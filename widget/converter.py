import os


def to_py(target, save_to):
    """ Call pyuic5 in command prompt

        Link for more info on commands:
        https://doc.bccnsoft.com/docs/PyQt5/designer.html#pyuic5
    """

    # Get the file name of target
    filename = os.path.basename(target[:-3])

    # Use os module to call pyuic5 and convert the file
    os.system("pyuic5 -o {}/{}.py {}".format(save_to, filename, target))
