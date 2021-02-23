word1 = input("word1:")
word2 = input("word2:")

def hamming(w1, w2):
    w1 = str(w1)
    w2 = str(w2)
    n = 0
    for i in range(len(w1)):
        n+= w1[i] != w2[i]
    return n

print(hamming(word1, word2))