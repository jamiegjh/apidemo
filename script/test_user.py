# testcases/test_user.py
import pytest
from apiTestFramework.common.request_util import send_request
from apiTestFramework.config import BASE_URL


def test_get_user_info(login_token):
    """测试获取用户信息（依赖登录Token）"""
    # 直接使用全局Fixture返回的Token
    headers = {
        "Authorization": login_token,
        "Content-Type": "application/json"
    }
    url = f"{BASE_URL}/api/clues/course/list?name=19999922222222"
    response = send_request(method="GET", url=url, headers=headers)

    print(response.json())
    # 断言
    assert response.status_code == 200
    assert response.json().get("code") == 200
