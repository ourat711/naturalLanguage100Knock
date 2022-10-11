import gzip
import json
import re
from urllib.error import ContentTooShortError
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
    ^\{\{基礎情報.*?$   # '{{基礎情報'で始まる行
    (.*?)       # キャプチャ対象、任意の0文字以上、非貪欲
    ^\}\}$      # '}}'の行
  ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

  # 基礎情報テンプレートの抽出
  contents = pattern.findall(lists)

  # 抽出結果からのフィールド名と値の抽出条件コンパイル
  pattern = re.compile(r'''
    ^\|         # '|'で始まる行
    (.+?)       # キャプチャ対象（フィールド名）、任意の1文字以上、非貪欲
    \s*         # 空白文字0文字以上
    =
    \s*         # 空白文字0文字以上
    (.+?)       # キャプチャ対象（値）、任意の1文字以上、非貪欲
    (?:         # キャプチャ対象外のグループ開始
        (?=\n\|)    # 改行+'|'の手前（肯定の先読み）
        | (?=\n$)   # または、改行+終端の手前（肯定の先読み）
    )           # グループ終了
  ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

  # フィールド名と値の抽出
  answer = {}
  if contents != []:
    fields = pattern.findall(contents[0])

    # 結果
    for field in fields:
      answer[field[0]] = re.sub("'''|'''''","'", field[1])
  print(answer)
