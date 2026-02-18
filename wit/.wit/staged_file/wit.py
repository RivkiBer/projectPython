# -*- coding: utf-8 -*-
import sys
import click
import init as init_module
import add as add_module
import commit as commit_module
import status as status_module
import checkout as checkout_module

@click.group()
def cli():
    """WIT - מערכת ניהול גרסאות פשוטה"""
    pass

@cli.command()
def init():
    """אתחול מאגר WIT בתיקייה הנוכחית"""
    init_module.create_init()

@cli.command()
@click.argument('file_name')
def add(file_name):
    """הוספת קבצים ל-stage"""
    add_module.add_to_stage(file_name)

@cli.command()
@click.option('-m', '--message', required=True, help='Commit message')
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
    checkout_module.checkout(commit_id)

if __name__ == "__main__":
    cli()
