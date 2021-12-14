from base import ScrapeBase


class Spa13(ScrapeBase):
    spa13_url = "https://spa13.scrape.center/js/main.js"

    def parsing(self):
        d = self.inspection_request('GET', url=Spa13.spa13_url, data_type=False)
        print(d)


if __name__ == '__main__':
    an3 = Spa13()
    an3.parsing()
