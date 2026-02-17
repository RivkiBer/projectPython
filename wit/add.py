# # -*- coding: utf-8 -*-
#
# import shutil
# import os
# from os.path import exists
# from pathlib import Path
# import files_func
#
# # פונקציה שבודקת את תיקיית staged_file ומכניסה לשם את כל הקבצים ששונו עם כל הבדיקות
# def add_to_stage(file_name=None, staged_path='.wit/staged_file'):
#     current_directory = os.getcwd()  # הנתיב הנוכחי שבו התוכנית רצה
#     # קריאה לפונקציה לחיפוש הקובץ
#     if file_name!='.':
#      file_name = files_func.find_file_in_folder(file_name, current_directory)        # קריאה לפונקציה שמוסיפה את הקובץ לסטייג'
#     else:file_name=current_directory
#     if file_name is None:
#         return f"לא נמצא קובץ בשם {file_name} בתתי "
#
#     if not os.path.exists('.wit'):
#         print("You need to initialize the repository first")
#         return
#
#     if file_name==current_directory:
#        add_file()
#     else:
#         #פונקציה שמוסיפה קובץ
#         add_file(file_name, staged_path)
#
#     src = file_name
#     dest = staged_path
#
#     # קריאת שמות הקבצים להתעלמות מתוך .witignore.txt
#     skip = ['.wit']  # הוספנו את .wit כדי לא להעתיק אותה
#     ignore_file = '.wit/.witignore.txt'
#     if os.path.exists(ignore_file):
#         with open(ignore_file, 'r', encoding='utf-8') as f:
#             skip += [line.strip() for line in f if line.strip()]
#
#     # אם הוחלט להוסיף תיקיה שלמה
#     if file_name  == '.':
#         os.makedirs(dest, exist_ok=True)
#
#         for root, dirs, files in os.walk(src):
#             # התעלמות מתיקיות שמופיעות ב-skip
#             dirs[:] = [d for d in dirs if d not in skip]
#
#             # נתיב יחסית ל-src
#             rel_path = os.path.relpath(root, src)
#             dest_path = os.path.join(dest, rel_path)
#             os.makedirs(dest_path, exist_ok=True)
#
#             for file in files:
#                 if file not in skip:
#                     shutil.copy2(os.path.join(root, file), os.path.join(dest_path, file))
#     else:
#         # אם מדובר בקובץ ספציפי
#         add_file(file_name, staged_path)
#     print("successfully added to stage")
#
# # פונקציה שמוסיפה קובץ מסויים
# def add_file(file_name, staged_path='.wit/staged_file'):
#     if not is_file_changed(file_name):
#         return
#     # התעלמות מקבצים שנמצאים ב-.witignore.txt
#     if files_func.check_name_in_file(file_name, '.wit/.witignore.txt'):
#         print(f"The file '{file_name}' is in the .witignore file. Skipping.")
#         return
#     file_path = file_name
#     file_name_temp = Path(file_path).name
#     dest_path = f"{staged_path}/{file_name_temp}"
#     files_func.remove_path(dest_path)
#     files_func.copy_files(file_name, dest_path)
#
#
# #  האם היה שינויים
# def is_file_changed(path_file):
#     file_name=os.path.basename(path_file)
#     if files_func.check_name_in_file(file_name, '.wit/.witignore.txt'):
#         return False
#     staged_file_path = f'.wit/staged_file/{file_name}'
#     #אם קיים הקובץ עם השם של הקובץ להעלאה
#     if os.path.exists(staged_file_path):
#         if os.path.isdir(path_file):
#           return not files_func.if_folders_equals(path_file, staged_file_path)
#         else:return  not files_func.if_files_equal(file_name,)
#
#     head_path = '.wit/commits/head.txt'
#     if os.path.exists(head_path):
#         with open(head_path, 'r', encoding='utf-8') as head_file:
#             head_commit = head_file.read().strip()
#             commit_path = f'.wit/commits/{head_commit}'
#             if exists(commit_path):
#                 path = files_func.find_file_in_folder(file_name, commit_path)
#                 if path is not None:
#                     if os.path.isdir(path):
#                      if files_func.if_folders_equals(path, file_name):
#                          return  False
#                      elif files_func.if_files_equal(path,file_name):
#                         return False
#     return True
#
#
#
#
#
import os
import shutil
from pathlib import Path
import files_func


