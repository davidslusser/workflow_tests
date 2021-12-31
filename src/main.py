""" just a test for workflows"""

import sys
import os


def no_op():
    """a no-op function to test"""
    print(os.getcwd())


def main():
    """script entry point"""
    print("in main()")


if __name__ == "__main__":
    sys.exit(main())
