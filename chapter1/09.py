import random

def Typoglycemia(sList):
    answerList = []
    for i in range(len(sList)):
        target = ''.join(random.sample(sList[i], len(sList[i]))) if len(sList[i]) > 4 else sList[i]
        answerList.append(target)
    return ' '.join(answerList)

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(sentence)
print(Typoglycemia(sentence.split(' ')))