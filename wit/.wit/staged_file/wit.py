# -*- coding: utf-8 -*-
<<<<<<< HEAD
import click
import init as init_module
import add as add_module
import commit as commit_module
import status as status_module

@click.group()
def cli():
    """WIT - מערכת ניהול גרסאות פשוטה"""
    pass

@cli.command()
def init():
    """אתחול ריפוזיטורי"""
    init_module.create_init(r"C:\Users\PC\Desktop\projectPython\wit")

@click.command()
@click.argument('file_name')
def add(file_name):
    """הוספת קבצים ל-stage"""
    add_module.add_to_stage(file_name)

@cli.command()
@click.argument('message')
def commit(message):
    """יצירת commit חדש עם הודעה"""
    commit_module.create_commit(message)

@cli.command()
def status():
    """הצגת סטטוס הקבצים"""
    status_module.show_status()

@cli.command()
@click.argument('commit_id')
def checkout(commit_id):
    """חזרה לקומיט מסוים"""
    print(f"Checkout ל-commit {commit_id}")
    # כאן אפשר לקרוא לפונקציה המתאימה שלך
cli.add_command(init)
cli.add_command(add)
cli.add_command(commit)
cli.add_command(status)
cli.add_command(checkout)
if __name__ == "__main__":
    cli()
=======

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


add()
>>>>>>> main
