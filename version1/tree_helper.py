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

def insert(words, word):
    node = words
    for c in word:
        ind = ord(c) - 96
        if node[ind] == '':
            node[ind] = [c] + [''] * 26
        node = node[ind]

def save_tree(words):
    f = open('word_tree.txt', 'w')
    f.write(str(words))
    f.close()