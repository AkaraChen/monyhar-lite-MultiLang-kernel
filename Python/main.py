import os
import re
import urllib
import requests
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

from typing import Any

# U know the rules,

# And so do I~
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}

if_proxy = input("Do you want to set proxy server?[Y/n]")

if if_proxy == "Y":
    if_localhost = input("Localhost?[Y/n]")
    if if_localhost == "Y":
        http_port = input("HTTP PROXY PORT:")
        http_proxy = "localhost" + http_port
        https_port = input("HTTPS PROXY PORT:")
        https_proxy = "localhost" + https_port
    else:
        http_proxy = input("Type http proxy address here.")
        https_proxy = input("Type https proxy address here.")
        proxies: dict[str, Any] = {"http": http_proxy, "https": https_proxy}
    if_test = input("Test the proxy server?[Y/n]")
    try:
        if if_test == "Y":
            ping_http_proxy = "ping" + http_proxy
            ping_https_proxy = "ping" + https_proxy
            ping_result = os.system("ping " + http_proxy)
            if "Lost = 0" in ping_result:
                print("Connected to the http proxy server.")
                ping_result = os.system("ping " + https_proxy)
            if "Lost = 0" in ping_result:
                print("Connected to the https proxy server.")
            else:
               print("No proxy server was set.")
    except:
        print('\033[1;31;40m')  # 下一目标输出背景为黑色，颜色红色高亮显示
        print('[Warning]Have you set all the proxy server?')  # 字体颜色红色反白处理
        print('\033[0m')


class Monyhar:
    def __init__(self):
        print("Welcome to Monyhar Browser")

    def surf_internet(self):
        html = requests.get(self)
        print(html.status_code)  # print the http code returned.
        print(html.text)  # print text returned.
        html = html.status_code
        return html

    @staticmethod
    def about():
        print("[Info]Monyhar Browser,made by tucaoba233.")
        print("[Info]©CopyRight 2021-2021 tucaoba233, All Rights Reserved.")
        print("[Info]This project follow GPL-3.0 License")

    def detection(self):
        print(self)

    def get_html(self):
        html = urllib.request.urlopen(self).read()
        return html

    def save_html(self, file_content):
        #    注意windows文件命名的禁用符，比如 /
        self = re.sub('[\/:*?"<>|]', '_', self)
        with open(self + ".html", "wb") as f:
            #   写文件用bytes而不是str，所以要转码
            f.write(file_content)
            f.close()


url = input("url:   example: https://www.google.com |")
old_url = url

#if re.search("http://", url) is None:
#    url = "http://" + url
if_https = input("Try to connect with https?[Y/n]")
if if_https == "Y":
    try:
        req = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(req)
        cache = res.read()
        print(cache)
        html = cache
    except:
        print('\033[1;31;40m')  # 下一目标输出背景为黑色，颜色红色高亮显示
        print("\033[7;31m[ERROR] Failed to connect to the server with HTTPS/SSL connection.\033[1;31;40m")
        print('\030[WARNING] Your connection to this site is not secure.\033[1;31;40m')  # 字体颜色红色反白处理
        print('\033[0m')
        print("[Info] Do you want to visit anyway?[Yes/n]")
        if_visit = input()
        if if_visit == "Yes":
            cache = Monyhar.surf_internet(url)
            print(cache)
            html = cache
        else:
            print("[Info] User cancelled the connection.")
else:
    print('\033[1;31;40m')  # 下一目标输出背景为黑色，颜色红色高亮显示
    print('\030[7;31m[WARNING] Your connection to this site is not secure.\033[1;31;40m')  # 字体颜色红色反白处理
    print('\033[0m')
    cache = Monyhar.surf_internet(url)
    print(cache)
    html = cache

if input("Help-About?[Y/n]") == "Y":
    Monyhar.about()
if input("Do you want to download the page?[Y/n]") == "Y":
    Monyhar.save_html(old_url, Monyhar.get_html(url))
