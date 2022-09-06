from array import array

word = "パタトクカシーー"
pickSuffixArray = [1,3,5,7]
answer = ""

wordArray = list(word)
for i in range(len(wordArray)):
    if i in pickSuffixArray:
        answer += wordArray[i]

print(answer)
