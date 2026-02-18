# -*- coding: utf-8 -*-
import os
import click
from files_func import WIT_DIR, STAGED_DIR, COMMITS_DIR, HEAD_FILE, WIT_IGNORE, is_wit_initialized

def create_init():
    if is_wit_initialized():
        click.echo("Repository already initialized.")
        return

    os.makedirs(STAGED_DIR, exist_ok=True)
    os.makedirs(COMMITS_DIR, exist_ok=True)

    with open(HEAD_FILE, "w", encoding="utf-8") as f:
        f.write("")

    with open(WIT_IGNORE, "w", encoding="utf-8") as f:
        f.write(".idea\n.vscode\n.gitignore\n__pycache__\ndetails.txt\n")

    click.echo(f"Initialized empty Wit repository in {WIT_DIR}")
