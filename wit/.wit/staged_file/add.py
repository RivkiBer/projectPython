import shutil
import os
from os.path import exists
from pathlib import Path


#פונקציה שבודקת את תיקיית staged_file ומכניסה לשם את כל הקבצים ששונו עם כל הבדיקות

def add_to_stage(file_name):
    if not os.path.exists('.wit'):
        print("you need to initialize the repository first")
        return

    if file_name=='.':

        src = '.'
        dest = '.wit/staged_file'
        skip = '.wit'
        shutil.copytree(src, dest,ignore=shutil.ignore_patterns(skip),dirs_exist_ok=True)
    else:
        add_file(file_name)

#פונקציה שמוסיפה קובץ מסוי
def add_file(file_name):
    if is_file_changed(file_name):
        file_path = file_name
        file_name_temp = Path(file_path).name
        dest_path = f'.wit/staged_file/{file_name_temp}'
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


#האם היה שינויים
def is_file_changed(file_name):
    if check_name_in_file(file_name,'.wit/.witignor.txt'):
      print("the file is in the .witignore file")
      return False
    if os.path.exists(f'.wit/staged_file/{file_name}'):
        return not if_files_equal(file_name, '.wit/staged_file/file_name')

    with open('.wit/commits/head.txt', 'r') as head_file:
        head_commit = head_file.read().strip()
        if exists(head_commit) :
            path= find_file_in_folder(file_name,f'.wit/commits/{head_commit}')
            if path is not None:
               if if_files_equal(path,file_name):
                   return False
    return True


#אם הקובץ השתנה מהADD האחרוןה
def if_files_equal(file1, file2):
    if os.path.isdir(file1) or os.path.isdir(file2):
        return False
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            return f1.read() == f2.read()
    except Exception as e:
        print(f"Error comparing files: {e}")
        return False


#
def check_name_in_file(name_to_find,path):
        with open(f'{path}', 'r', encoding='utf-8') as file:
            for line in file:
                if name_to_find.strip() == line.strip():
                    return True
        return False
def find_file_in_folder(file_name,path):
        for root, dirs, files in os.walk(path):
            if file_name in files:
                return os.path.join(root, file_name)
        return None
