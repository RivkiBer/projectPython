import os
import shutil


def move_checkout(commit_name,path2):
    path = r'.wit\commits'
    if os.path.exists(f"{path}/{commit_name}"):
        with open(".wit/commits/head.txt", "w", encoding="utf-8") as details_file:
            details_file.write(commit_name)
            # הנתיב לתיקיה הראשית
            folder_path = path2
            # שם התיקיה שברצונך לשמור
            keep_folder = '.wit'

            # עובר על כל הקבצים והתיקיות בתיקיה
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)

                # אם זה תיקייה ושמה לא שווה לשם התיקייה לשמירה
                if os.path.isdir(item_path) and item != keep_folder and item != 'wit.py' and item !='checkout.py':
                    shutil.rmtree(item_path)  # מוחק את התיקייה ואת כל תוכנה
                elif os.path.isfile(item_path):
                    os.remove(item_path)  # מוחק קובץ

            # הגדר את הנתיב של התיקיות
            source_folder = f"{path}/{commit_name}"# התיקייה המקורית
            destination_folder = path2  # התיקייה היעד
            # עבור על כל הקבצים והתיקיות בתיקייה המקורית
            for item in os.listdir(source_folder):
                source_item = os.path.join(source_folder, item)
                destination_item = os.path.join(destination_folder, item)
                if os.path.isdir(source_item):
                    shutil.copytree(source_item, destination_item)
                elif os.path.isfile(source_item):
                    shutil.copy2(source_item, destination_item)





