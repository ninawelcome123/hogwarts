from commonLib.decodeApi import DecodeApi
from utils.read_yaml import read_yaml
import pytest
import allure
from pathlib import Path
import os

cases, params = read_yaml(r'D:\Code\frameworkLearn20211130\data\encodeApi.yaml')
myparam = list(params)

@allure.epic("测试解密")
class TestEncode:
    @allure.story("base64解密测试")
    @pytest.mark.parametrize('data,expected', myparam, ids=cases)
    def test_encode(self, data, expected):
        actual = DecodeApi().send(data)
        print(">>>>>>>>>>>>>>>>>>")
        print(actual)
        print(">>>>>>>>>>>>>>>>>>")
        print(expected)
        assert actual == expected


if __name__ == '__main__':
    # cases, params = read_yaml('data/encodeApi.yaml')
    # myparam = list(params)
    # print(myparam)

    my_file1 = Path("./result")
    my_file2 = Path("./report")
    # if my_file1.exists():
    #     os.system("rm -rf ./result")
    # if my_file2.exists():
    #     os.system("rm -rf ./report")
    if my_file1.exists():
        os.system("rmdir ./result")
    if my_file2.exists():
        os.system("rmdir ./report")
    # 借助框架allure-pytest使用allure生成测试报告.
    pytest.main(["-v","-s","test_sent.py","--alluredir=./result"])
    # 两种方法生成及查看报告
    # 方法一：生成直接查看
    os.system("allure serve ./result")
    # 方法二：先生成，再查看
    # os.system("allure generate ./result -o ./report --clean")
    # os.system("allure open -h 127.0.0.1 -p 8883 ./report")

