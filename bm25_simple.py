import math
from collections import Counter

class BM25Simple:
    def __init__(self, docs):
        self.docs = [d.split() for d in docs]
        self.N = len(self.docs)
        self.avgdl = sum(len(d) for d in self.docs) / max(1, self.N)
        self.doc_freqs = []
        self.df = {}
        for doc in self.docs:
            freqs = Counter(doc)
            self.doc_freqs.append(freqs)
            for term in freqs.keys():
                self.df[term] = self.df.get(term, 0) + 1
        self.k1 = 1.5
        self.b = 0.75

    def idf(self, term):
        n_q = self.df.get(term, 0)
        return math.log(1 + (self.N - n_q + 0.5) / (n_q + 0.5))

    def score(self, query, index):
        score = 0.0
        freqs = self.doc_freqs[index]
        doc_len = len(self.docs[index])
        for term in query.split():
            if term not in freqs:
                continue
            idf = self.idf(term)
            f = freqs[term]
            denom = f + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
            score += idf * f * (self.k1 + 1) / denom
        return score

    def query(self, query, top_k=5):
        scores = [(i, self.score(query, i)) for i in range(self.N)]
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]


if __name__ == "__main__":
    docs = [
        "the quick brown fox",
        "quick brown quick",
        "lazy dog brown",
    ]
    bm25 = BM25Simple(docs)
    print("BM25 scores for 'quick brown' ->", bm25.query("quick brown"))
