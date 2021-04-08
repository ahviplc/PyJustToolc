# PyJustToolc

```markdown
__________            ____.               __ ___________           .__          
\______   \___.__.   |    |__ __  _______/  |\__    ___/___   ____ |  |   ____  
 |     ___<   |  |   |    |  |  \/  ___/\   __\|    | /  _ \ /  _ \|  | _/ ___\ 
 |    |    \___  /\__|    |  |  /\___ \  |  |  |    |(  <_> |  <_> )  |_\  \___ 
 |____|    / ____\________|____//____  > |__|  |____| \____/ \____/|____/\___  >
           \/                        \/                                      \/ 
                                                                                            
                              Full Of ❤Love❤                                                           
```

banner生成网址:
> http://patorjk.com/software/taag/#p=testall&f=Graffiti&t=PyJustToolc

## fork me
ahviplc/PyJustToolc: ❤PyJustToolc > Python Tools For U (You) ❤
> https://github.com/ahviplc/PyJustToolc

PyJustToolc: ❤PyJustToolc > Go Tools For U (You) ❤
> https://gitee.com/ahviplc/PyJustToolc

## who is who
> 我的Java语言的JustToolc项目地址:

```markdown
ahviplc/JustToolc: ❤JustToolc > Java Tools For U (You) ❤
https://github.com/ahviplc/JustToolc

JustToolc: ❤JustToolc > Java Tools For U (You) ❤
https://gitee.com/ahviplc/JustToolc
```

## slogan
```markdown
❤PyJustToolc > Python Tools For U (You)❤
```

## 打包发布Py模块

> 打包发布Py模块,打包并上传到PyPI

### 具体步骤
```markdown
1. 打包和安装第三方包的工具
我们需要借助setuptools和pip和wheel和twine等工具进行自己包的打包和发布以及安装，如果需要构建成wheel还需要安装wheel模块
如果python版本>=2.7.9或者>=3.4，setuptools和pip是已经安装好的，可能需要进行更新到最新版本
> pip install -U pip setuptools wheel

wheel需要安装
> pip install wheel

twine需要安装
> pip install twine

可以使用包管理工具，例如
> yum install pip
> sudo apt-get install pip

2. 具体一些文件介绍
setup.py
这个文件是打包整个项目最重要的文件，它里面提供了两个主要的功能：

setup()函数，此函数的参数指定了如何配置自己的项目。
命令行工具，包括打包，测试，发布等。可以通过下面的命令查看
查看setup.py工具的帮助信息,如下指令
> python setup.py --help-commands

编译python的包(本质上是新建了一个build目录，而后将指定的packages列表包下的所有".py"文件拷贝过去)
> python setup.py build

将源文件进行打包操作
> python setup.py sdist

基于我们刚刚打包的文件进行安装
> pip install .\dist\PyJustToolc-0.1.0.tar.gz 

卸载咱们刚刚安装的包
> pip uninstall PyJustToolc

setup.cfg
此文件包含了构建时候的一些默认参数例如构建bdist_wheel的时候的--universal参数
--universal的意思是这个二进制包对所有 支持的 Python 版本和 ABI（应用程序二进制接口） 都适用，「 一处打包，到处使用」，
生成的文件名类似：*.whl
[bdist_wheel]
universal=1
这样每次打包的时候就会默认使用--universal参数了，效果类似：
打whl包指令如下:
> python setup.py bdist_wheel --universal

README.md
不用多说

utools/
此文件夹就是utools源代码所在的包。

tests/
此文件夹是一个测试包，包含了一些测试。
```

