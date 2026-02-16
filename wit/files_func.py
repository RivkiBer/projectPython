import os
import shutil


def copy_files(src, dest, skip=''):
    shutil.copytree(src, dest, ignore=shutil.ignore_patterns(*skip), dirs_exist_ok=True)

    # מחיקת הנתיב הקיים אם קיים
def remove_path(path):
     if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)


