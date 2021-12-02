from base import ScrapeBase


class Spa13(ScrapeBase):
    spa13_url = "https://spa13.scrape.center/"

    def parsing(self):
        d = self.inspection_request('GET', url=Spa13.spa13_url)
        results = d["results"]
        for r in results:
            print(r["name"])


if __name__ == '__main__':
    an3 = Spa13()
    an3.parsing()
