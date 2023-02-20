""" just a test for workflows """
import sys
import os


def no_op():
    """ a no-op function """
    # this is an inline comment

    print(os.getcwd())


def main():
    """script entry point"""
    print("in main()")
    print('still in main()')


if __name__ == '__main__':
    sys.exit(main())
