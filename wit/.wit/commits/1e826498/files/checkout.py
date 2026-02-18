# -*- coding: utf-8 -*-
import os
import shutil
import click
from files_func import get_paths, is_wit_initialized, BASE_PATH as DEFAULT_BASE_PATH

def checkout(commit_id, base_path=None):
    if not is_wit_initialized(base_path):
        click.echo("Not a wit repository.")
        return

    WIT_DIR, STAGED_DIR, COMMITS_DIR, HEAD_FILE, _ = get_paths(base_path)
    repo_root = base_path or DEFAULT_BASE_PATH
    target_commit_dir = os.path.join(COMMITS_DIR, commit_id)
    source_files = os.path.join(target_commit_dir, 'files')

    if not os.path.exists(source_files):
        click.echo(f"Error: Commit {commit_id} not found")
        return

    # ניקוי תיקיית העבודה (לא מוחק תיקיות שמתחילות בנקודה חוץ מ-.wit)
    for item in os.listdir(repo_root):
        if item == '.wit' or item.startswith('.'):
            continue
        item_path = os.path.join(repo_root, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        except (PermissionError, OSError):
            # התעלמות מקבצים שלא ניתן למחוק
            continue

    # העתקת קבצים חזרה
    for item in os.listdir(source_files):
        src = os.path.join(source_files, item)
        dst = os.path.join(repo_root, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

    # עדכון HEAD
    with open(HEAD_FILE, 'w', encoding='utf-8') as f:
        f.write(commit_id)

    # עדכון Stage
    if os.path.exists(STAGED_DIR):
        shutil.rmtree(STAGED_DIR)
    shutil.copytree(source_files, STAGED_DIR)

    click.echo(f"Successfully moved to commit {commit_id}.")
