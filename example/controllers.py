from example.logic.logic1 import TestClass, hello
from example.logic.sub_logic.logic2 import moah


def test_controller():
    hello()
    test = TestClass()
    test.method1()
    test.method2()
    print(moah())
    return {"ok": True}
