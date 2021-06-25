import time
import requests
import subprocess

while True:
    subprocess.run("clear")
    #2 page requests every 2 mins for the top 200 coins on coinmarketcap
    url = "https://coinmarketcap.com/"
    res = requests.get(url).text
    url = "https://coinmarketcap.com/?page=2"
    res += requests.get(url).text
    start = res.find("Bitcoin</p>")#skip to prices table
    res = res[start:]

    coinsOfInterest = ["Bitcoin","Ethereum","Ravencoin","Dogecoin"]
    colors=["\x1b[1;37;43m","\x1b[1;37;40m","\x1b[1;31;44m","\x1b[1;33;47m"]
    colorsEnd="\x1b[0m"
    index=0

    for coin in coinsOfInterest:
        coinLine = res.find(coin)
        surroundingData = res[coinLine:coinLine+600]
        dollarSign = surroundingData.find(">$") + 1
        endOfData = surroundingData[dollarSign:].find("<") + dollarSign
        print("{:<25}{:>25}".format(colors[index] + coin, surroundingData[dollarSign:endOfData]+colorsEnd))
        index+=1
    time.sleep(120)# 2 mins
