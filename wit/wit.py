# import click
#
# from . import init as init_module
# from . import add as add_module
# from . import commit as commit_module
# from . import checkout as checkout_module
# from . import status as status_module
#
# @click.group()
# def cli():
#     """WIT - מערכת ניהול גרסאות פשוטה"""
#     pass
# @cli.command()
# def init():
# #####################################
#     init_module.create_init(r"C:\python\projectPython\wit")
#
# @cli.command()  # שנה מ-@click ל-@cli
# @click.argument('file_name')
# def add(file_name):
#     """הוספת קבצים ל-stage"""
#     add_module.add_to_stage(file_name)
#
# @cli.command()
# @click.argument('message')
# def commit(message):
#     """יצירת commit חדש עם הודעה"""
#     commit_module.create_commit(message)
#
#
# @cli.command()
# def status():
#     """הצגת סטטוס הקבצים"""
#     status_module.show_status()
#
# @cli.command()
# @click.argument('commit_id')
# def checkout(commit_id):
#     """חזרה לקומיט מסוים"""
#     print(f"Checkout ל-commit {commit_id}")
#     # כאן אפשר לקרוא לפונקציה המתאימה שלך
# cli.add_command(init)
# cli.add_command(add)
# cli.add_command(commit)
# cli.add_command(status)
# cli.add_command(checkout)
# if __name__ == "__main__":
#     cli()
# -*- coding: utf-8 -*-
import click
import os

import init as init_module
import add as add_module
import commit as commit_module
# ... וכן הלאה
@click.group()
def cli():
    """WIT - מערכת ניהול גרסאות פשוטה"""
    pass

@cli.command()
def init():
    """אתחול מאגר WIT בתיקייה הנוכחית"""
    # במקום נתיב קבוע, אנחנו לוקחים את התיקייה שבה המשתמש נמצא כרגע
    current_directory = os.getcwd()
    init_module.create_init(current_directory)
    click.echo(f"Initialized empty Wit repository in {current_directory}")

@cli.command()
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
    click.echo(f"Checking out to commit {commit_id}...")
    # כאן תקרא לפונקציה מ-checkout_module

# הערה: כשמשתמשים ב-@cli.command() אין צורך להוסיף cli.add_command(init) בסוף,
# ה-decorator כבר עושה את זה אוטומטית. אפשר למחוק את השורות האלו.

if __name__ == "__main__":
    cli()