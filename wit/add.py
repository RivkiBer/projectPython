import os
import shutil
import click
import files_func


def add_to_stage(file_name=None):
    # 1. תמיד נעבוד עם נתיבים מוחלטים כדי למנוע בלבול
    current_dir = os.path.abspath(os.getcwd())
    staged_root = os.path.join(current_dir, '.wit', 'staged_file')

    # 2. זיהוי היעד - אם זה נקודה, היעד הוא תיקיית העבודה הנוכחית
    if file_name == '.' or file_name is None:
        target = current_dir
    else:
        # חיפוש הקובץ/תיקייה אם ניתן שם ספציפי
        target = files_func.find_file_in_folder(file_name, current_dir)

    if not target or not os.path.exists(target):
        click.echo(f"Error: Path {file_name} not found.")
        return

    if not os.path.exists(os.path.join(current_dir, '.wit')):
        click.echo("Error: .wit directory not found. Run init first.")
        return

    # 3. הגדרת התעלמות (Ignore)
    skip = {'.wit'}
    ignore_file = os.path.join(current_dir, '.wit', '.witignore.txt')
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r', encoding='utf-8') as f:
            skip.update(line.strip() for line in f if line.strip())

    # 4. סריקה והוספה
    # אם זה קובץ בודד - נהפוך אותו לרשימה. אם תיקייה - נסרוק.
    if os.path.isfile(target):
        files_to_process = [target]
    else:
        files_to_process = []
        for root, dirs, files in os.walk(target):
            # סינון תיקיות (כדי לא להיכנס ל-.wit)
            dirs[:] = [d for d in dirs if d not in skip]
            for f in files:
                if f not in skip:
                    files_to_process.append(os.path.join(root, f))

    # 5. העתקה בפועל
    for full_path in files_to_process:
        if files_func.is_file_changed(full_path):
            # חישוב נתיב יחסי מתיקיית השורש של הפרויקט
            rel_path = os.path.relpath(full_path, current_dir)
            dest_path = os.path.join(staged_root, rel_path)

            # יצירת תיקיות היעד בסטייג'
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # העתקה
            shutil.copy2(full_path, dest_path)
            click.echo(f"Staged: {rel_path}")

    click.echo("Add operation complete.")