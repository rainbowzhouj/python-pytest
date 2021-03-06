#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml

from pythoncode.calculator import Calculator


# 解析测试数据文件
def get_datas():
    with open("./datas/calc.yml", encoding='utf-8')as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    sub_datas = datas['sub']['datas']
    mul_datas = datas['mul']['datas']
    div_datas = datas['div']['datas']
    # print(add_datas)
    # print(add_ids)
    return [add_datas, add_ids, sub_datas, mul_datas, div_datas]


# 解析测试步骤文件
def steps(addstepsfile, calc, a, b, expect):
    with open(addstepsfile)as f:
        steps = yaml.safe_load(f)
        for step in steps:
            if 'add' == step:
                print("step:add")
                result = calc.add(a, b)
            elif 'add1' == step:
                print("step:add1")
                result = calc.add1(a, b)
            assert expect == result


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', get_datas()[0],
                             ids=get_datas()[1])
    def test_add(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert result == expect
        # if a & b is str:
        #     print("参数类型应为数值类型")
        # else:
        #     result = self.calc.add(a, b)
        #     assert result == expect

    # @pytest.mark.parametrize('a,b,expect', [
    #     [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]
    # ])
    # def test_add_float(self, a, b, expect):
    #     result = self.calc.add(a, b)
    #     assert round(result, 2) == expect
    # assert 2 ==self.calc.add(1,1)
    # assert 3 ==self.calc.add1(1,2)
    # assert 0 ==self.calc.add(-1,1)
    @pytest.mark.parametrize('a,b,expect', get_datas()[4])
    def test_div(self, get_calc, a, b, expect):
        result = get_calc.div(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', get_datas()[4])
    def test_div_zero(self, get_calc, a, b, expect):
        with pytest.raises(ZeroDivisionError):
            # self.calc.div(a, b)
            result = get_calc.div(a, b)
            assert result == expect

    def test_add_steps(self, get_calc):
        a = 1
        b = 1
        expect = 2
        steps("./steps/add_steps.yml", get_calc, a, b, expect)

    @pytest.mark.parametrize('a,b,expect', get_datas()[2])
    def test_sub(self, get_calc, a, b, expect):
        result = get_calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', get_datas()[3])
    def test_mul(self, get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        assert result == expect

        # @pytest.mark.parametrize('a,b,expect', [[2, 1, 2], [200, 100, 2], [0.2, 0.1, 2], [-2, -1, 2], [1, 0, 1],
    #                                         ['he', 'llo', 'python']],
    #                          ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case', 'str_case'])
    # def test_div(self, a, b, expect):
    #     if b == 0:
    #         print("除数不能为0")
    #     elif a & b is str:
    #         print("参数类型应为数值类型")
    #     else:
    #         result = self.calc.div(a, b)
    #         assert result == expect
