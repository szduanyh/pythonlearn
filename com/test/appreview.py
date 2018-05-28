#!/usr/bin/env python
# _*_coding:utf-8_*_

# 完整程序如下：

import sys

sys.path.append('../')

import random
import configparser
import requests
import json
import jieba.analyse


# 返回一个随机的请求头 headers
def getheaders():
    user_agent_list = [
        'iTunes/12.7.4 (Windows; Microsoft Windows 10 x64 Enterprise Edition (Build 16299); x64) AppleWebKit/7604.5002.1000.1 (dt:2)',
        'iTunes/12.7.3 (Windows; Microsoft Windows 10 x64 Enterprise Edition (Build 16299); x64) AppleWebKit/7604.5002.1000.1 (dt:2)',
        'iTunes/12.4.3 (Windows; Microsoft Windows 10 x64 Enterprise Edition (Build 16299); x64) AppleWebKit/7604.5002.1000.1 (dt:2)',
        'iTunes/12.1.3 (Windows; Microsoft Windows 10 x64 Enterprise Edition (Build 16299); x64) AppleWebKit/7604.5002.1000.1 (dt:2)',
        'iTunes/12.7.4 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/7604.5002.1000.1 (dt:2)',
        'iTunes/12.7.3 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/7604.5002.1000.1 (dt:2)',
        'iTunes/12.4.3 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/7604.5002.1000.1 (dt:2)',
        'iTunes/12.1.3 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/7604.5002.1000.1 (dt:2)',
        'iTunes/11.0 (Windows; Microsoft Windows 10 x64 Enterprise Edition (Build 16299); x64) AppleWebKit/7604.5002.1000.1',
        'iTunes/12.7 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/536.36',
        'iTunes/11.0 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/536.36',
        'iTunes/11.0 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/537.40',
        'iTunes/11.0 (Windows; Microsoft Windows 7 Business Edition Service Pack 1 (Build 7601)) AppleWebKit/536.27.1'
    ]
    UserAgent = random.choice(user_agent_list)
    headers = {'User-Agent': UserAgent}
    return headers


def getproxip(path):
    with open(path, 'r', encoding='utf-8') as f:
        txt = []
        for s in f.readlines():
            txt.append(s.strip())
    if len(txt):
        return random.choice(txt)
    return ''


# 清空文档
def truncatefile(path):
    with open(path, 'w', encoding='utf-8') as f:
        f.truncate()


def download_page(url, proxip, headers):
    """获取url地址页面内容"""
    # proxies = {"http": "http://" + proxip, "https": "http://" + proxip}  # 代理ip
    # data = requests.get(url, proxies=proxies, headers=headers).content
    data = requests.get(url, headers=headers).content
    return data


def download_info(url):
    """获取url地址页面内容"""
    data = requests.get(url).content
    return data


def writeReview(html, fpath):
    try:
        viewdata = json.loads(html)
        if len(viewdata['userReviewList']):
            with open(fpath, 'a', encoding='utf-8') as f:
                for item in viewdata['userReviewList']:
                    f.write(item.get('title', '') + '\n')
                    f.write(item.get('body', '') + '\n')
                    f.write('-' * 100 + '\n')
                    # f.write('rating:' + str(item.get('rating', 'NA')) + '\n')
                    # f.write('title:' + item.get('title', '') + '\n')
                    # f.write('body:' + item.get('body', '') + '\n')
                    # f.write('-' * 100 + '\n')
                f.close()
            return True
        return False
    except:
        return False


def writeDescription(html, fpath):
    try:
        viewdata = json.loads(html)
        if len(viewdata):
            filename = fpath + '_1.txt'
            truncatefile(filename)
            trackName = viewdata['results'][0].get('trackName', '')
            description = viewdata['results'][0].get('description', '')
            tags = analyseContent(trackName + description)
            with open(filename, 'a', encoding='utf-8') as f:
                f.write('trackName:' + trackName + '\n')
                f.write('description:' + description + '\n')
                f.write('-' * 100 + '\n')
                f.write(",".join(tags))
                f.close()
            return True
        return False
    except:
        return False


def downApp(appid, appfile):
    proxippath = 'ip.txt'  # 存放代理ip的文档path
    headers = getheaders()  # 定制请求头
    proxip = getproxip(proxippath)
    infourl = 'http://itunes.apple.com/cn/lookup?id=' + str(appid)
    infohtml = download_info(infourl)
    retcode = writeDescription(infohtml, appfile)
    if retcode:
        page = 0
        pagesize = 500
        filename = appfile + '_2.txt'
        truncatefile(filename)
        while True:
            page += 1
            startindex = (page - 1) * pagesize
            endindex = startindex + pagesize
            url = 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?cc=cn&id=' + str(
                appid) + '&displayable-kind=11&startIndex=' + str(startindex) + '&endIndex=' + str(
                endindex) + '&sort=0&appVersion=all'
            html = download_page(url, proxip, headers)
            retcode = writeReview(html, filename)
            if not retcode:
                break
            print("\r%s当前进度第: %d页" % (appid, page))
        print("评论分词操作")
        content = open(filename, 'rb').read()
        tags = analyseContent(content, True)
        with open(filename, 'a', encoding='utf-8') as f:
            for tag in tags:
                f.write("tag: %s\t\t weight: %f\n" % (tag[0], tag[1]))
            f.close()


# 分词
def analyseContent(content, withWeight=False):
    tags = jieba.analyse.extract_tags(content, topK=1000, withWeight=withWeight)
    return tags


def main():
    conf = configparser.ConfigParser()  # 生成conf对象
    conf.read('config.ini', encoding="utf-8-sig")  # 读取ini配置文件
    AppID = conf.get('AppInfo', "AppID")
    AppFile = conf.get('AppInfo', "AppFile")
    print(AppID, AppFile)
    downApp(AppID, AppFile)
    print('爬取完成')
    # downApp(AppID, AppFile)
    # print(AppID, AppFile)

    # appid = 414478124
    # page = 0
    # pagesize = 100
    # count = 0
    # output_file = 'AppView.txt'  # 最终文本输出的文件
    # proxippath = 'ip.txt'  # 存放代理ip的文档path
    # headers = getheaders()  # 定制请求头
    # proxip = getproxip(proxippath)
    # while True:
    #     page += 1
    #     startindex = (page - 1) * pagesize
    #     endindex = startindex + pagesize
    #     url = 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?cc=cn&id=' + str(
    #         appid) + '&displayable-kind=11&startIndex=' + str(startindex) + '&endIndex=' + str(
    #         endindex) + '&sort=0&appVersion=all'
    #     html = download_page(url, proxip, headers)
    #     retcode = writeReview(html, output_file)
    #     if not retcode:
    #         break
    #     count = count + 1
    #     print("\r当前进度第: %d页" % page, end="")


if __name__ == '__main__':
    main()
