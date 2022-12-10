#!/usr/bin/env python3
from sys import stdin
import os
import re
#from glob import glob
from nltk import download as nltk_download
# nltk_download('stopwords')
# nltk_download('wordnet')
# nltk_download('omw-1.4')
# nltk_download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
lemmatizer = WordNetLemmatizer()


def pre_preocessing(line):
    token_list = word_tokenize(line)
    # remove puncuation and special characters
    # removing strings containing . and -
    token_list = [token for token in token_list if '.' not in token]
    token_list = [token for token in token_list if '-' not in token]
    token_list = [re.sub('[^A-Za-z0-9]+', '', token) for token in token_list]
    # if string contains any digit then its removed
    token_list = [token for token in token_list if not any(
        map(str.isdigit, token))]
    # all empty strings are removed
    token_list = [str for str in token_list if str]
    # all terms converted to lower characters
    token_list = [token.lower() for token in token_list]
    # stop words removal
    stop_words = set(stopwords.words('english'))
    token_list = [token for token in token_list if not token in stop_words]

    return token_list


count = dict()

for line in stdin:
    doc_id = os.environ['map_input_file']
    doc_id = os.path.basename(doc_id)
    if doc_id not in count.keys():
        count[doc_id] = 0
    line = line.strip()
    token_list = pre_preocessing(line)
    for token in token_list:
        count[doc_id] = count[doc_id] + 1
        term = lemmatizer.lemmatize(token)
        print("%s\t%s\t%s" % (term, doc_id, count[doc_id]))
