from base import ScrapeBase


class AntiSpider3(ScrapeBase):
    anti3_url = "https://antispider3.scrape.center/api/book/?limit=18&offset=0"

    def parsing(self):
        d = self.inspection_request('GET', url=AntiSpider3.anti3_url)
        results = d["results"]
        for r in results:
            print(r["name"])


if __name__ == '__main__':
    an3 = AntiSpider3()
    an3.parsing()
