import gzip
import json
import re
fileName = "jawiki-country.json.gz"

def wikiDataList():
    wikiDataList = []
    with gzip.open(fileName, mode='rt') as dataFile:
        for line in dataFile:
            wikiDataList.append(json.loads(line))
    return wikiDataList

for list in wikiDataList():
  print(list['title'])
  lists = list['text']

  # パターン
  pattern = re.compile(r'''
      (?:File|ファイル)   # 非キャプチャ、'File'か'ファイル'
      :
      (.+?)   # キャプチャ対象、任意の文字1文字以上、非貪欲
      \| # |をエスケープ
      ''', re.VERBOSE)
  result = pattern.findall(lists)

  # 結果
  for line in result:
      print(line)
