import sys
import pathlib
import conf

class Db:
    def __init__(self):
        datadir = Db._create_and_get_dir()
        print(datadir)

    @staticmethod
    def _get_datadir() -> pathlib.Path:

        """
        Returns a parent directory path
        where persistent application data can be stored.

        # linux: ~/.local/share
        # macOS: ~/Library/Application Support
        # windows: C:/Users/<USER>/AppData/Roaming
        """

        home = pathlib.Path.home()

        if sys.platform == "win32":
            return home / "AppData/Roaming"
        elif sys.platform == "linux":
            return home / ".local/share"
        elif sys.platform == "darwin":
            return home / "Library/Application Support"

    @staticmethod
    def _create_and_get_dir():
        my_datadir = Db._get_datadir() / conf.APP_NAME
        try:
            my_datadir.mkdir(parents=True)
        except FileExistsError:
            pass
