# -*- coding: utf-8 -*-

import add as add_module
import commit as commit_module
import init as init_module
from status import show_status
import checkout as checkout_module

def commits():
    commit_module.create_commit(r"C:\שנה ב תכנות\פייתון\wit_project\projectPython\wit")


#שולח לדף COMMIT

def status():
    show_status()
    #שולח לדף STATUS


def checkout():
    checkout_module.move_checkout('a588ac1e',r"C:\שנה ב תכנות\פייתון\wit_project\projectPython\wit")
    #שולח לדף CHECKOUT



def init():
    init_module.create_init(r"C:\שנה ב תכנות\פייתון\wit_project\projectPython\wit")
    #שולח לדף INIT

###
def add():
    add_module.add_to_stage(r"C:\שנה ב תכנות\פייתון\wit_project\projectPython\wit\.")


status()
