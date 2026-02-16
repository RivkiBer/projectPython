
#מדפיס את הSTATUS הנדוכחי ע"י קבלה מהCOMMIT ןה STAGED
import os
from os.path import join, exists, relpath
from add import if_files_equal

def show_status():
    staged_dir = join('.wit', 'staged_file')
    commits_dir = join('.wit', 'commits')
    head_file = join(commits_dir, 'head.txt')
    witignore_file = join('.wit', '.witignore')

    # קבצים להתעלם מהם
    ignored = []
    if exists(witignore_file):
        with open(witignore_file, 'r', encoding='utf-8') as f:
            ignored = [line.strip() for line in f]

    def is_ignored(path):
        # קבצים או תיקיות שצריך להתעלם מהם באופן אוטומטי
        ignored_paths = ['venv', '__pycache__', '.DS_Store', 'Thumbs.db']

        # אם הקובץ נמצא בתיקיות שצריך להתעלם מהן, תחזור True
        if any(path.startswith(i) for i in ignored_paths):
            return True

        # אם הקובץ מופיע ב-witignore, תחזור True
        return any(path.startswith(i) for i in ignored)

    # קבלת הקומיט האחרון
    last_commit = None
    if exists(head_file):
        with open(head_file, 'r', encoding='utf-8') as f:
            c = f.read().strip()
            if c:
                last_commit = join(commits_dir, c)

    staged_changes = []
    modified_not_staged = []
    untracked_files = []

    # סורק את הקבצים בספריית הפרויקט
    for root, _, files in os.walk('.'):
        for f in files:
            if f.startswith('.wit'):
                continue
            path = join(root, f)
            rel_path = relpath(path, '.')
            if is_ignored(rel_path):
                continue

            staged_file_path = join(staged_dir, rel_path)
            commit_file_path = join(last_commit, rel_path) if last_commit else None

            if exists(staged_file_path):
                if commit_file_path and exists(commit_file_path):
                    if not if_files_equal(staged_file_path, commit_file_path):
                        staged_changes.append(rel_path)
                else:
                    staged_changes.append(rel_path)

                # בדיקה אם שונה מאז שנוסף ל-stage
                if not if_files_equal(path, staged_file_path):
                    modified_not_staged.append(rel_path)
            else:
                # לא ב-stage ולא ב-commit → untracked
                if not commit_file_path or not exists(commit_file_path):
                    untracked_files.append(rel_path)

    # הדפסה מסודרת
    print("Staged but not committed:", sorted(staged_changes))
    print("Modified but not staged:", sorted(modified_not_staged))
    print("Untracked files:", sorted(untracked_files))
