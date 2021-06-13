class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

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
        words = []
        current_node = self.root

        if prefix not in current_node.children.get(prefix):
            return None

        # while current_node.children:
        #     if current_node.children
        for char in current_node.children:
            print(char)

    # def get_word(self, node):
    #     pass


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.add(word)


MyTrie.suffixes('f')

