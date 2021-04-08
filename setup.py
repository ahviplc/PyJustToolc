#!/usr/bin/env python
import os
from setuptools import setup, find_packages

from utools import __version__ as version
from utools import __author__ as author
from utools import __email__ as email

maintainer = author
maintainer_email = email
author = maintainer
author_email = maintainer_email
description = "❤PyJustToolc > Python Tools For U (You)❤"

# 代码可用
# 有的将README成为其long_description
# here = os.path.abspath(os.path.dirname(__file__))  # 'C:\\_developSoftKu\\ideaIU-2019.1.3.win\\#CodeKu\\pythonKu\\PyJustToolc'
# with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
#     README = f.read()
# with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
#     REQUIREMENTS = f.read()

long_description = """
=====
❤PyJustToolc > Python Tools For U (You)❤
=====
------------
1. Via pip(recommend)::
    pip install utools
2. Via easy_install::
    easy_install utools
3. From source::
    python setup.py install
If you want to use **mayavi** to visualize VASP data, it is recommened to install `Canopy environment <https://store.enthought.com/downloads/#default>`_ on your device instead of installing it manually.
After installing canopy, you can set corresponding aliases, for example:
.. code-block:: shell
    alias canopy='/Users/<yourname>/Library/Enthought/Canopy/edm/envs/User/bin/python'
    alias canopy-pip='/Users/<yourname>/Library/Enthought/Canopy/edm/envs/User/bin/pip'
    alias canopy-ipython='/Users/<yourname>/Library/Enthought/Canopy/edm/envs/User/bin/ipython'
    alias canopy-jupyter='/Users/<yourname>/Library/Enthought/Canopy/edm/envs/User/bin/jupyter'
Then you can install utools to canopy::
    canopy-pip install utools
"""

install_requires = [
    'twine>=3.4.1',
    'pony>=0.7.14',
]

license = 'LICENSE'

keywords = [
    "utools", "PyJustToolc", "Python Tools For U (You)"
]

name = 'PyJustToolc'
platforms = ['win', 'linux']
url = 'https://github.com/ahviplc/PyJustToolc'
download_url = 'https://github.com/ahviplc/PyJustToolc'
classifiers = [
    'Development Status :: 3 - Alpha',
    'Topic :: Text Processing',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7.3',
]

test_suite = 'tests.utools_test'

setup(author=author,
      author_email=author_email,
      description=description,
      license=license,
      long_description=long_description,
      install_requires=install_requires,
      maintainer=maintainer,
      name=name,
      packages=find_packages(exclude=('tests', 'examples')),  # 打包 排除一些
      # package_dir={'': 'utools'},
      package_data={"utools": ['utils/*.py']},  # 这里只是占位 包含utools/utils下所有*.py文件 和 utools下所有*.py文件
      include_package_data=True,  # 默认情况下False 则不包含非python包文件(例如您列出的不在“包中”的测试py文件) 反之包含.
      zip_safe=False,  # 其为False 则出现的不是一个*.egg文件，而是一个文件夹.
      platforms=platforms,
      url=url,
      download_url=download_url,
      version=version,
      test_suite=test_suite,
      classifiers=classifiers)
