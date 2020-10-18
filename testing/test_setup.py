#!/usr/bin/env python
# -*- coding: utf-8 -*-

def setup_module(self):
    print("资源准备：TestDemo setup_module")


def teardown_module(self):
    print("资源销毁：TestDemo teardown_module")


def test_case1():
    print("test case1")


def setup_function():
    print("开始计算：setup function")


def teardown_function():
    print("结束计算： teardown function")


class TestDemo():

    # 执行类前 分别执行setup_class teardown class，例如：打开浏览器后，登录
    def setup_class(self):
        print("TestDemo setup_class")

    # 每个类里面的方法前后分别执行 setup，teardown ，例如：注销后，关闭浏览器
    def teardown_class(self):
        print("TestDemo teardown_class")

    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")
