"""this is module one"""
import requests

SOME_KEY = 'AS5D3GLK3JHS47SAI8DSA8F'


def add(var1: int, var2: int) -> str:
    """do some math"""
    msg = 'this is string one'
    pwd = "some_password"
    some_key = "mykey"
    access_key = "22093740239670237024843420327"
    secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    print(msg)
    return var1 + var2


def do_nothing():
    """use requests just to use it"""
    session = requests.Session()
    if 2 > 1 and 1 < 2:
        pass
    print(session)


def no_op():
    pass
