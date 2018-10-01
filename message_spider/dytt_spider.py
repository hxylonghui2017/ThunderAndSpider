import requests
import re

from message_spider.spider_config import *
from requests.exceptions import RequestException

class dytt_spider:
    def __init__(self):
        self.url = url_dytt

    def get_html(self, url, headers):
        try:
            response = requests.get(url, headers=headers)
            # Python HTTP库requests中文页面乱码解决方案
            response.encoding = response.apparent_encoding
            if response.status_code == 200:
                return response.text
            return None
        except RequestException:
            return None

    def _get_re_findall_items(self, html, re_str):
        pattern = re.compile(re_str, re.S)
        items = re.findall(pattern, html)
        return items

    def get_index(self, html, re_str):
        items = self._get_re_findall_items(html, re_str)
        for item in items:
            yield {
                "name": item[1],
                "url": url_dytt + item[0]
            }

    def get_thunder_link(self, html, re_str):
        items = self._get_re_findall_items(html, re_str)
        for item in items:
            yield {
                "thunder": item
            }

    def get_all_thunderlink(self):
        index = self.get_html(self.url, headers)
        for item in self.get_index(index, re_strIndex):
            html = self.get_html(item['url'], other_headers)
            if html:
                for x in self.get_thunder_link(html, re_strLink):
                    yield {
                        "影片名：": item["name"],
                        "磁力链接：": x['thunder'],
                    }

if __name__=="__main__":
    dytt = dytt_spider(url_dytt)
    for mess in dytt.get_all_thunderlink():
        print(mess)