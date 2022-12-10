#!/usr/bin/env python
from sys import stdin
positional_index = {}
for line in stdin:
    line = line.strip()
    term, doc_id, pos = line.split('\t')
    pos = int(pos)
    if term in positional_index.keys():
        postings = positional_index[term]
        if doc_id in postings.keys():
            postings[doc_id].append(pos)
        else:
            postings[doc_id] = []
            postings[doc_id].append(pos)
        positional_index[term] = postings
    else:
        postings = dict()
        postings[doc_id] = []
        postings[doc_id].append(pos)
        positional_index[term] = postings

for term in positional_index.keys():
    postings = ''
    positional_postings = positional_index[term]
    for doc_id in positional_postings.keys():
        temp = sorted(positional_postings[doc_id])
        positional_index[term][doc_id] = temp
        for i in positional_index[term][doc_id]:
            postings = postings + str(i) + ';'

        positional_index[term][doc_id] = postings

    print("%s\t%s" % (term, positional_index[term]))
