def n_gram(resource, n):
    answerList = []

    for i in range(len(resource)):
        ngramWord = resource[i:i+n]
        if n != len(ngramWord):
            break
        answerList.append(ngramWord)
    return answerList

word1 = "paraparaparadise"
word2 = "paragraph"
n =2
checkWord = "se"

X = set(n_gram(word1, n))
Y = set(n_gram(word2, n))

print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))
print("含まれる" if checkWord in X else "含まれない")
print("含まれる" if checkWord in Y else "含まれない")
