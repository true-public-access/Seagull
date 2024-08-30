""" Seagull broser to define the fuctions that controle the internet access, 
    Copyright (C) 2024 Kai Broadbent 'BlazarKnight'

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to appblazarknight@gmail.com
"""


def geturlsorce(url: str):
    sorce = ["uhgfk"]

    from selenium import webdriver

    try:
        brower = webdriver.Firefox()
        brower.get(url)
        out = str(brower.page_source)
        brower.close()
        return out

    finally:
        pass


def getfilesaf(url: str):
    import os, requests

    get_response = requests.get(url, stream=True)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def get_fileexturl(url):
    """from urllib.parse import urlparse
    import os
    path = urlparse(url).path
    path_without_params, _ = os.path.splitext(path.split('?')[0])
    _, file_extension = os.path.splitext(path_without_params)
    return file_extension"""
    import re

    match = re.search(r"\.([a-zA-Z0-9]+)$", url)
    if match:
        return match.group(1)
    else:
        return None

    return file_name


def Findurlin(string):
    import re

    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


def findnumberin(i):
    new_data = "".join((ch if ch in "0123456789" else " ") for ch in i)
    numbers = [i for i in new_data.split()]
    return numbers


def wildwebser(term):
    import duckduckgo_search

    if term != "":
        return duckduckgo_search.DDGS().answers(keywords=term)
    else:
        return "error no search terms provided"


if __name__ == "__main__":
    print("go")
    print((wildwebser("usaa cik")))
    getfilesaf(
        "https://firstfrc.blob.core.windows.net/frc2024/Manual/2024GameManual.pdf"
    )
    """
    url= "https://www.sec.gov/Archives/edgar/cik-lookup-data.txt"
    name = geturlsorce(url)
    get_fileexturl(url)
    nums =findnumberin(str(name))
    ciks=[i for i in nums if len(i)==10]
    print(len(set(ciks)))
    print(ciks[50])
    """
