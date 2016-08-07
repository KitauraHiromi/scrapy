# coding: utf-8
from datetime import datetime

import scrapy


# SitemapSpiderを継承する
class CNETSpider(scrapy.spiders.SitemapSpider):
    name = "cnet"
    allowed_domains = ["www.cnet.com"]
    sitemap_urls = (
        # ここにはrobots.txtのURLを指定してもよいが、
        # 無関係なサイトマップが多くあるので、今回はサイトマップのURLを直接指定する。
        'http://www.cnet.com/sitemaps/news.xml',
    )
    sitemap_rules = (
        # 正規表現 '/news/' にマッチするページをparse_news()メソッドでパースする
        (r'/news/', 'parse_news'),
    )

    def parse_news(self, response):
        yield {
            # h1要素の文字列を取得する
            'title': response.css('h1::text').extract_first(),
            # div[itemprop="articleBody"]の直下のp要素以下にある全要素から文字列を取得して結合する
            'body': ''.join(response.css('div[itemprop="articleBody"] > p ::text').extract()),
            # time[itemprop="datePublished"]のclass属性にUTCの時刻が格納されているので、パースする
            'time': datetime.strptime(
                response.css('time[itemprop="datePublished"]::attr(class)').extract_first(),
                '%Y-%m-%d %H:%M:%S'
            ),
        }