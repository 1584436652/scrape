import requests
from retry import retry


class ScrapeBase:
    def __init__(self):
        self.headers = {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            ' (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

    @retry(delay=3, tries=3)
    def inspection_request(self, method, timeout=None, data_type=True, **kwargs):
        _method = "GET" if not method else method
        _max_timeout = timeout if timeout else 3
        q = requests.request(method=_method, timeout=_max_timeout, **kwargs)
        assert q.status_code == 200
        return q.json() if data_type else q.text

    def parsing(self):
        pass


if __name__ == '__main__':
    pass



