import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  #url管理器
        self.downloader = html_downloader.HtmlDownloader()  #下载器
        self.parser = html_parser.HtmlParser()  #解析器
        self.outputer = html_outputer.HtmlOutputer()  #输出器

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)  #将要爬取的地址添加到url里面
        while self.urls.has_new_url():  #如果还存在未爬取的 url 页面
            try:
                new_url = self.urls.get_new_url()  #获取一个新的url
                print('count%d:%s' % (count, new_url))
                html_cont = self.downloader.download(new_url)  #爬取页面数据 下载页面
                new_urls, new_data = self.parser.parse(
                    new_url, html_cont)  #解析数据 拿到新的url 和数据
                self.urls.add_new_urls(new_urls)  #将新的url添加到待爬取的urls中
                self.outputer.collect_data(new_data)  #清洗数据
                if count >= 10:
                    break
                count = count + 1
            except:
                print('爬取失败')

        self.outputer.output_html()  #保存输出数据


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    spider = SpiderMain()
    spider.craw(root_url)