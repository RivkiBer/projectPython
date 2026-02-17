import os
import shutil
import click

def checkout(commit_id):
    repo_root = os.getcwd()
    wit_dir = os.path.join(repo_root, '.wit')
    target_commit_dir = os.path.join(wit_dir, 'commits', commit_id)
    source_files = os.path.join(target_commit_dir, 'files')

    if not os.path.exists(source_files):
        click.echo(f"Error: Commit {commit_id} not found in {source_files}")
        return

    # ניקוי תיקיית העבודה
    for item in os.listdir(repo_root):
        if item == '.wit':
            continue
        item_path = os.path.join(repo_root, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

    # העתקה חזרה לפרויקט
    for item in os.listdir(source_files):
        src = os.path.join(source_files, item)
        dst = os.path.join(repo_root, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

    # עדכון ה-HEAD (נתיב מדויק לפי הקוד שלך)
    head_path = os.path.join(wit_dir, 'commits', 'head.txt')
    with open(head_path, 'w', encoding='utf-8') as f:
        f.write(commit_id)

    # עדכון ה-Staging Area
    staged_dir = os.path.join(wit_dir, 'staged_file')
    if os.path.exists(staged_dir):
        shutil.rmtree(staged_dir)
    shutil.copytree(source_files, staged_dir)

    click.echo(f"Successfully moved to commit {commit_id}.")