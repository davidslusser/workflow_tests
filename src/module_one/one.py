"""this is module one"""
import requests


def add(var1: int, var2: int) -> int:
    """do some math"""
    msg = "this is string one"
    print(msg)
    return var1 + var2


def do_nothing():
    """use requests just to use it"""
    session = requests.Session()
    print(session)

