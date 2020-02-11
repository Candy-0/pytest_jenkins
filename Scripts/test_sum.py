import pytest, yaml, os
from Base.getData import GetData


def get_yaml():
    """
    解析yaml文件
    :param yaml_name:需要解析的yaml文件名字
    :return: 返回yaml文件数据
    """
    # 打开文件
    data_l = []
    data = GetData().get_yaml_data("sum.yml")
    for i in data.values():
            # 解析组装数据
        data_l.append(tuple(i.values()))
    return data_l
    # 组装
    # 返回


# 目标：[(1, 2, 3), (2, 3, 5), (4, 5, 6)]
# data={
# 'test_001': {'a': 1, 'b': 2, 'c': 3},
# 'test_002': {'a': 2, 'b': 3, 'c': 5},
# 'test_003': {'a': 4, 'b': 5, 'c': 6}
# }


class TestSum:

    @pytest.mark.parametrize("a,b,c", get_yaml())
    def test_s(self, a, b, c):
        """
        计算两个数之和等于第三个数   a+b=c
        :param a:
        :param b:
        :param c:
        :return:
        """
        print("\n{}+{}={}".format(a, b, c))
        # 断言
        assert a + b == c
