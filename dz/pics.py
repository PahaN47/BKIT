from urllib import request

def get_pic(url):
    return request.urlopen(url)
    