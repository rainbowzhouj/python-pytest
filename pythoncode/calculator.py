#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


# 被测代码，计算器（加 减 乘 除）
class Calculator():
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

# import pytest
#
# from pythoncode.calculator import Calculator
#
# class TestCalc:
#
#     def setup_class(self):
#         print("开始计算")
#         self.calc = Calculator()
#
#     def teardown_class(self):
#         print("计算结束")
#     # def setup(self):
#     #     print("开始计算")
#     # def teardown(self):
#     #     print("计算结束")
#
#     @pytest.mark.parametrize('a,b,expect',
#                             [[1, 1, 2],
#                             [100, 100, 200],
#                             [0.1, 0.1, 0.2],
#                             [0, 0.1, 0.1],
#                             ['a','b','c']])
#     def test_add(self,a,b,expect):
#         if a or b or expect is str:
#             print("参数类型应为数字")
#         else:
#             result=self.calc.add(a,b)
#             assert result==expect
#     @pytest.mark.parametrize('a,b,expect',
#                             [[1, 1, 1],
#                             [100, 100, 1],
#                             [0, 0.1, 0],
#                             [2,0.1,20],
#                             ['0.5','10',0.05],
#                             [2,3,0.6666666666666666],
#                             [1,0,0]
#                              ])
#     def test_div(self,a,b,expect):
#         if b == 0:
#             print("除数不能为0")
#         elif a or b or expect is str:
#             print("参数类型应为数字")
#         else:
#             result = self.calc.div(a,b)
#             assert result == expect
#         # result = self.calc.div(a,b)
#         # assert result == expect
# if __name__ == '__main__':
# pytest.main(['test_calc.py','-v'])
