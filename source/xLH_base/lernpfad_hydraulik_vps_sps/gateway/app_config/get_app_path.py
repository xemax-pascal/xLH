import sys, os, pathlib


def get_app_path():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        app_path = sys._MEIPASS
    else:
        app_path = str(pathlib.Path(__file__).parents[1].as_posix())
    return app_path


if __name__ == '__main__':
    print(get_app_path())


# https://pyinstaller.org/en/stable/runtime-information.html