from rich import print

def handleNonIntArguments(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise NonIntArgumentException()
        return func(*args)

    return wrapper


def NonIntArgumentException(Exception):
    pass

def main():
    @handleNonIntArguments
    def sum(a, b, c):
        return a + b + c

    try:
        result = sum(1, 2, 'a')
        print('This should not print out')
    except NonIntArgumentException as e:
        print('Hooray!')


if __name__ == "__main__":
    main()
