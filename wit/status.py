# -*- coding: utf-8 -*-
import os
from files_func import (
    WIT_DIR, STAGED_DIR, COMMITS_DIR, BASE_PATH,
    get_head_id, get_ignored_list, compare_files, is_wit_initialized
)


def show_status():
    if not is_wit_initialized():
        print("Not a wit repository.")
        return

    ignored = get_ignored_list()
    head_id = get_head_id()
    commit_files_path = os.path.join(COMMITS_DIR, head_id, "files") if head_id else None

    staged_changes = []
    modified_not_staged = []
    untracked_files = []

    for root, dirs, files in os.walk(BASE_PATH):
        dirs[:] = [d for d in dirs if d not in ignored and not d.startswith('.wit')]

        for f in files:
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, BASE_PATH)

            if rel_path.startswith('.wit') or any(p in ignored for p in rel_path.split(os.sep)):
                continue

            staged_path = os.path.join(STAGED_DIR, rel_path)
            commit_path = os.path.join(commit_files_path, rel_path) if commit_files_path else None

            # 1. בדיקת Stage מול Commit
            if os.path.exists(staged_path):
                if not commit_path or not os.path.exists(commit_path) or not compare_files(staged_path, commit_path):
                    staged_changes.append(rel_path)

                # 2. בדיקת עבודה מול Stage
                if not compare_files(full_path, staged_path):
                    modified_not_staged.append(rel_path)
            else:
                # 3. בדיקת Untracked (או שונה מהקומיט האחרון)
                if not commit_path or not os.path.exists(commit_path):
                    untracked_files.append(rel_path)
                elif not compare_files(full_path, commit_path):
                    modified_not_staged.append(rel_path)

    print(f"\n--- STATUS  ---")
    print(f"Changes to be committed: {sorted(staged_changes) if staged_changes else 'None'}")
    print(f"Changes not staged:      {sorted(modified_not_staged) if modified_not_staged else 'None'}")
    print(f"Untracked files:         {sorted(untracked_files) if untracked_files else 'None'}\n")