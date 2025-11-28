import requests
from typing import Dict, Optional

def send_request(
    method: str,
    url: str,
    json: Optional[Dict] = None,
    params: Optional[Dict] = None,
    headers: Optional[Dict] = None,
    timeout: int = 10
) -> requests.Response:
    """公共请求工具：支持GET/POST等方法"""
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            json=json,
            params=params,
            headers=headers,
            timeout=timeout
        )
        response.raise_for_status()  # 抛出HTTP错误（如404/500）
        return response
    except Exception as e:
        raise RuntimeError(f"请求失败：{str(e)}") from e