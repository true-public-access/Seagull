
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


if __name__ == "__main__":
    print(geturlsorce('https://www.chess.com/?utm_source=partnership&utm_medium=opera&utm_campaign=speed_dial'))