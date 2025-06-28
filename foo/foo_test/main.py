def main():
    print("Hello from foo-test!")
    foo = Foo(12)

class Foo(object):
    def __init__(self, x):
        self.x = x

    def bar(self):
        return self.x
    
if __name__ == "__main__":
    main()
