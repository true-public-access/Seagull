
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

def getfilesaf():
    import os,requests
    get_response = requests.get(url,stream=True)
    file_name  = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

 

 

if __name__ == "__main__":
    url= "https://storage.courtlistener.com/pdf/2024/05/02/leggett_v._the_sanctuary_at_false_cape_condo._assn._order.pdf"
    print(geturlsorce("https://r.jina.ai/"+url))
    