#!/usr/bin/env python
# _*_coding:utf-8_*_

# 完整程序如下：
import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        #r.encoding ='utf-8'
        return r.text
    except:
        return ''


def printAPPName(html):
    try:
        pattern = re.compile(r'{"im:name":{"label":(.*?)}, "rights"', re.S)
        # 如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。
        # 而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配
        APPName = re.findall(pattern, str(html))
        return 'APPName:' + str(APPName)
    except:
        return ''


def fillUnivlist(titles, comments, stars, html):
    try:
        pattern = re.compile(r'"title":{"label":(.*?)}, "content"', re.S)  # 提取标题
        nbaInfo = re.findall(pattern, str(html))  # 提取title

        # findStr = '"title":{"label":'
        # nbaInfo = nbaInfo1[nbaInfo1.find(findStr)+len(findStr):]
        patternFloor = re.compile(r'"content":{"label":(.*?), "attributes":{"type":"text"}}', re.S)  # 提取content
        floorText = re.findall(patternFloor, str(html))

        patternStar = re.compile(r'"im:rating":{"label":(.*?)}, "id"', re.S)  # 提取星级
        star = re.findall(patternStar, str(html))
        # print(str(star))

        number = len(nbaInfo)
        print(number)
        for i in range(number):
            Info = nbaInfo[i]  # 利用Tools类移除不想要的格式字符
            if i == 0: Info = Info[Info.find('"title":{"label":') + len('"title":{"label":'):]
            # print(Info)
            Info1 = floorText[i]
            Info2 = star[i]
            # print(Info2+"hello")
            titles.append('title:' + Info)
            comments.append('content:' + Info1)
            stars.append('star:' + Info2)
    except:
        return ''


def writeText(titleText, fpath):
    try:
        with open(fpath, 'a', encoding='utf-8') as f:
            f.write(str(titleText) + '\n')
            f.write('\n')
            f.close()
    except:
        return ''


def writeUnivlist(titles, comments, stars, fpath, num):
    with open(fpath, 'a', encoding='utf-8') as f:
        for i in range(num):
            f.write(str(stars[i]) + '\n')
            f.write('*' * 10 + '\n')
            f.write(str(titles[i]) + '\n')
            f.write('*' * 50 + '\n')  # 输入一行*号
            f.write(str(comments[i]) + '\n')
            f.write('*' * 100 + '\n')
        f.close()


def main():
    count = 0
    url = 'https://itunes.apple.com/rss/customerreviews/page=1/id=414478124/sortby=mostrecent/json?l=en&&cc=cn'  # 要访问的网址
    output_file = 'D:/StockInfo.txt'  # 最终文本输出的文件
    html = getHTMLText(url)  # 获取HTML
    APPName = printAPPName(html)
    writeText(APPName, output_file)
    for i in range(10):
        i = i + 1
        titles = []
        comments = []
        stars = []
        url = 'https://itunes.apple.com/rss/customerreviews/page=' + str(
            i) + '/id=414478124/sortby=mostrecent/json?l=en&&cc=cn'
        html = getHTMLText(url)
        fillUnivlist(titles, comments, stars, html)
        writeUnivlist(titles, comments, stars, output_file, len(titles))
        count = count + 1
        print("\r当前进度: {:.2f}%".format(count * 100 / 10), end="")


if __name__ == '__main__':
    main()

# 如果想爬取其他APP只需要改变id的值，如想爬腾讯的，只需将id=414478124换成id=444934666
# 另外本程序是模仿https://www.cnblogs.com/sea-ocean/p/6601421.html的
