import re
from collections import defaultdict

_word_re = re.compile(r"\w+")

def tokenize(text: str):
    return _word_re.findall(text.lower())


class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)  # term -> set(doc_id)
        self.docs = {}

    def add_document(self, doc_id: str, text: str):
        self.docs[doc_id] = text
        for term in set(tokenize(text)):
            self.index[term].add(doc_id)

    def search_or(self, query: str):
        terms = tokenize(query)
        results = set()
        for t in terms:
            results |= self.index.get(t, set())
        return list(results)

    def search_and(self, query: str):
        terms = tokenize(query)
        if not terms:
            return []
        results = None
        for t in terms:
            docs = self.index.get(t, set())
            results = docs if results is None else (results & docs)
        return list(results or [])


if __name__ == "__main__":
    ii = InvertedIndex()
    ii.add_document("doc1", "The quick brown fox")
    ii.add_document("doc2", "Quick brown fox jumps")
    ii.add_document("doc3", "Lazy dog")
    print("OR search 'quick fox' ->", ii.search_or("quick fox"))
    print("AND search 'quick fox' ->", ii.search_and("quick fox"))
