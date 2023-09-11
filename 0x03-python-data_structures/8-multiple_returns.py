#!/usr/bin/python3
def multiple_returns(sentence):
    senlen = len(sentence)
    idx = 0

    if (senlen == 0):
        sentence[0] = ""
    else:
        for char in sentence:
            idx += 1
    return (idx, sentence[0])
