# -*- coding: utf-8 -*-
import os
import shutil
import datetime
import uuid
from files_func import STAGED_DIR, COMMITS_DIR, HEAD_FILE


def create_commit(message):
    if not os.path.exists(STAGED_DIR) or not os.listdir(STAGED_DIR):
        print("Nothing to commit, stage is empty.")
        return

    commit_id = str(uuid.uuid4())[:8]
    path = os.path.join(COMMITS_DIR, commit_id)
    os.makedirs(os.path.join(path, "files"))

    # העברה פיזית (shutil.move) מה-Stage לקומיט (מנקה את ה-Stage)
    for item in os.listdir(STAGED_DIR):
        shutil.move(os.path.join(STAGED_DIR, item), os.path.join(path, "files", item))

    with open(os.path.join(path, "details.txt"), "w", encoding="utf-8") as f:
        f.write(f"Date: {datetime.datetime.now()}\nMessage: {message}\n")

    with open(HEAD_FILE, "w", encoding="utf-8") as f:
        f.write(commit_id)

    print(f"Created commit: {commit_id}")