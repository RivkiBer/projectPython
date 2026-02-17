import os
import shutil
import datetime
import uuid
import files_func
import click


def create_commit(message):
    staged_path = '.wit/staged_file'
    head_file = ".wit/commits/head.txt"

    # 1. בדיקה אם התיקייה קיימת ויש בה קבצים
    if not os.path.exists(staged_path) or not os.listdir(staged_path):
        click.echo("Error: Nothing to commit. Use 'add' first.")
        return

    # 2. בדיקה האם היו שינויים מהקומיט האחרון (דרישת חובה בפרויקט)
    if os.path.exists(head_file):
        with open(head_file, "r", encoding="utf-8") as f:
            last_commit_id = f.read().strip()

        if last_commit_id:  # אם זה לא הקומיט הראשון
            last_commit_files = f".wit/commits/{last_commit_id}/files"
            # השוואה בין מה שיש עכשיו בסטייג' למה שיש בקומיט האחרון

            if files_func.if_folders_equals(staged_path, last_commit_files):
                print("No changes detected since last commit. Commit aborted.")
                return

    # 3. יצירת מזהה ייחודי ונתיבים
    commit_id = get_commit_id()
    commit_path = f".wit/commits/{commit_id}"
    os.makedirs(f"{commit_path}/files", exist_ok=True)

    # 4. העתקת הקבצים מהסטייג' לקומיט החדש
    # שים לב: אנחנו מעתיקים מ-staged_file לתיקיית ה-files של הקומיט
    files_func.copy_files(staged_path, f"{commit_path}/files")

    # 5. יצירת קובץ details.txt עם התאריך וההודעה
    with open(f"{commit_path}/details.txt", "w", encoding="utf-8") as details:
        details.write(f"Date: {datetime.datetime.now()}\n")
        details.write(f"Message: {message}\n")

    # 6. עדכון ה-HEAD שיצביע על הקומיט החדש
    with open(head_file, "w", encoding="utf-8") as head:
        head.write(commit_id)

    # 7. ניקוי הסטייג'ינג לאחר הקומיט
    files_func.remove_path(staged_path)
    # יצירה מחדש של התיקייה הריקה כדי שה-add הבא לא יכשל
    os.makedirs(staged_path, exist_ok=True)

    click.echo(f"Successfully created commit: {commit_id}")


def get_commit_id():
    return str(uuid.uuid4())[:8]