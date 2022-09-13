def cipher(x):
    answer = ""
    for c in x:
        answer += chr(219 - ord(c)) if c.islower() else c
    return answer

X = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(cipher(X))
