__author__ = 'Alex Florez'

from urllib import request
import re


def lookip(url):
    u = request.urlopen(url)
    html = u.read()
    # b'{"ip":"111.222.111.222","about":"/about","Pro!":"http://getjsonip.com"}'
    # converting from bytes to UTF-8
    html = html.decode('utf-8')
    # regular expression to match an IP
    match = re.search(r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}', html)
    if match:
        return match.group()

if __name__ == '__main__':
    urldir = 'http://jsonip.com/'
    myip = lookip(urldir)
    print(myip)
