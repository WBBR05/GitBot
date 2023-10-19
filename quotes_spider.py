from pathlib import Path
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://www.grelleforelle.com/programm/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

#####Terminal command#####
#prefix = 'https://www.grelleforelle.com/project/'
#links = [link for link in response.css('a::attr(href)').extract() if link.startswith(prefix)]
#for link in links:
#    print(link)