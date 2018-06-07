#下载器
import urllib.request


class HtmlDownloader(object):
    def download(self, url):
        if url is None: return None
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        if response.getcode() != 200:
            return None
        return response.read()#.decode('utf-8')