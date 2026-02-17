# -*- coding: utf-8 -*-
import click
import init, add, commit, status

@click.group()
def cli():
    """WIT - Simple Version Control System"""
    pass

@cli.command()
def init_cmd():
    init.create_init()

@cli.command()
@click.argument('path')
def add_cmd(path):
    add.add_to_stage(path)

@cli.command()
@click.option('-m', '--message', required=True, help='Commit message')
def commit_cmd(message):
    commit.create_commit(message)

@cli.command()
def status_cmd():
    status.show_status()

if __name__ == "__main__":
    cli()