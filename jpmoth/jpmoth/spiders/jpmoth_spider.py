import scrapy

from jpmoth.items import jpmothItem
from scrapy.selector import HtmlXPathSelector
import codecs

f = open("jpmoth.txt", "w")

def cvt(str_list):
	for i in range(len(str_list)):
		str_list[i] = str_list[i].encode("shift-jis")
	return str_list


class jpmothSpider(scrapy.Spider):

	name = "jpmoth"
	allowed_domains = ["jpmoth.org"]
	start_urls = ["http://www.jpmoth.org/"]


	custom_settings = {
		"DOWNLOAD_DELAY": 1,
		"DEPTH_LIMIT" : 10,
	}

	def parse(self, response):
		for href in response.xpath("//a/@href"):
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_next_page)

	def parse_next_page(self, response):
		urls = []
		for href in response.xpath("//a/@href"):
			#item["title"] = response.xpath("//title/text()").extract()
			urls.append(response.urljoin(href.extract()))
			#item["desc"] = response.xpath("//p/text()").extract()
		for element in urls:
			f.write(element)
			f.write("\n")
		yield{
			'urls':urls,
		}