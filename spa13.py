from base import ScrapeBase


class Spa13(ScrapeBase):
    spa13_url = "https://spa13.scrape.center/"

    def parsing(self):
        pass


if __name__ == '__main__':
    an3 = Spa13()
    an3.parsing()
