import requests

from base import ScrapeBase
from config import USERNAME, PASSWORD


class Login2(ScrapeBase):
    """
    session
    """
    session = requests.Session()
    login2_url = "https://login2.scrape.center/login?next=/"
    index_url = "https://login2.scrape.center/page/2"

    def login(self):
        data = {
            "username": USERNAME,
            "password": PASSWORD
        }
        req = self.session.post(self.login2_url, headers=self.headers, data=data)
        print(req.status_code)
        print(req.url)
        # cookies = req.cookies
        # print(cookies)
        in_req = self.session.get(url=self.index_url, headers=self.headers, cookies=cookies)
        print(in_req.text)


if __name__ == '__main__':
    login2 = Login2()
    login2.login()

