# -*- coding: utf-8 -*-
import os


<<<<<<< HEAD
def create_init(path2):
    print(path2)
=======
def create_init(path):
    print(path)
>>>>>>> main
    if os.path.exists('.wit'):
        print(os.path)
        print("you already do init")
        return

<<<<<<< HEAD
    os.makedirs(f"{path2}/.wit/staged_file", exist_ok=True)
    os.makedirs(f"{path2}/.wit/commits", exist_ok=True)
    with open(f"{path2}/.wit/commits/head.txt", "w") as file:
        file.write("")

    with open(f"{path2}/.wit/.witignore.txt", "w") as file:
        file.write("__pycache__\n")
        file.write("*.pyc\n")
        file.write(".idea\n")
        file.write("init.pyc\n")
=======
    os.makedirs(f"{path}/.wit/staged_file", exist_ok=True)
    os.makedirs(f"{path}/.wit/commits", exist_ok=True)
    with open(f"{path}/.wit/commits/head.txt", "w") as file:
        file.write("")

    with open(f"{path}/.wit/.witignore.txt", "w") as file:
        file.write("")
>>>>>>> main
    print("the initial succses")
