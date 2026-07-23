class WordDictionary:

    def __init__(self):
        self.root = dict()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = dict()
            curr = curr[letter]
        
        curr["\n"] = None


    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        while len(stack) > 0:
            trie_node, index = stack.pop()
            if len(word) == index:
                if "\n" in trie_node:
                    return True 
                continue 
            
            letter = word[index]
            if letter == ".":
                for potential_node in trie_node.values():
                    if potential_node:
                        stack.append((potential_node, index + 1))
            else:
                if letter in trie_node:
                    stack.append((trie_node[letter], index + 1))

        return False

