import time


def hello():
    time.sleep(2)
    print("I'm a function")


class TestClass:
    def method1(self):
        time.sleep(2)
        print("method1")

    def method2(self):
        time.sleep(1)
        print("method2")