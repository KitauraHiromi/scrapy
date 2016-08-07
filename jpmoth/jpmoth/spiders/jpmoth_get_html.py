import scrapy
import re
class DmozSpider(scrapy.Spider):
    name = "jpmoth_get_html"
    allowed_domains = ["jpmoth.org"]
    start_urls = []

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
    }

    with open("C:\Users\hiromi\scrapy\jpmoth\jpmoth\jpmoth_urls.txt") as url_list:
        for line in url_list:
            start_urls.append(line.rstrip())

    def parse(self, response):
        split = response.url.split("/")
        filename = "html/"
        for element in split[3:]:
            filename += element
            if(re.search(r"html", element)):
                pass
            else:
                filename += "%"
        with open(filename, 'wb') as f:
            f.write(response.body)