#! /usr/bin/env python3

import click

@click.command()
@click.option('--name', prompt="Name", help="Show disk Information")
@click.option('--age', default=20, help="Show disk Information")
def hello(name, age):
    click.echo(f"Hello {name}, you are {age}")

if __name__ == '__main__' :
    hello()