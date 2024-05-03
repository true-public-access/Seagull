
def geturlsorce(url:str):
    sorce = ["uhgfk"]
    import selenium
    from selenium import webdriver
    try:
        brower = webdriver.Firefox()
        brower.get(url)
        out = str(brower.page_source)
        brower.close()
        return out
    
    finally:
        pass

def getfilesaf(url:str):
    import os,requests
    get_response = requests.get(url,stream=True)
    file_name  = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def get_fileexturl(url):
    '''from urllib.parse import urlparse
    import os 
    path = urlparse(url).path
    path_without_params, _ = os.path.splitext(path.split('?')[0])
    _, file_extension = os.path.splitext(path_without_params)
    return file_extension'''
    import re
    match = re.search(r'\.([a-zA-Z0-9]+)$', url)
    if match:
        return match.group(1)
    else:
        return None

    return file_name
 

 

if __name__ == "__main__":
    url= "https://storage.courtlistener.com/pdf/2024/05/02/leggett_v._the_sanctuary_at_false_cape_condo._assn._order.pdf"
    print(getfilesaf(url))
    
