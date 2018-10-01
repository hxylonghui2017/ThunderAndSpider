headers={
    'Cookie':'37cs_user=37cs63629906334; XLA_CI=3e976860bea5549a9a73e10df8153fcd; 37cs_pidx=2; 37cs_show=253%2C75; cscpvrich5041_fidx=3',
    'Host':'www.dytt8.net',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400',
}

other_headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400',
    'Referer':'http://www.dytt8.net/',
    'Host':'www.dytt8.net',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

url_dytt = "http://www.dytt8.net"
re_strIndex = r'>最新电影下载</a>]<a\shref=\'(.*?)\'>(.*?)</a><br'
re_strLink = r'<td\sstyle="WORD-WRAP.*?<a\shref=".*?">(.*?)</a></td>'