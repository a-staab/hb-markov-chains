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
            # append word after n-gram word to list

    print chains

all_text = open_and_read_file("green-eggs.txt")
chains_dict = make_chains(all_text)
