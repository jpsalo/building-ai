import math
import numpy as np

text = """Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again"""


def unique_terms(docs):
    terms = []
    for doc in docs:
        for i, term_i in enumerate(doc):
            if term_i not in terms:
                terms.append(term_i)

    return terms


def term_frequencies(docs, terms):
    tf_list = np.zeros((len(docs), len(terms)))

    for i, doc in enumerate(docs):
        tf = np.array([])
        for j, term_i in enumerate(doc):
            if term_i not in tf:
                counter = 1
                tf = np.append(tf, term_i)
                for k, term_j in enumerate(doc):
                    if j != k and term_i == term_j:
                        counter += 1
                tf = np.append(tf, counter)
        tf = tf.reshape(-1, 2)
        for row in tf:
            word = row[0]
            tf_occurrences = int(row[1])
            tf_list[i, terms.index(word)] = tf_occurrences / len(doc)

    return tf_list


def document_frequencies(docs, terms):
    df_list = []

    for term in terms:
        df_occurrences = 0
        for doc in docs:
            if term in doc:
                df_occurrences += 1
        df_list.append(df_occurrences / len(docs))

    return df_list


def tf_idf_representations(docs, terms, tf, df):
    tf_idf_list = np.zeros((len(docs), len(terms)))

    with np.nditer(tf, op_flags=["readwrite"], flags=["multi_index"]) as it:
        for x in it:
            row = it.multi_index[0]
            col = it.multi_index[1]
            val = 0
            if x != 0:
                val = x * math.log(1 / df[col], 10)
            tf_idf_list[row, col] = val

    return tf_idf_list


def distance(row1, row2):
    sum = 0
    for w1, w2 in zip(row1, row2):
        sum = sum + float(abs(w1 - w2))

    if sum == 0:
        sum = np.inf

    return sum


def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal
    # despite casing) can be done with
    docs = [line.lower().split() for line in text.split("\n")]

    terms = unique_terms(docs)
    # print('terms:')
    # print(terms)
    # print('')

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    tf = term_frequencies(docs, terms)
    # print('term frequencies:')
    # print(tf)
    # print('')

    df = document_frequencies(docs, terms)
    # print('document frequencies:')
    # print(df)
    # print('')

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and
    # calculate its TF-IDF representation, which will be a vector
    tf_idf = tf_idf_representations(docs, terms, tf, df)
    # print('tf-idf')
    # print(tf_idf)
    # print('')

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.

    dist = np.array([[distance(sent1, sent2) for sent1 in tf_idf] for sent2 in tf_idf])
    print(np.unravel_index(np.argmin(dist), dist.shape))
    # return 0


main(text)
