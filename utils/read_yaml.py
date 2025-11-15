import yaml
from apiTestFramework import config
import os


def read_yaml(file_name: str) -> list:
    """
    读取YAML测试数据
    :param file_name: data目录下的YAML文件名（如"login_data.yaml"）
    :return: 列表形式的测试数据，每个元素为一组用例数据
    """
    # 拼接YAML文件完整路径
    file_path = os.path.join(config.BASE_DIR, "data", file_name)

    # 读取并解析YAML
    with open(file_path, "r", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)  # 安全加载，避免执行恶意代码

    # 确保返回列表（兼容单组数据场景）
    if not isinstance(yaml_data, list):
        return [yaml_data]
    return yaml_data