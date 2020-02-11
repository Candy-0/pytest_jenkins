import yaml

# 读取文件
with open("./data2.yml", "r",encoding="utf-8") as f:
    # yaml库解析
    value = yaml.safe_load(f)  # 返回字典
    print(value)
    print(type(value))