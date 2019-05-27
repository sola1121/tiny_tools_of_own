#!/usr/bin/env python3
# coding: utf-8

import os
import sys


pkg = str()
pypi = r"https://pypi.tuna.tsinghua.edu.cn/simple/"

if len(sys.argv) == 2:
    pkg = sys.argv[1]
else:
    pkg = input(">>> Package Name: ")


os.system("pip3 install -i %s %s" % (pypi, pkg))
