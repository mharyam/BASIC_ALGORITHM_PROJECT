class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def __str__(self):
        return f"{self.children} -- {self.is_word}"


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:  # checks if that char does not already exists in the children Trie
                current_node.children[char] = TrieNode()  # if it doesnt  add it to the children dict

            current_node = current_node.children[char]  # else loop through and go in the node

        current_node.is_word = True  # complete node by making is_word TRUE

    def find(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.is_word

    def suffixes(self, prefix):
        word = ''
        current_node = self.root

        if prefix not in current_node.children:
            return False

        current_node = current_node.children[prefix]
        self.suggest_word(current_node, word)
        return self.word_list

    def suggest_word(self, node, new_word):
        if node.is_word:
            self.word_list.append(new_word)

        for key, value in node.children.items():
            self.suggest_word(value, new_word+key)

MyTrie = Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.add(word)

print(MyTrie.suffixes('f'))

