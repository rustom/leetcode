import re

class WordDictionary:

    def __init__(self):
        self.wordList = set()
        

    def addWord(self, word: str) -> None:
        self.wordList.add(word)
        

    def search(self, word: str) -> bool:
        for listItem in self.wordList:
            if re.match(word, listItem) and (len(listItem) == len(word)):
                return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
word = 'add'
obj.addWord(word)
print(obj.search('a'))
print(obj.search('a.d'))