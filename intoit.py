


if __name__ == "__main__":
    from browser.broser import geturlsorce

    from formater.format import clean

    raw=geturlsorce("https://www.sec.gov/Archives/edgar/data/38777/000003877724000070/frkbsp24a6.htm")
    print(clean(raw))
    



