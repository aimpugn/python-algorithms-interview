import sys
sys.path.insert(0, '.')
import tracemalloc
import collections
from pai_util.trace import display_top

class TrieNode:
    def __init__(self):
        self.word = False   # 한 단어가 완성됨을 의미 
        self.children = {}  # 연결되는 다음 문자

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.word_map = collections.defaultdict(bool)


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children: 
                node.children[char] = TrieNode()
            node = node.children[char] # node.children[char].children[char]...로 연결된다
        node.word = True
        self.word_map[word] = True

    '''
    Runtime: 176 ms, faster than 64.30% of Python3 online submissions for Implement Trie (Prefix Tree).
    Memory Usage: 32.2 MB, less than 37.82% of Python3 online submissions for Implement Trie (Prefix Tree).
    '''
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.word


    '''
    Runtime: 160 ms, faster than 74.00% of Python3 online submissions for Implement Trie (Prefix Tree).
    Memory Usage: 32.2 MB, less than 37.82% of Python3 online submissions for Implement Trie (Prefix Tree).
    '''
    def search2(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.word_map:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
        


# Your Trie object will be instantiated and called as such:
tracemalloc.start()
# 1 <= word.length <= 2000
word = 'asdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxgtyeuyriwpasdksdklfnsdmvncxmvnjdgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuef'
obj = Trie()
print(len(word))
obj.insert(word)
print(obj.search(word))
prefix1 = 'asdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwf'
print(obj.startsWith(prefix1))
prefix2 = 'asdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefh'
print(obj.startsWith(prefix2))
prefix3 = 'asdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxgtyeuyriwpasdksdklfnsdmvncxmvnjdgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviue'
print(obj.startsWith(prefix3))
word2 = 'jnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfiddsdfsdfsdfsdfiddsdfsdfidjdksdndvlndslfwoiefhowfcslmnvdslfwoiefhowfcslmnvkjsdhowfcslmnvkjsdbfkjcslmnvkjsdbfkjsdbfjsdhfiuwefgquyvrgquyvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhtxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqasdfsddsvrtgbdidddddytjnhgdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvasdfsddsvrtgbdidddddytjnhgtfgghdddddrfeferdhtyjretyjnddsdfsdfidjdksdndvlndslfwoiefhowfcdslmnvkjsdbfkjsdbfjsdhfiuwefgquywesdfsdfliwopfihwlfcnsdvccjbvhsdfjhsfiqoqghasgfsagdstxfzxgcvgquyrwfeutyqwreuywdksdklfnsdmvncxmvnjdgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuefqoqwjpowqpqoiwjdjksbjdnbcnmxbvhfdgvgjghasgfsagdstxfzxgcvgquyrwfeutyqwreuywqtduhsvajvzbxbxbxbhshsdfgtyeuyriwpasdksdklfnsdmvncxmvnfjdgviuef'
print(len(word2))
obj.insert(word2)
word3 = 'dewoidhdslknforhgferiubgvkjfbvkasdjdbfkjasdfjksdbfkjsabhfuiweihfiuqwegfihbvhsbvmnxcbncnndhjdhxcycywioqwiskkdfbnsdkjhfreifgiwreuhfdsjbvckcjbvkjsdfkujshfiuwegfiweufedjihfdskjfnsdkjbfviuerhbvyrefbvifdhbsdkjfbvksdubfiweufhiewuhasdjkcaskjdqiuqwiqwouwiudhwiudbsutcdstytdtcrsfytcrsadtycfasdgcvsd'
print(len(word3))
obj.insert(word3)
prefix4 = 'dewoidhdslknforhgferiubgvkjfbvkasdjdbfkjasdfjksdbfkjsabhfuiweihfiuqwegfihbvhsbvmnxcbncnndhjdhxcycywioqwiskkdfbnsdkjhfreifgiwreuhfdsjbvckcjbvkjsdfkujshfiuwegfiweufedjihfdskjfnsdkjbfviuerhbvyrefbvifdhbsdkjfbvksdubfiweufhiewuhasdjkcaskjdqiuqwiqwouwiudhwiudbsutcdstytdtcrsfytcrsadtycfasdcxvdsfdv'
print(obj.startsWith(prefix4))
prefix5 = 'dewoidhdslknforhgferiubgvkjfbvkasdjdbfkjasdfjksdbfkjsabhfuiweihfiuqwegfihbvhsbvmnxcbncnndhjdhxcycywioqwiskkdfbnsdkjhfreifgiwreuhfdsjbvckcjbvkjsdfkujshfiuwegfiweufedjihfdskjfnsdkjbfviuerhbvyrefbvifdhbsdkjfbvksdubfiweufhiewuhasdjkcaskjdqiuqwiqwouwiudhwiudbsutcdstytdtcrsfytcrsadtycfasd'
print(obj.startsWith(prefix5))
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')
""" print("[ Top 10 ]")
for stat in top_stats[:10]:
    print('메모리 블록이 할당된 곳:', stat.traceback, '/ 메모리 블록 수(int):', stat.count, '/ 총 메모리 블록의 바이트 단위 크기 (int):', stat.size) """
display_top(snapshot)
tracemalloc.stop()
