def main():
    print(greet("Alice"))
    print("-" * 20)
    print(add_numbers(5, 7))

def log_execution(func):
    """
    A decorator that logs the start and end of a function's execution.
    """
    def wrapper(*args, **kwargs):
        print(f"INFO: Calling function '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"INFO: Finished executing function '{func.__name__}'.")
        return result
    return wrapper

@log_execution
def greet(name):
    return f"Hello, {name}!"

@log_execution
def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    main()
