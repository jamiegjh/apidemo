# 接口信息：
# 验证码：
# 地址：http://kdtx-test.itheima.net/api/captchaImage
# 方法：get
#
# 登录：
# 地址：http://kdtx-test.itheima.net/api/login
# 方法：Post
# 请求数据：
# 请求头：Content-Type: application/json
# 请求体：{"username":”admin", "password": " admin123","code":"2", "uuid":"验证码接口返回数据"}
#

# 接口封装时，重点是依据接口文档封装接口信息，需要使用的测试数据是从测试用例传递的、接口方法被调用时需要返回对应的响应结果

# 导包
import requests
from apiTestFramework import config
from apiTestFramework.common.request_util import send_request


# 创建接口类
class LoginAPI:
    # 初始化
    def __init__(self):
        # 指定url基本信息
        # self.url_verify = "http://kdtx-test.itheima.net/api/captchaImage"
        self.url_verify = config.BASE_URL + "/api/captchaImage"
        # self.url_login = "http://kdtx-test.itheima.net/api/login"
        self.url_login = config.BASE_URL + "/api/login"

    # 验证码
    def get_verify_code(self):
        return requests.get(url=self.url_verify)

    # 登录
    def login(self, test_data):
        return requests.post(url=self.url_login, json=test_data)

    def login_yml(self, username: str, password: str, code: str, uuid: str) -> requests.Response:
        """
        登录接口
        :param username: 用户名
        :param password: 密码
        :param code: 验证码（仓库默认可固定为"2"）
        :param uuid: 验证码接口返回的uuid
        :return: 登录响应对象
        """
        headers = {"Content-Type": "application/json"}
        data = {
            "username": username,
            "password": password,
            "code": code,
            "uuid": uuid
        }
        return requests.post(
            url=self.url_login,
            json=data,
            headers=headers
        )

    def get_captcha_uuid(self) -> str:
        """获取验证码UUID（登录依赖）"""
        response = send_request(method="GET", url=self.url_verify)
        uuid = response.json().get("uuid")
        if not uuid:
            raise ValueError("获取验证码UUID失败")
        return uuid

    def login_get_token(self, username: str, password: str) -> str:
        """登录并返回Token（核心公共函数）"""
        uuid = self.get_captcha_uuid()
        login_data = {
            "username": username,
            "password": password,
            "code": "2",  # apidemo仓库默认验证码
            "uuid": uuid
        }
        response = send_request(method="POST", url=self.url_login, json=login_data)
        token = response.json().get("token")
        if not token:
            raise RuntimeError(f"登录失败：{response.json().get('msg')}")
        return token