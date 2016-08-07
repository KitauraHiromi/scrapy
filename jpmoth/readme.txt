http://www.jpmoth.org/の階層の末端にあるhtmlファイルを全て保存し、画像ファイルと合わせてpdf化することで、オフライン蛾図鑑を作成する。

【ファイル説明】
/jpmoth/spiders/jpmoth_spider.py
スパイダプログラム
jpmoth.orgからクローリングし、urlを/jpmoth/jpmoth.txtに記述する
scrapy crawl jpmothで実行

/jpmoth/spiders/jpmoth_get_html.py
スパイダプログラム
/jpmoth/jpmoth_urls.txtからurlを取得、そのurlのhtmlファイルを/htmlに保存する
scrapy crawl jpmoth_get_htmlで実行

/extract_doc.py
htmlファイルから不要な<>を取り除き、/extracted_documents/htmlに保存する

/jpmoth/extract_urls.py
/jpmoth/jpmoth.txtから必要なurlを取得し、jpmoth_urls.txtに保存する

/extracted_documents/get_figure_list.py
/extracted_documents/htmlからhtmlファイルを読み込み、画像ファイルのurlを取得、/extracted_documents/list.txtに保存する。

【使い方】
cd scrapy/jpmoth
scrapy crawl jpmoth				#jpmoth.txtができる
cd jpmoth
python extract_urls.py			#jpmoth_urls.txtができる
cd ..
scrapy crawl jpmoth_get_html	#/htmlに大量に生のhtmlファイルが生成される
python extract_doc.py			#/extracted_documents/htmlに大量に必要な部分だけを抽出したhtmlファイルが生成される
cd extracted_documents
python get_figure_list.py		#/extracted_documents/list.txtに画像ファイルのurlが記述される