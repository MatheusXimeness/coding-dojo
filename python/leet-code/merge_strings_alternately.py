# i will always start from the word 1
# i will verify if

# w1 = a
# w2 = b
# merged = ab

# w1 = a
# w2 = ba
# merged = aba

# w1 = ac
# w2 = b
# merged = abc


def solution(word1, word2):
    largest = word1 if len(word1) > len(word2) else word2
    i = 0
    merged = ""
    while i < len(word1) and i < len(word2):
        merged += word1[i] + word2[i]
        i += 1
    j = i
    while j < len(largest):
        merged += largest[j]
        j += 1

    return merged

w1 = "abc"
w2 = "pqr"

w3 = "ab"
w4 = "pqrs"

w5 = "abcd"
w6 = "pq"

print("PRIMEIRO: ", solution(w1, w2))
print("SEGUNDO: ", solution(w3, w4))
print("TERCEIRO: ", solution(w5, w6))
