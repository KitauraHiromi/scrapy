# coding: utf-8
import scrapy


# scrapy.Spiderを継承してBlogSpiderを定義する
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://blog.scrapinghub.com']

    def parse(self, response):
        # トップページをパースするメソッド。
        # URLに /yyyy/mm/ を含むアーカイブページへのリンクを抽出してクロールする。
        # それらのページはparse_titles()メソッドでパースする。
        for url in response.css('ul li a::attr("href")').re(r'.*/\d\d\d\d/\d\d/$'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)

    def parse_titles(self, response):
        # アーカイブページからエントリーのタイトルを取得する
        for post_title in response.css('div.entries > ul > li a::text').extract():
            yield {'title': post_title}