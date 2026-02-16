# -*- coding: utf-8 -*-

import shutil
import os
from os.path import exists
from pathlib import Path
import files_func


# פונקציה שבודקת את תיקיית staged_file ומכניסה לשם את כל הקבצים ששונו עם כל הבדיקות
def add_to_stage(file_name, staged_path='.wit/staged_file'):
    print(file_name)
    if not os.path.exists('.wit'):
        print("You need to initialize the repository first")
        return

    if os.path.basename('.'):
        src = r'C:\שנה ב תכנות\פייתון\wit_project\projectPython\wit'
        dest = staged_path
        skip = ['.wit']
        #שולח לתיקייה שמעתיקה את הקבצים בפרויקט לתוך STAGED_FILE
        files_func.copy_files(src, dest, skip)
    else:
        #פונקציה שמוסיפה קובץ
        add_file(file_name, staged_path)


# פונקציה שמוסיפה קובץ מסויים
def add_file(file_name, staged_path='.wit/staged_file'):
    if not is_file_changed(file_name):
        return
    file_path = file_name
    file_name_temp = Path(file_path).name
    dest_path = f"{staged_path}/{file_name_temp}"
    files_func.remove_path(dest_path)
    files_func.copy_files(file_name, dest_path)


# האם היה שינויים
def is_file_changed(file_name):
    if check_name_in_file(file_name, '.wit/.witignor.txt'):
        print("The file is in the .witignore file")
        return False
    if os.path.exists(f'.wit/staged_file/{file_name}'):
        return not if_files_equal(file_name, '.wit/staged_file/file_name')

    with open('.wit/commits/head.txt', 'r') as head_file:
        head_commit = head_file.read().strip()
        if exists(head_commit):
            path = find_file_in_folder(file_name, f'.wit/commits/{head_commit}')
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
