#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from pythoncode.calculator import Calculator


def test_a():
    print("test case a")


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2], [-1, -1, -2], [1, 0, 1],
                                            ['he', 'llo', 'python']],
                             ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case', 'str_case'])
    def test_add(self, a, b, expect):
        if a & b is str:
            print("参数类型应为数值类型")
        else:
            result = self.calc.add(a, b)
            assert result == expect

    # # 整型
    #     def test_add(self):
    #         #calc = Calculator()
    #         result = self.calc.add(1, 1)
    #         assert result == 2
    # # 长整型
    #     def test_add1(self):
    #         #calc = Calculator()
    #         result = self.calc.add(100, 100)
    #         assert result == 200
    #
    # # 浮点型
    #         def test_add2(self):
    #             #calc = Calculator()
    #             result = self.calc.add(0.1, 0.1)
    #             assert result == 0.2

    def test_sub(self):
        calc = Calculator()
        result = calc.sub(3, 1)
        assert result == 2

    def test_mul(self):
        pass

    @pytest.mark.parametrize('a,b,expect', [[2, 1, 2], [200, 100, 2], [0.2, 0.1, 2], [-2, -1, 2], [1, 0, 1],
                                            ['he', 'llo', 'python']],
                             ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case', 'str_case'])
    def test_div(self, a, b, expect):
        if b == 0:
            print("除数不能为0")
        elif a & b is str:
            print("参数类型应为数值类型")
        else:
            result = self.calc.div(a, b)
            assert result == expect
