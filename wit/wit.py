# -*- coding: utf-8 -*-

import sys
import init as init_module
import add as add_module
import commit as commit_module


def commits():
    commit_module.create_commit(r"C:\שנה ב תכנות\פייתון\wit_project\projectPython\wit")
#שולח לדף COMMIT

def status():
    status_module.show_status()
    #שולח לדף STATUS


def checkout():
    print()
    #שולח לדף CHECKOUT


def init():
    init_module.create_init(r"C:\שנה ב תכנות\פייתון\wit_project\projectPython\wit")
    #שולח לדף INIT



def add():
    add_module.add_to_stage(r"C:\שנה ב תכנות\פייתון\wit_project\projectPython\wit\.")


commits()
