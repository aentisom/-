# 2020-6-8

import requests
import re

img_pt = re.compile('<a href="//(.*?)" target=.*? class="view_img_link" referrerPolicy="no-referrer">')
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.142 Mobile Safari/537.36"
}
next_page_pt = re.compile('<a title="Older Comments" href="//(.*?)" class="previous-comment-page">')

def get_one_page_imgs(url="http://jandan.net/ooxx") :

    data = requests.get(url, headers=headers)

    jpgs = re.findall(img_pt, data.text)

    img_name_pt = re.compile("large/(.*?)$")

    for jpg in jpgs :
        print(jpg)
        img_name = re.findall(img_name_pt, jpg)[0]
        print(img_name)
        img = requests.get("http://{}".format(jpg))
        with open("./{}".format(img_name), "wb+") as f:
            f.write(img.content)
    try :
        next_page_url = "http://{}".format(re.findall(next_page_pt, data.text)[0])
    except :
        return
    get_one_page_imgs(url = next_page_url)
get_one_page_imgs()
