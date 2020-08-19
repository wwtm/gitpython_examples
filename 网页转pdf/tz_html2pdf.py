#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 18:42
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : tz_html2pdf.py
# @Software: PyCharm

# 导入库
import pdfkit

# 这里传入我知乎专栏文章url，转换为pdf
pdfkit.from_url(r'https://mp.weixin.qq.com/s?__biz=MzAwNjQyNjg2Mg==&mid=2649895372&idx=1&sn=2c77c0ddc20bcabdc5c2506b0795b607&chksm=830b084db47c815b8213aa8b1ca79a38ecea93e771757e505016f28274fd755feb16da1e1a5d#rd', 'tianzuo.pdf')
# pdfkit.from_file('wenzhang.html','tianzuo1.pdf')
# pdfkit.from_string('Hello Pdf!','tianzuo2.pdf')