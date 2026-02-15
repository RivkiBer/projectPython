 ## פרטים ID וכו ע"י פונקציות נוספות ומכניסה תיקייה חדשה עם הקבצים עם השינויים"#
# #יוצR HEAD שמצביע על הCOMMIT האחרון המשתנה יהיה מצביע על כל השמות
#
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# def create_commit(message):
#     if not os.path.exists('.wit/staged_file'):
#         print("you need to do add Command before commit and chek if you did git init")
#         return
#
#     commit_id = get_commit_id()
#     print(commit_id)
#     os.makedirs(f".wit/commits/{commit_id}/files", exist_ok=True)
#     source = '.wit/staged_file'
#     dest = fr".wit/commits/{commit_id}/files"
#     shutil.copytree(source, dest)
#     os.makedirs(f".wit/commits/{commit_id}/details.txt")
#     with open(f".wit/commits/{commit_id}/details.txt", "w") as details_file:
#         details_file.write(f"Date: {datetime.datetime.now()}\n")
#         details_file.write(f"Message: {message}\n")
#
#
# def get_commit_id():
#     return str(uuid.uuid4())[:8]  # לקחת רק 8 תווים ראשונים
#   # יצירת מזהה ייחודי
import os
import shutil
import datetime
import uuid


def create_commit(message):
    if not os.path.exists('.wit/staged_file'):
        print("You need to use the 'add' command before commit and check if you did 'git init'.")
        return

    commit_id = get_commit_id()
    print(f"Commit ID: {commit_id}")

    commit_path: str = f".wit/commits/{commit_id}"
    os.makedirs(f"{commit_path}/files", exist_ok=True)

    source = '.wit/staged_file'
    dest = f"{commit_path}/files"

    if os.path.exists(dest):
        shutil.rmtree(dest)  # מחיקת תיקיית יעד אם היא קיימת

    shutil.copytree(source, dest)

    # יצירת קובץ details.txt
    with open(f"{commit_path}/details.txt", "w", encoding="utf-8") as details_file:
        details_file.write(f"Date: {datetime.datetime.now()}\n")
        details_file.write(f"Message: {message}\n")
    with open(".wit/commits/head.txt", "w", encoding="utf-8") as details_file:
        details_file.write(os.path.basename(commit_path))


def get_commit_id():
    return str(uuid.uuid4())[:8]  # לקיחה של 8 תווים ראשונים מהמזהה הייחודי
