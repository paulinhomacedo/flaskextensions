from typer import run

from fexservice.crontab import crontab


def main():
    crontab()

def cli():
    run(main)
