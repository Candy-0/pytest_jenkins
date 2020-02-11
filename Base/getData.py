import os
import yaml


class GetData:
    """解析各种数据文件类"""

    def get_yaml_data(self,yaml_name):
        """
        解析yaml文件
        :param yaml_name:需要解析的yaml文件名字
        :return: 返回yaml文件数据
        """
        # 打开文件
        with open("./Data" + os.sep + yaml_name, 'r') as f:
            # 读取数据
            data = yaml.safe_load(f)  # 返回yaml数据 字典格式
            # print("data={}".format(data))
        return data