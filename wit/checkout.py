import os
import shutil
import files_func
from status import show_status  # נניח שהפונקציה מחזירה רשימות או שיש פונקציה לבדיקת שינויים


def move_checkout(commit_id):
    commits_root = os.path.join('.wit', 'commits')
    target_commit_dir = os.path.join(commits_root, commit_id)

    # 1. בדיקה אם הקומיט בכלל קיים
    if not os.path.exists(target_commit_dir):
        print(f"Error: Commit ID {commit_id} not found.")
        return

    # 2. דרישת חובה: בדיקה אם יש שינויים לא שמורים (Uncommitted changes)
    # כאן כדאי להשתמש בלוגיקה של status. אם יש משהו ב-staged או modified - חוסמים.
    # לצורך הפשטות, נבדוק אם הסטייג' ריק והתיקייה תואמת לסטייג'
    staged_dir = os.path.join('.wit', 'staged_file')
    if os.path.exists(staged_dir) and os.listdir(staged_dir):
        print("Error: You have uncommitted changes in your staging area. Commit or remove them before checkout.")
        return

    # 3. ניקוי תיקיית העבודה (למעט .wit)
    current_dir = os.getcwd()
    for item in os.listdir(current_dir):
        if item == '.wit':
            continue
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

    # 4. שחזור הקבצים מתוך תיקיית ה-'files' של הקומיט
    source_files = os.path.join(target_commit_dir, 'files')
    if os.path.exists(source_files):
        for item in os.listdir(source_files):
            src_item = os.path.join(source_files, item)
            dst_item = os.path.join(current_dir, item)

            if os.path.isdir(src_item):
                shutil.copytree(src_item, dst_item)
            else:
                shutil.copy2(src_item, dst_item)

    # 5. עדכון ה-HEAD
    with open(os.path.join(commits_root, "head.txt"), "w", encoding="utf-8") as head_file:
        head_file.write(commit_id)

    print(f"Successfully checked out to commit {commit_id}")