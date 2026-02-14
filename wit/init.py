
# -*- coding: utf-8 -*-
import os


def create_init(path):
    if os.path.exists('.wit'):
        print("you already do init")
        return

    os.makedirs(f"{path}/.wit/staged_file")
    os.makedirs(f"{path}/.wit/commits")
    with open(f"{path}/.wit/commits/head.txt","w") as file:
        file.write("")

    with open(f"{path}/.wit/.witignore.txt", "w") as file:
        file.write("")
    print("the initial succses")




