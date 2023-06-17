""" just a test for workflows"""

import os
import sys


def no_op():
    """a no-op function"""
    print(os.getcwd())


def main():
    """script entry point"""
    print("in main()")


if __name__ == "__main__":
    sys.exit(main())
