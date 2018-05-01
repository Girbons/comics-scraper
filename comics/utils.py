import os


def create_and_change_dir(dir_name):
    """
    :param string dir_name: is the folder name.

    create a directory if does not exist and change to it
    """
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    os.chdir(dir_name)
