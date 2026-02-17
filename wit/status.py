import os
from os.path import join, exists, relpath
from files_func import if_files_equal


def show_status():
    staged_dir = join('.wit', 'staged_file')
    commits_dir = join('.wit', 'commits')
    head_file = join(commits_dir, 'head.txt')
    # שימי לב: לפי הדרישות הקובץ הוא .witignore (בלי .txt)
    witignore_file = '.witignore'

    # טעינת קבצי התעלמות
    ignored = ['.wit']
    if exists(witignore_file):
        with open(witignore_file, 'r', encoding='utf-8') as f:
            ignored += [line.strip() for line in f if line.strip()]

    def is_ignored(rel_path):
        return any(rel_path == i or rel_path.startswith(i + os.sep) for i in ignored)

    # קבלת נתיב הקבצים של הקומיט האחרון
    last_commit_files_dir = None
    if exists(head_file):
        with open(head_file, 'r', encoding='utf-8') as f:
            c = f.read().strip()
            if c:
                # הנתיב חייב לכלול את תיקיית ה-'files' הפנימית
                last_commit_files_dir = join(commits_dir, c, 'files')

    staged_changes = []
    modified_not_staged = []
    untracked_files = []

    # סריקת הפרויקט
    for root, dirs, files in os.walk('.'):
        # סינון תיקיות שצריך להתעלם מהן כבר בשלב הסריקה
        dirs[:] = [d for d in dirs if not is_ignored(relpath(join(root, d), '.'))]

        for f in files:
            path = join(root, f)
            rel_p = relpath(path, '.')

            if is_ignored(rel_p):
                continue

            staged_file_path = join(staged_dir, rel_p)
            commit_file_path = join(last_commit_files_dir, rel_p) if last_commit_files_dir else None

            # 1. בדיקת Staged (נמצא בסטייג' ושונה מהקומיט האחרון)
            if exists(staged_file_path):
                if not commit_file_path or not exists(commit_file_path) or not if_files_equal(staged_file_path,
                                                                                              commit_file_path):
                    staged_changes.append(rel_p)

                # 2. בדיקת Modified (שונה בתיקיית העבודה לעומת הסטייג')
                if not if_files_equal(path, staged_file_path):
                    modified_not_staged.append(rel_p)

            else:
                # 3. בדיקת Untracked (לא בסטייג' ולא בקומיט)
                if not commit_file_path or not exists(commit_file_path):
                    untracked_files.append(rel_p)
                # מקרה מיוחד: היה בקומיט, לא בסטייג', אבל שונה בתיקיית העבודה
                elif not if_files_equal(path, commit_file_path):
                    modified_not_staged.append(rel_p)

    # הדפסה לפי פורמט ברור
    print("\n--- WIT STATUS ---")
    print(f"Changes to be committed: {sorted(staged_changes) if staged_changes else 'None'}")
    print(f"Changes not staged for commit: {sorted(modified_not_staged) if modified_not_staged else 'None'}")
    print(f"Untracked files: {sorted(untracked_files) if untracked_files else 'None'}\n")