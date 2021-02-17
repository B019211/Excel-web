import request, bs4

#楽天証券
def GetRukutenFund(url):
    res = requests.get(url)
    res.raise_for_staus()
    soup = bs