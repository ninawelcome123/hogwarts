import base64
import json

import requests


class DecodeApi:

    def send(self, data: dict):
        res = requests.request(data["method"], data["url"], headers=data["headers"])
        if str.lower(data["encryption"]) == "base64":
            return json.loads(base64.b64decode(res.content))
        elif str.lower(data["encryption"]) == "private":
            return json.loads(requests.post("url", payload=res.content()))  # 解密动作委托第三方进行


if __name__ == '__main__':
    data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/key.txt",
        "headers":None,
        "encryption": "base64"
    }
    print(DecodeApi().send(data))