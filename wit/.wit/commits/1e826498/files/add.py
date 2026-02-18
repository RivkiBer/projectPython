# -*- coding: utf-8 -*-
import os
import shutil
import click
from files_func import get_paths, is_wit_initialized, get_ignored_list, BASE_PATH as DEFAULT_BASE_PATH

def add_to_stage(target, base_path=None):
    if not is_wit_initialized(base_path):
        click.echo("Error: Not a wit repository (run init first).")
        return

    _, STAGED_DIR, _, _, _ = get_paths(base_path)
    BASE_PATH = base_path or DEFAULT_BASE_PATH
    ignored = get_ignored_list(base_path)

    if target == ".":
        for root, dirs, files in os.walk(BASE_PATH):
            dirs[:] = [d for d in dirs if d not in ignored and not d.startswith('.wit')]
            rel_path = os.path.relpath(root, BASE_PATH)
            target_dir = STAGED_DIR if rel_path == "." else os.path.join(STAGED_DIR, rel_path)
            os.makedirs(target_dir, exist_ok=True)
            for f in files:
                # skip ignored files
                if f not in ignored:
                    shutil.copy2(os.path.join(root, f), os.path.join(target_dir, f))
        click.echo("Successfully added all files to stage.")

    elif os.path.exists(target):
        rel_path = os.path.relpath(target, BASE_PATH)
        dest = os.path.join(STAGED_DIR, rel_path)
        if os.path.isdir(target):
            shutil.copytree(target, dest, dirs_exist_ok=True)
        else:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(target, dest)
        click.echo(f"Added {target} to stage.")
    else:
        click.echo(f"Error: Path {target} does not exist.")
