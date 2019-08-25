"""
Allow application to be executable through `python -m <appname>`.
"""

from .cli import cli

if __name__ == "__main__":
    cli(prog_name="rabbot")
