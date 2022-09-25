# coding: utf-8
import gzip
import json
fileName = "jawiki-country.json.gz"
title = "イギリス"

def wikiDataList():
    wikiDataList = []
    with gzip.open(fileName, mode='rt') as dataFile:
        for line in dataFile:
            wikiDataList.append(json.loads(line))
    return wikiDataList

dataList = [list for list in wikiDataList() if list['title'] == title].pop()
print(dataList['text'])
