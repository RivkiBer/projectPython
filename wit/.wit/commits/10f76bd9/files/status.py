# -*- coding: utf-8 -*-
import os
import click
from files_func import get_paths, is_wit_initialized, get_ignored_list, get_head_id, compare_files, BASE_PATH as DEFAULT_BASE_PATH

def show_status(base_path=None):
    if not is_wit_initialized(base_path):
        click.echo("Not a wit repository.")
        return

    WIT_DIR, STAGED_DIR, COMMITS_DIR, _, _ = get_paths(base_path)
    BASE_PATH = base_path or DEFAULT_BASE_PATH
    ignored = get_ignored_list(base_path)
    head_id = get_head_id(base_path)
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

            if os.path.exists(staged_path):
                if not commit_path or not os.path.exists(commit_path) or not compare_files(staged_path, commit_path):
                    staged_changes.append(rel_path)
                if not compare_files(full_path, staged_path):
                    modified_not_staged.append(rel_path)
            else:
                if not commit_path or not os.path.exists(commit_path):
                    untracked_files.append(rel_path)
                elif not compare_files(full_path, commit_path):
                    modified_not_staged.append(rel_path)

    click.echo(f"\n--- STATUS  ---")
    click.echo(f"Changes to be committed: {sorted(staged_changes) if staged_changes else 'None'}")
    click.echo(f"Changes not staged:      {sorted(modified_not_staged) if modified_not_staged else 'None'}")
    click.echo(f"Untracked files:         {sorted(untracked_files) if untracked_files else 'None'}\n")
