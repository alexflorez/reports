__author__ = 'Alex Florez'

from urllib import request
from urllib.error import HTTPError, URLError


def macvendor(macaddress):
    baseurl = 'http://api.macvendors.com/'
    try:
        u = request.urlopen(baseurl + macaddress)
        namevendor = u.read()
        namevendor = namevendor.decode('utf-8')
        return namevendor
    except HTTPError as e:
        #print(e.code)
        return e.code
    except URLError as e:
        #print(e.args)
        return None

if __name__ == '__main__':
    # formatos validos
    # 00-11-22-33-44-55
    # 00:11:22:33:44:55
    # 00.11.22.33.44.55
    # 001122334455
    # 0011.2233.4455
    mac = '40-BA-61-96-BE-12'
    vendor = macvendor(mac)
    print(vendor)
