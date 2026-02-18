# -*- coding: utf-8 -*-
import os
import shutil
import datetime
import uuid
import click
from files_func import get_paths, BASE_PATH as DEFAULT_BASE_PATH

def create_commit(message, base_path=None):
    _, STAGED_DIR, COMMITS_DIR, HEAD_FILE, _ = get_paths(base_path)

    if not os.path.exists(STAGED_DIR) or not os.listdir(STAGED_DIR):
        click.echo("Nothing to commit, stage is empty.")
        return

    commit_id = str(uuid.uuid4())[:8]
    path = os.path.join(COMMITS_DIR, commit_id)
    os.makedirs(os.path.join(path, "files"))

    for item in os.listdir(STAGED_DIR):
        shutil.move(os.path.join(STAGED_DIR, item), os.path.join(path, "files", item))

    with open(os.path.join(path, "details.txt"), "w", encoding="utf-8") as f:
        f.write(f"Date: {datetime.datetime.now()}\nMessage: {message}\n")

    with open(HEAD_FILE, "w", encoding="utf-8") as f:
        f.write(commit_id)

    click.echo(f"Created commit: {commit_id}")
