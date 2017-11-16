import os


class FileWalker:
    def __init__(self, absolute_path):
        self.__absolute_path = os.path.abspath(absolute_path)

    def change_svg_suffix(self, suffix):
        file_count = 0
        for root, dirs, files in os.walk(self.__absolute_path):
            for fn in files:
                file_count = file_count + 1
                os.chdir(self.__absolute_path)
                os.rename(fn, "%s.svg" % (fn.split('.svg')[0]), suffix)
                print file_count

    def change_png_suffix(self, suffix):
        file_count = 0
        for root, dirs, files in os.walk(self.__absolute_path):
            for fn in files:
                file_count = file_count + 1
                os.chdir(self.__absolute_path)
                os.rename(fn, "%s.png" % (fn.split('.png')[0]), suffix)
                print file_count
