import unittest
import utools


# 创建Test基础类BaseModuleTest
class BaseModuleTest(unittest.TestCase):
    def test(self):
        utools.utils.print_a_line()
        print(utools.get_random.get_random_str_with_counts(5))
        print(utools.__version__)
        print(utools.utils.get_now_time())
        utools.utils.print_a_line()
        self.assertEqual(1, 1)

    def test4(self):
        print('测试其他...')
        self.assertEqual(1, 1)

    def test5(self):
        utools.easy_say.say_hello_world('LC')


# 如果utools/__init__.py:18中__all__去掉get_random 则不会找到Ta【NameError: name 'get_random' is not defined】
# from utools import *
# def test2():
#     utils.print_a_line()
#     print(__version__)
#     print(get_random.get_random_str_with_counts(5))
#     utils.print_a_line()


def test3():
    utools.utils.print_a_line()
    print(utools.get_random.get_random_str_with_counts(5))
    print(utools.__version__)
    print(utools.utils.get_now_time())
    utools.utils.print_a_line()


if __name__ == '__main__':
    # test() - 用unittest.main()代替
    unittest.main()
    # test2()
    # test3()  # 这个就是test()代码
