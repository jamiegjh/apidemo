import pytest
from apiTestFramework.api.login import LoginAPI
from apiTestFramework.utils.read_yaml import read_yaml

class TestLoginParams:
    """登录接口参数化测试（多场景）"""
    def setup_method(self):
        self.login_api = LoginAPI()
        # 获取验证码uuid（所有用例共享）
        captcha_response = self.login_api.get_verify_code()
        self.uuid = captcha_response.json().get("uuid")
        print(self.uuid)
        assert self.uuid is not None, "获取验证码uuid失败"

    # 从YAML读取数据进行参数化
    @pytest.mark.parametrize("case", read_yaml("login_data.yaml"))
    def test_login_params(self, case):
        """参数化测试：覆盖多种登录场景"""
        # 解析测试数据
        username = case["username"]
        password = case["password"]
        code = case["code"]
        expected_code = case["expected_code"]
        expected_msg = case["expected_msg"]
        case_name = case["case_name"]
        print(f"\n测试场景：{case_name}")

        # 调用登录接口
        response = self.login_api.login_yml(
            username=username,
            password=password,
            code=code,
            uuid=self.uuid
        )

        # 断言
        assert response.status_code == 200, f"{case_name} - 响应状态码错误"
        response_json = response.json()
        assert response_json.get("code") == expected_code, f"{case_name} - 接口code错误"
        assert expected_msg in response_json.get("msg", ""), f"{case_name} - 响应消息错误"