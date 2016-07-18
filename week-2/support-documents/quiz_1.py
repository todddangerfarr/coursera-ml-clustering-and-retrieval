# Quiz question 3
    # Consider the following two sentences.

    # Sentence 1: The quick brown fox jumps over the lazy dog.
    # Sentence 2: A quick brown dog outpaces a quick fox.
    # Compute the Euclidean distance using word counts. To compute word counts,
    # turn all words into lower case and strip all punctuation, so that "The" and
    # "the" are counted as the same token. That is, document 1 would be represented as
    #
    # x=[# the,# a,# quick,# brown,# fox,# jumps,# over,# lazy,# dog,# outpaces]
    # where # word is the count of that word in the document.
    #
    # Round your answer to 3 decimal places.

import string
import math

sent_1 = 'The quick brown fox jumps over the lazy dog.'
sent_2 = 'A quick brown dog outpaces a quick fox.'

# strip punctuation, convert to lowercase and split to list
sent_1_words = sent_1.translate(None, string.punctuation).lower().split(' ')
sent_2_words = sent_2.translate(None, string.punctuation).lower().split(' ')

# make a list of non-duplicates
word_list = list(set(sent_2_words + sent_1_words))

# create the word vectors
def create_word_vector(sentence_list):
    sentence_vector = [0 for x in range(len(word_list))]
    for word in sentence_list:
        if word in word_list:
            sentence_vector[word_list.index(word)] += 1
    return sentence_vector

# calculate euclidean distance between two word vectors
def euclidean_distance(x, q):
    sum_of_squares = 0
    for i in range(len(x)):
        sum_of_squares += (x[i]-q[i])**2
    return math.sqrt(sum_of_squares)

# create the word vectors
sent_1_vec = create_word_vector(sent_1_words)
sent_2_vec = create_word_vector(sent_2_words)

print 'Question 3 Answer ###########################'
print 'Word List: {}'.format(word_list)
print ''
print 'Sentence 1 Vector: {}'.format(sent_1_vec)
print 'Sentence 2 Vector: {}'.format(sent_2_vec)
print ''

print 'The Euclidean distance is: {:.3f}'.format(euclidean_distance(sent_1_vec, sent_2_vec))

# Quiz Question 4
    # Consider the following two sentences.
    #
    # Sentence 1: The quick brown fox jumps over the lazy dog.
    # Sentence 2: A quick brown dog outpaces a quick fox.
    # Recall that
    #
    # Compute the cosine distance between sentence 1 and sentence 2 using word counts.
    # To compute word counts, turn all words into lower case and strip all punctuation,
    # so that "The" and "the" are counted as the same token. That is, document 1 would
    # be represented as
    #
    # x=[# the,# a,# quick,# brown,# fox,# jumps,# over,# lazy,# dog,# outpaces]
    # where # word is the count of that word in the document.
    #
    # Round your answer to 3 decimal places.

# calculate the cosine distance between two work vectors
def cosine_distance(x, q):
    sum_of_squares_x = sum(map(lambda i: i*i, x))
    sum_of_squares_q = sum(map(lambda i: i*i, q))
    normalized_x = [(i / math.sqrt(sum_of_squares_x)) for i in x]
    normalized_q = [(i / math.sqrt(sum_of_squares_q)) for i in q]

    return 1 - sum(map(lambda i, j: i * j, normalized_x, normalized_q))

print ''
print 'Question 4 Answer ###########################'
print 'The Cosine Distance is: {:.3f}'.format(cosine_distance(sent_1_vec, sent_2_vec))
