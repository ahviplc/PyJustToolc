import os
import utoolc


# # 如果utoolc/__init__.py:23中__all__去掉 get_random 则不会找到Ta【NameError: name 'get_random' is not defined】
# from utoolc import *
# def test():
#     utils.print_a_line()
#     print(__version__)
#     print(get_random.get_random_str_with_counts(5))
#     utils.print_a_line()

def test2():
    # 使用相对路径
    utoolc.do.do_cverter('markdown', 'rst', '../README.md', '../README_ok.rst')
    utoolc.do.do_cverter("rst", "markdown", '../README.rst', '../README_ok.md')


def test3():
    project_path = os.path.abspath('..')  # C:\_developSoftKu\ideaIU-2019.1.3.win\#CodeKu\pythonKu\PyJustToolc
    print(project_path)
    # 使用绝对路径
    utoolc.do.do_cverter('markdown', 'rst', project_path + '\\README.md', project_path + '\\README_ok2.rst')
    utoolc.do.do_cverter("rst", "markdown", project_path + '\\README.rst', project_path + '\\README_ok2.md')


if __name__ == '__main__':
    # test()
    # test2()
    # test3()
    pass
