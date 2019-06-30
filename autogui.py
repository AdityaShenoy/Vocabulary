import tree_helper as th
import bot
import file_helper as fh

if __name__ == "__main__":
    words = th.init_tree()

    word = input('Enter a word: ')
    while th.contains(words, word):
        print('This word has already been covered')
        word = input('Enter a new word:')

    bot.find_word(word)
    fh.filter_file()