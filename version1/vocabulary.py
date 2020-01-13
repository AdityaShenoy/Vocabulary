import tree_helper as th
import bot

if __name__ == "__main__":
    words = th.init_tree()
    while True:
        word = input('Enter a word: ')
        while th.contains(words, word):
            print('This word has already been covered')
            word = input('Enter a new word:')

        bot.find_word(word)
        th.insert(words, word)
        th.save_tree(words)