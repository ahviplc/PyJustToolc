import unittest
import utoolc


# 创建Test基础类BaseModuleTest
class BaseModuleTest(unittest.TestCase):
    def test(self):
        utoolc.utils.print_a_line()
        print(utoolc.get_random.get_random_str_with_counts(5))
        print(utoolc.__version__)
        print(utoolc.utils.get_now_time())
        utoolc.utils.print_a_line()
        self.assertEqual(1, 1)

    def test4(self):
        print('测试其他...')
        self.assertEqual(1, 1)

    def test5(self):
        utoolc.easy_say.say_hello_world('LC')


# 如果utoolc/__init__.py:18中__all__去掉get_random 则不会找到Ta【NameError: name 'get_random' is not defined】
# from utoolc import *
# def test2():
#     utils.print_a_line()
#     print(__version__)
#     print(get_random.get_random_str_with_counts(5))
#     utils.print_a_line()


def test3():
    utoolc.utils.print_a_line()
    print(utoolc.get_random.get_random_str_with_counts(5))
    print(utoolc.__version__)
    print(utoolc.utils.get_now_time())
    utoolc.utils.print_a_line()


if __name__ == '__main__':
    # test() - 用unittest.main()代替
    unittest.main()
    # test2()
    # test3()  # 这个就是test()代码
