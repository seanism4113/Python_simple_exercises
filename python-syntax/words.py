def print_upper_words(word_list, must_start_with):
    ''' Prints out a list of words in uppercase '''

    for word in word_list:
        if word[0] in must_start_with:
            print(word.upper())

