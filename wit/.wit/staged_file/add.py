# -*- coding: utf-8 -*-

import shutil
import os
from os.path import exists
from pathlib import Path



def add_to_stage(file_name=None, staged_path='.wit/staged_file'):
    if file_name is None:
        print("No file specified to add.")
        return
    if not os.path.exists('.wit'):
        print("You need to initialize the repository first")
        return


    src = r'C:\Users\PC\Desktop\projectPython\wit'
    dest = staged_path

    # קריאת שמות הקבצים להתעלמות מתוך .witignore.txt
    skip = ['.wit']  # הוספנו את .wit כדי לא להעתיק אותה
    ignore_file = '.wit/.witignore.txt'
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r', encoding='utf-8') as f:
            skip += [line.strip() for line in f if line.strip()]

    # אם הוחלט להוסיף תיקיה שלמה
    if file_name  == '.':
        os.makedirs(dest, exist_ok=True)

        for root, dirs, files in os.walk(src):
            # התעלמות מתיקיות שמופיעות ב-skip
            dirs[:] = [d for d in dirs if d not in skip]

            # נתיב יחסית ל-src
            rel_path = os.path.relpath(root, src)
            dest_path = os.path.join(dest, rel_path)
            os.makedirs(dest_path, exist_ok=True)

            for file in files:
                if file not in skip:
                    shutil.copy2(os.path.join(root, file), os.path.join(dest_path, file))
    else:
        # אם מדובר בקובץ ספציפי
        add_file(file_name, staged_path)
    print("successfully added to stage")

# פונקציה שמוסיפה קובץ מסויים
def add_file(file_name, staged_path='.wit/staged_file'):
    if not is_file_changed(file_name):
        return

    # התעלמות מקבצים שנמצאים ב-.witignore.txt
    if check_name_in_file(file_name, '.wit/.witignore.txt'):
        print(f"The file '{file_name}' is in the .witignore file. Skipping.")
        return

    file_path = file_name
    file_name_temp = Path(file_path).name
    dest_path = f"{staged_path}/{file_name_temp}"

    # מחיקת הנתיב הקיים אם קיים
    if os.path.exists(dest_path):
        if os.path.isdir(dest_path):
            shutil.rmtree(dest_path)
        else:
            os.remove(dest_path)

    # העתקת התיקייה או הקובץ
    if os.path.isdir(file_name):
        shutil.copytree(file_name, dest_path, dirs_exist_ok=True)
    else:
        shutil.copy(file_name, dest_path)


# האם היה שינויים
def is_file_changed(file_name):
    if check_name_in_file(file_name, '.wit/.witignore.txt'):
        return False

    staged_file_path = f'.wit/staged_file/{file_name}'
    if os.path.exists(staged_file_path):
        return not if_files_equal(file_name, staged_file_path)

    head_path = '.wit/commits/head.txt'
    if os.path.exists(head_path):
        with open(head_path, 'r', encoding='utf-8') as head_file:
            head_commit = head_file.read().strip()
            commit_path = f'.wit/commits/{head_commit}'
            if exists(commit_path):
                path = find_file_in_folder(file_name, commit_path)
                if path is not None:
                    if if_files_equal(path, file_name):
                        return False
    return True


# אם הקובץ השתנה מהADD האחרון
def if_files_equal(file1, file2):
    if os.path.isdir(file1) or os.path.isdir(file2):
        return False
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            return f1.read() == f2.read()
    except Exception as e:
        print(f"Error comparing files: {e}")
        return False


# בודק אם שם הקובץ קיים בקובץ .witignore
def check_name_in_file(name_to_find, path):
    if not os.path.exists(path):
        return False
    with open(f'{path}', 'r', encoding='utf-8') as file:
        for line in file:
            if name_to_find.strip() == line.strip():
                return True
    return False


# מוצא קובץ בתיקייה מסוימת
def find_file_in_folder(file_name, path):
    for root, dirs, files in os.walk(path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None
