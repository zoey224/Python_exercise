import requests
import re
import urllib.request
import datetime


def get_id(url):
    page = requests.get(url).content.decode("utf-8");
    reg = '<url>(.*)</url>'
    id =re.findall(reg, page)[0]
    return id

def combine_url(id):
    header = "http://s.cn.bing.net"
    pic_url=header+id
    return pic_url

def main():
    url = "http://cn.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1"
    path = r'/BingPics/pic'
    time = datetime.date.today()
    pic_id = get_id(url)
    pic = combine_url(pic_id)
    urllib.request.urlretrieve(pic, path + str(time) + '.jpg')
    print(str(time)+" is finished")

if __name__ == '__main__':
    main()