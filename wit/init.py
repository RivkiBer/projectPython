# -*- coding: utf-8 -*-
import os

import click


    # ... שאר הקוד
def create_init(path):
    if os.path.exists('.wit'):
        raise click.ClickException("Repository already initialized in this directory.")
    print(path)
    if os.path.exists('.wit'):
        print(os.path)
        print("you already do init")
        return

    os.makedirs(f"{path}/.wit/staged_file", exist_ok=True)
    os.makedirs(f"{path}/.wit/commits", exist_ok=True)
    with open(f"{path}/.wit/commits/head.txt", "w") as file:
        file.write("")

    with open(f"{path}/.wit/.witignore.txt", "w") as file:
        file.write("__pycache__\n")
        file.write("*.pyc\n")
        file.write(".idea\n")
        file.write("init.pyc\n")
    print("the initial succses")
