#!/usr/bin/env python3


import click


@click.group()
def cli():
    pass



@cli.command()
@click.option('--action', default='df', help="select command action...")
def zihan(action):

    from app import GetHandler

    GetHandler.get_unit(action).run()


if __name__ == '__main__':
    cli()