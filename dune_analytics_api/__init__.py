import os
from getpass import getpass
from argparse import ArgumentParser

from .version import __version__
from .session import Session
from .query_maker import QueryMaker
from .terminal import Terminal


def get_username_password():
    parser = ArgumentParser()
    parser.add_argument('--env', '-e', action='store_true')
    args = parser.parse_args()
    if args.env:
        print("Trying to get username and password from environment...")
        username = os.environ['DUNE_USERNAME']
        password = os.environ['DUNE_PASSWORD']
    else:
        print("Enter username and password to create a session.")
        username = input("Username: ")
        password = getpass("Password: ")
    return username, password


def main():
    username, password = get_username_password()
    print("Creating a session...")
    session = Session.from_login(username, password)
    query_maker = QueryMaker(session)
    terminal = Terminal(query_maker)
    print(f"Welcome to dune-analytics-api (version {__version__}) where you " \
          f"can perform SQL queries as at https://duneanalytics.com/")
    terminal.run()
