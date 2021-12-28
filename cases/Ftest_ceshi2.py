
#自动化测试框架
#unittest
#pytest
#robotframework
#前两款是聚焦在开发者的白盒单元测试
#robotframework主要聚焦在系统测试
import pytest

"""
可以用python编写测试用例，简便易用
可以用文件系统目录层次对应手工测试用例层次结构
灵活的初始化清除机制
可以灵活挑选测试用例执行
利用第三方差价，可以生成不错的报表
"""


"""
编写测试用例代码文件，必须以test_或者_test格式，
"""


def setup_module():
    print('\n *** 初始化-模块 ***')


def teardown_module():
    print('\n ***   清除-模块 ***')


class Test_错误密码02:

    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')

    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')

    def setup_method(self):
        print('\n --- 初始化-方法  ---')

    def teardown_method(self):
        print('\n --- 清除  -方法 ---')

    def test_C001001(self):
        print('\n用例C001001')
        assert 1 == 1

    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2

    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2


class Test_错误密码03:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1

    def test_C001022(self):
        print('\n用例C001022')
        assert 2 == 2
