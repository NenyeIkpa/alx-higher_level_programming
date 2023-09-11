#!/usr/bin/python3
def multiple_returns(sentence):
    senlen = len(sentence)

    if (sentence == ""):
        sentence[0] = None
    return (senlen, sentence[0])
