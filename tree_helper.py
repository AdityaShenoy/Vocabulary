def init_tree():
    f = open('word_tree.txt', 'r')
    tree = eval(f.readline())
    f.close()
    return tree

def contains(words, word):
    node = words
    for c in word:
        ind = ord(c) - 96
        if node[ind] == '':
            return False
        node = node[ind]
    return True