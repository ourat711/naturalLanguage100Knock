import math

word1 = "パトカー"
word2 = "タクシー"
answer = ""

word1Array = list(word1)
word2Array = list(word2)
for i in range(len(word1Array)+len(word2Array)):
    if i % 2 == 0:
        answer += word1Array[math.floor(i/2)]
    else:
        answer += word2Array[math.floor(i/2)]

print(answer)
