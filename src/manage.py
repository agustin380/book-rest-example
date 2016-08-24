import click

from app.api import app
from app import settings


@click.group()
def cmds():
    pass


@cmds.command()
@click.option('--port', default=5000, type=int,
              help='Set server port')
@click.option('--host', default='0.0.0.0', type=str,
              help='Set server host')
@click.option('--debug', default=False,
              help='Set server debug')
def runserver(port, host, debug):
    click.echo('Start server at: {}:{}'.format(host, port))
    app.run(host=host, port=port, debug=debug)

@cmds.command()
def syncdb():
    from app.models import db
    db.create_all()

@cmds.command()
def test():
    import unittest

    loader = unittest.TestLoader()
    tests = loader.discover('app.tests')
    testRunner = unittest.runner.TextTestRunner()
    testRunner.run(tests)


if __name__ == "__main__":
    cmds()
