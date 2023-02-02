import os
import requests
from bs4 import BeautifulSoup

def fetch_file_infos(post_url):
    res = requests.get(post_url)
    soup = BeautifulSoup(res.text, "html.parser")
    download_box = soup.find("div", class_="moreless_content")
    a_tags = download_box.find_all("a")

    file_infos = []
    for a_tag in a_tags:
        url = a_tag.get("href")
        try:
            name = a_tag.find("span", class_="name").get_text()
        except:
            name = a_tag.get_text()
        file_info = (url, name)
        file_infos.append(file_info)
    return file_infos

def download_file(url, name):
    res = requests.get(url)

    with open(name, "wb") as file:
        file.write(res.content)
        print(name, "downloaded")
    return

def download_from(post_url):
    fileInfos = fetch_file_infos(post_url)
    downloaded_files = []

    for url, name in fileInfos:
        download_file(url, name)
        downloaded_files.append(name)
    return downloaded_files