def add_to_stage(file_name=None, staged_path='.wit/staged_file'):
    """
    מוסיף קובץ או תיקיה לשלב הסטייג'ינג.
    אם אין קובץ או תיקיה מוגדרים, יתווספו כל הקבצים בפרויקט חוץ מ-.wit.
    """
    current_directory = os.getcwd()  # הנתיב הנוכחי שבו התוכנית רצה

    # אם לא הוגדר קובץ ספציפי, סורקים את כל התיקיות
    if file_name != '.':
        file_name = files_func.find_file_in_folder(file_name, current_directory)
    else:
        file_name = current_directory

    if file_name is None:
        raise FileNotFoundError(f"לא נמצא קובץ בשם {file_name} בתתי תיקיות")

    if not os.path.exists('.wit'):
        raise FileNotFoundError("לא נמצא תיקיית .wit. יש לבצע 'init' לפני השימוש ב-add")

    # אם אנחנו עובדים על כל התיקיה
    if file_name == current_directory:
        add_all_files_to_stage(current_directory, staged_path)
    else:
        # אם מדובר בקובץ ספציפי
        add_file(file_name, staged_path)

    print(f"successfully added {file_name} to stage")


def add_all_files_to_stage(directory, staged_path):
    """
    סורק את כל הקבצים בתיקיה (למעט תיקיית .wit) ומוסיף לשלב הסטייג'ינג.
    """
    try:
        skip = ['.wit']  # התעלמות מתיקיית .wit
        ignore_file = '.wit/.witignore.txt'

        # אם יש קובץ .witignore, נטען את הקבצים שצריך להתעלם מהם
        if os.path.exists(ignore_file):
            with open(ignore_file, 'r', encoding='utf-8') as f:
                skip += [line.strip() for line in f if line.strip()]

        for root, dirs, files in os.walk(directory):
            # התעלמות מתיקיות שצריך להתעלם מהן
            dirs[:] = [d for d in dirs if d not in skip]

            for file in files:
                file_path = os.path.join(root, file)

                # אם הקובץ לא נמצא ב-.witignore
                if file not in skip:
                    add_file(file_path, staged_path)

    except FileNotFoundError as e:
        raise FileNotFoundError(f"לא נמצאה תיקייה בשם {directory}: {e}")
    except PermissionError as e:
        raise PermissionError(f"לא ניתן לגשת לתיקייה {directory}: {e}")
    except Exception as e:
        raise Exception(f"נפלה שגיאה במהלך הוספת קבצים לתיקיית הסטייג'ינג: {e}")


def add_file(file_name, staged_path='.wit/staged_file'):
    """
    מוסיף קובץ ספציפי לשלב הסטייג'ינג אם יש שינוי.
    """
    try:
        # אם הקובץ לא השתנה, לא נוסיף אותו
        if not files_func.is_file_changed(file_name):
            print(f"{file_name} hasn't changed, skipping.")
            return

        # יצירת נתיב עבור הקובץ בסטייג'ינג
        file_name_temp = Path(file_name).name
        dest_path = os.path.join(staged_path, file_name_temp)

        # אם הקובץ קיים בסטייג'ינג, נמחק אותו קודם
        if os.path.exists(dest_path):
            files_func.remove_path(dest_path)

        # העתקת הקובץ או התיקיה
        files_func.copy_files(file_name, dest_path)
        print(f"Added {file_name} to staging.")

    except FileNotFoundError:
        raise FileNotFoundError(f"הקובץ {file_name} לא נמצא.")
    except PermissionError:
        raise PermissionError(f"לא ניתן לגשת לקובץ {file_name}. חסר היתרונות המתאימים.")
    except Exception as e:
        raise Exception(f"נפלה שגיאה במהלך הוספת הקובץ {file_name} לשלב הסטייג'ינג: {e}")



