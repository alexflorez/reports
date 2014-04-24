__author__ = 'Alex Florez'

from urllib import request

def lookip(url):
    u = request.urlopen(url)
    html = u.read()

    # b'{"ip":"111.222.111.222","about":"/about","Pro!":"http://getjsonip.com"}'
    # print(html) # tipo byte
    ip = []
    for i, b in enumerate(html):
        if i < 7:
            continue
        if chr(b) == '"':
            break
        ip.append(chr(b))

    myip = ''.join(b for b in ip)
    return myip

if __name__ == '__main__':
    url = 'http://jsonip.com/'
    myip = lookip(url)
    print(myip)