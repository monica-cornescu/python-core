""" Finally block executes no matter how the try-block terminates
In case something happens with the mkdir operation, the original path will not be restored, so:
we handle the exception and do a cleanup (always restore the original path)
"""

import os
import sys


def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    try:
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)
        print("the original path was still restored")

if __name__ == '__main__':
    make_at("/etc/", "my_dir")
