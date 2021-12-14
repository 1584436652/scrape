import requests

from base import ScrapeBase
from config import USERNAME, PASSWORD


class Login3(ScrapeBase):
    """
    jwt
    """
    login3_url = "https://login3.scrape.center/api/login"
    index_url = "https://login3.scrape.center/api/book/?limit=18&offset=0"

    def login(self):
        data = {
            "username": USERNAME,
            "password": PASSWORD
        }
        req = requests.post(self.login3_url, headers=self.headers, data=data)
        print(req.status_code)
        token = req.json()["token"]
        print(token)
        jwt_headers = {
            "Authorization": f"jwt {token}"
        }
        in_req = requests.get(url=self.index_url, headers=jwt_headers)
        print(in_req.status_code)
        print(in_req.json())


if __name__ == '__main__':
    login3 = Login3()
    login3.login()

