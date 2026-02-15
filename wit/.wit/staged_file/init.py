# -*- coding: utf-8 -*-
import os


def create_init(path):
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
        file.write("")
    print("the initial succses")
