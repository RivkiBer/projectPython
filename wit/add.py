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

        for item in os.listdir('.'):
            if item != '.wit':
                add_file(item)
    else:
        add_file(file_name)

#פונקציה שמוסיפה קובץ מסוי
def add_file(file_name):
    if not is_file_changed(file_name):
        return
    file_path = file_name
    dest_path = os.path.join('.wit', 'staged_file', file_name)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
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
    if check_name_in_file(file_name,'.wit/.witignore.txt'):
      print("the file is in the .witignore file")
      return False
    staged_path = os.path.join('.wit', 'staged_file', file_name)

    if os.path.exists(staged_path):
        return not if_files_equal(file_name, staged_path)


    # וידוא שקובץ head.txt בכלל קיים כדי שלא תהיה שגיאת FileNotFoundError
    if os.path.exists('.wit/commits/head.txt'):
        with open('.wit/commits/head.txt', 'r') as head_file:
            head_commit = head_file.read().strip()
        
        # השינוי המרכזי: בדיקה שהמחרוזת לא ריקה (למשל לפני ה-commit הראשון)
        if head_commit: 
            commit_path = os.path.join('.wit', 'commits', head_commit)
            commit_file_path = os.path.join(commit_path, file_name)
            
            # בדיקה אם הקובץ קיים בקומיט הקודם ואם הוא זהה
            if os.path.exists(commit_file_path) and if_files_equal(commit_file_path, file_name):
                return False # רק אם הוא זהה לחלוטין לקודם, נחזיר False (כלומר: לא השתנה)

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

