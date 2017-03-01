from random import choice
# open_and_read_file("green-eggs.txt")


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
    return contents


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    words = text_string.split()
    for counter in range(len(words)-2):
        first_word = words[counter]
        second_word = words[counter + 1]
        bi_gram = (first_word, second_word)
        # check if we've already added this bigram as a key in the chains dict
        third_words = chains.get(bi_gram, [])
        if third_words == []:  # if list of third words is empty
            chains[bi_gram] = [words[counter + 2]]
            # adds new key-value pair to chains dictionary
        else:
            third_words.append(words[counter + 2])
            # append word after n-gram to list

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    first_bi_gram = choice(markov_chains.keys())
    first_third_word = choice(chains[first_bi_gram])
    link = str(first_bi_gram[0]) + " " + str(first_bi_gram[1]) + " " + first_third_word
    print link

    third_words_list = chains[(first_bi_gram[1], first_third_word)]
    print third_words_list

    #random_word = choice(chains[(first_third_word, link_word)])
    # choose random value from the list that is the value for (first_third_word + link_word)
    #print random_word

all_text = open_and_read_file("green-eggs.txt")    # return text
markov_chains = make_chains(all_text)
make_text(markov_chains)
