import re

word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
answerList = dict()

wordArray = list(re.sub(r"[^a-zA-Z]", "", word))
for i in range(len(wordArray)):
    if wordArray[i] in answerList:
        answerList[wordArray[i]] += 1
    else:
        answerList[wordArray[i]] = 1

print(answerList)
