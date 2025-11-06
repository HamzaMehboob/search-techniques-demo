from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return False
        return node.is_end

    def starts_with(self, prefix: str) -> list:
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return []
        results = []
        self._collect(node, prefix, results)
        return results

    def _collect(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)
        for ch, child in node.children.items():
            self._collect(child, prefix + ch, results)


if __name__ == "__main__":
    t = Trie()
    for w in ["apple", "app", "apricot", "bat", "batch"]:
        t.insert(w)
    print("search('app') ->", t.search("app"))
    print("starts_with('ap') ->", t.starts_with("ap"))
