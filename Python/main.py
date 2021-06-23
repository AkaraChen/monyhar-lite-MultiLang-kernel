import os
import re
import urllib
import requests
from typing import Any

# U know the rules,

# And so do I~


if_proxy = input("Do you want to set proxy server?[Y/n]")

if if_proxy == "Y":
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
        print("Did you set the proxy server?")


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
        print("Monyhar Browser,made by tucaoba233.")
        print("©CopyRight 2021-2021 tucaoba233, All Rights Reserved.")
        print("This project use GPL-3.0 License")

    def detection(self):
        print(self)

    def get_html(self):
        html = urllib.request.urlopen(self).read()
        return html

    def save_html(file_Name, file_content):
        #    注意windows文件命名的禁用符，比如 /
        file_Name = re.sub('[\/:*?"<>|]','_', file_Name)
        with open(file_Name + ".html", "wb") as f:
            #   写文件用bytes而不是str，所以要转码
            f.write(file_content)
            f.close()


global url
url = input("url:")
old_url = url

if re.search("http://", url) is None:
    url = "http://" + url

cache = Monyhar.surf_internet(url)
print(cache)
html = cache

if input("Help-About?[Y/n]") == "Y":
    Monyhar.about()
if input("Do you want to download the page?[Y/n]") == "Y":
    Monyhar.save_html(old_url, Monyhar.get_html(url))
