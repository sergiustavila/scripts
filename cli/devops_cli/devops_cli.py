#! /usr/bin/env python3

import click
import psutil
import subprocess

@click.group()
def cli():
    """Simple cli"""
    pass

@cli.command("disk_sdk", short_help="Show disk Information using python sdk")
def disk_sdk():
    click.echo(psutil.disk_usage("/"))

@cli.command("disk_cmd", short_help="Show disk Information")
def disk_cmd():
    click.echo(subprocess.run(["df", "-h"]))

if __name__ == '__main__' :
    cli()