### setup()的参数
```markdown
setup()的参数

这里只介绍我使用的几个参数，其他参数的具体使用可以参考：https://docs.python.org/3/distutils/setupscript.html

name

versions = "utools"
是整个项目的名字，打包后会使用此名字和版本号。

version

from vaspy import __version__
version = __version__
description

是一个简短的对项目的描述，一般一句话就好，会显示在pypi上名字下端。

long_description

是一个长的描述，相当于对项目的一个简洁，如果此字符串是rst格式的，PyPI会自动渲染成HTML显示。这里可以直接读取README.rst中的内容。

url

包的连接，通常为GitHub上的链接或者readthedocs的链接。

packages

需要包含的子包列表，setuptools提供了find_packages()帮助我们在根路径下寻找包，这个函数distutil是没有的。

setup_requires

这个参数定义了VASPy安装和顺利运行所需要的其他依赖项（最基本的），使用pip安装的时候会对这些依赖项进行安装。
关于这个参数与requirements.txt的区别可以参考：install_requires vs Requirements files

classifier

这个参数提供了一系列的分类，在PyPI上会将其放入不同的目录中讲项目进行归类。
具体的categories的名称和规则参考：https://pypi.python.org/pypi?%3Aaction=list_classifiers

test_suite

这个参数可以帮助我们使用
> python setup.py test
来跑单元测试，再也不需要单独再写一个脚本例如utools_test.py这样来跑单元测试了
```

## bdist命令
> bdist命令是一个二进制分发包，或称作安装程序。该命令可以生成模板操作系统的安装程序。

```markdown
制作windows下的安装包
python setup.py bdist_wininst  # 创建"*.exe"的文件
python setup.py bdist_msi  # 创建"*.msi"的文件 可用
python setup.py bdist --format=msi  # 同样是创建"*.msi"的文件

制作rpm包
> python setup.py bdist_rpm  # 创建"*.rpm"的文件，该命令需要在Linux操作系统上执行！
> python setup.py bdist --format=rpm  # 同上

制作压缩文件
> python setup.py bdist --format=zip  # 创建"*.zip"压缩文件
> python setup.py bdist --format=gztar  # 创建"*.tar.gz"文件
```

## 将python打包成egg包或者whl包(本质上是一个zip文件)
```markdown
安装wheel模块
> pip install wheel

整理好"setup.py"文件

打包whl和egg格式
> python setup.py bdist_egg  # 打"*.egg"的包
> python setup.py bdist_wheel  # 打"*.whl"的包

一次性执行sdist和bdist_wheel两个
> python setup.py sdist bdist_wheel  # 打"*.tar.gz 和 *.whl
```

## 上传
```markdown
> twine upload dist/*

twine 安装： 
> pip install twine

twine 提示输入 pypi 账号和密码，上传成功否就能在自己的pypi账号中看到了。

当你有新版本的时候，你可以使用以下命令 来忽略已经存在的库
> twine upload --skip-existing dist/* 
```

## 待完善,带复看
```markdown
packages=find_packages(where='PyJustToolc', include=('utools','example'),exclude=("*.tests", "*.tests.*", "tests.*", "tests")), # include all packages under automated
```

## 一些链接
```markdown
Python __all__变量用法
http://c.biancheng.net/view/2401.html

打包发布Python模块的方法详解_python_脚本之家 - 此打包根据这个做的
https://www.jb51.net/article/92789.htm

Python的打包工具(setup.py)实战篇 - 尹正杰 - 博客园 - 还有这个 - 很不错,很全
https://www.cnblogs.com/yinzhengjie/p/14124623.html

GitHub - PytLab/VASPy: Manipulating VASP files with Python.
https://github.com/PytLab/VASPy

手把手教你打包Python库并创建自己的PyPI项目 - 简书 - 也可参考
https://www.jianshu.com/p/6019aee27883

GitHub - YaokaiYang-assaultmaster/py3PortScanner: 🎃Port scanner for Python >= 3.0! Faster! Stronger! Better!
https://github.com/YaokaiYang-assaultmaster/py3PortScanner

Python打包指南2021 | Frost's Blog
https://frostming.com/2020/12-25/python-packaging/

使用 twine 上传自己的 python 包到 pypi - leffss - 博客园
https://www.cnblogs.com/leffss/p/12029963.html

GitHub - pypa/twine: Utilities for interacting with PyPI
https://github.com/pypa/twine

GitHub - pdm-project/pdm: A modern Python package manager with PEP 582 support.
https://github.com/pdm-project/pdm

PyPI · The Python Package Index 正式
https://pypi.org/

TestPyPI · The Python Package Index 测试
https://test.pypi.org/

Python包管理工具setuptools之setup函数参数详解 - 一切都是当下 - 博客园
https://www.cnblogs.com/potato-chip/p/9106225.html
```

## about me
```markdown
By LC
寄语:一人一世界,一树一菩提!~LC
Version 0.1.0 From 2021
