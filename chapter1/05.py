def n_gram(resource, n):
    answerList = []
    for i in range(len(resource)):
        ngramWord = resource[i:i+n]
        if n != len(ngramWord):
            break
        answerList.append(ngramWord)
    return answerList

word = "I am an NLPer"
words = word.split(' ')

print(n_gram(word, 1))
print(n_gram(word, 3))
print(n_gram(words, 1))
print(n_gram(words, 3))