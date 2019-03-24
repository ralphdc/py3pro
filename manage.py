#!/usr/bin/env python3


import click


@click.group()
def cli():
    pass



@cli.command()
@cli.option('--action', default='df', help="select command action...")
def zihan():
    pass

