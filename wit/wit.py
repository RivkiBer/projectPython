# -*- coding: utf-8 -*-

import init as init_module
import add as add_module
import status as status_module



def commits():
    pass
#שולח לדף COMMIT

def status():
    status_module.show_status()
    #שולח לדף STATUS


def checkout():
    print()
    #שולח לדף CHECKOUT


def init():
    init_module.create_init("Z:\יד תשפו\רובינסקי חנה\python\PythonProject\projectPython\wit")
    #שולח לדף INIT



def add():
    add_module.add_to_stage("Z:\יד תשפו\רובינסקי חנה\python\PythonProject\projectPython\wit\\add.py")


add()
