
# -*- coding: utf-8 -*-
import os


def create_init(path):

    os.makedirs(f"{path}/.wit/staged_file", exist_ok = True)
    os.makedirs(f"{path}/.wit/commits", exist_ok= True )
    with open(f"{path}/.wit/commits/head.txt","w") as file:
        file.write("")

    with open(f"{path}/.wit/.witignor.txt", "w") as file:
        file.write("")


