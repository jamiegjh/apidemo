# conftest.py
import pytest
from apiTestFramework.api.login import LoginAPI
from apiTestFramework.config import ADMIN_USERNAME, ADMIN_PASSWORD

@pytest.fixture(scope="session")  # scope="session"：整个测试会话只执行1次
def login_token():
    """全局Fixture：登录并返回Token，所有用例共享"""
    print("\n===== 执行前置依赖：登录获取Token =====")
    login_api = LoginAPI()
    token = login_api.login_get_token(
        username=ADMIN_USERNAME,
        password=ADMIN_PASSWORD
    )
    yield token  # 生成Token供用例使用
    print("\n===== 测试会话结束：Token失效 =====")

# 可选：封装带Token的请求头Fixture（进一步简化用例）
@pytest.fixture(scope="session")
def auth_headers(login_token):
    """全局Fixture：返回带Token的请求头"""
    return {"Authorization": token, "Content-Type": "application/json"}