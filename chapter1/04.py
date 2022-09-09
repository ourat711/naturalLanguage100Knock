word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
header = [1, 5, 6, 7, 8, 9, 15, 16, 19]
answerList = dict()

wordArray = list(word)
stackWord = ""
for i in range(len(wordArray)):
    if  wordArray[i] == " ":
        if len(answerList)+1 in header:
            stackWord = stackWord[0]
        else:
            stackWord = stackWord[0:2]
        answerList[stackWord] = len(answerList) + 1
        stackWord = ""
    else:
        stackWord += wordArray[i]

print(answerList)
