# -*- coding: utf-8 -*-
import os


def create_init(path2):
    print(path2)
    if os.path.exists('.wit'):
        print(os.path)
        print("you already do init")
        return

    os.makedirs(f"{path2}/.wit/staged_file", exist_ok=True)
    os.makedirs(f"{path2}/.wit/commits", exist_ok=True)
    with open(f"{path2}/.wit/commits/head.txt", "w") as file:
        file.write("")

    with open(f"{path2}/.wit/.witignor.txt", "w") as file:
        file.write("")
    print("the initial succses")
