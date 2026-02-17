# -*- coding: utf-8 -*-
import os
from files_func import WIT_DIR, STAGED_DIR, COMMITS_DIR, HEAD_FILE, WIT_IGNORE


def create_init():
    if os.path.exists(WIT_DIR):
        print("Repository already initialized.")
        return

    os.makedirs(STAGED_DIR, exist_ok=True)
    os.makedirs(COMMITS_DIR, exist_ok=True)

    with open(HEAD_FILE, "w", encoding="utf-8") as f:
        f.write("")

    with open(WIT_IGNORE, "w", encoding="utf-8") as f:
        f.write(".idea\n.vscode\n.gitignore\n__pycache__\ndetails.txt\ninit.pyc\n")



    print("Initialized succseed.")