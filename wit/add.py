# -*- coding: utf-8 -*-
import os
import shutil
from files_func import STAGED_DIR, is_wit_initialized, get_ignored_list, BASE_PATH


def add_to_stage(target):
    if not is_wit_initialized():
        print("Error: Not a wit repository (run init first).")
        return

    ignored = get_ignored_list()

    # אם היעד הוא נקודה (כל התיקייה)
    if target == ".":
        for root, dirs, files in os.walk(BASE_PATH):
            # מסנן תיקיות להתעלמות
            dirs[:] = [d for d in dirs if d not in ignored and not d.startswith('.wit')]

            rel_path = os.path.relpath(root, BASE_PATH)
            target_dir = STAGED_DIR if rel_path == "." else os.path.join(STAGED_DIR, rel_path)

            os.makedirs(target_dir, exist_ok=True)
            for f in files:
                if f not in ignored:
                    shutil.copy2(os.path.join(root, f), os.path.join(target_dir, f))
        print("Successfully added all files to stage.")

    # אם היעד הוא קובץ או תיקייה ספציפית
    elif os.path.exists(target):
        rel_path = os.path.relpath(target, BASE_PATH)
        dest = os.path.join(STAGED_DIR, rel_path)

        if os.path.isdir(target):
            shutil.copytree(target, dest, dirs_exist_ok=True)
        else:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(target, dest)
        print(f"Added {target} to stage.")
    else:
        print(f"Error: Path {target} does not exist.")