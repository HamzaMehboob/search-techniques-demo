from linear_search import linear_search
from binary_search import binary_search
from trie import Trie
from inverted_index import InvertedIndex
from bm25_simple import BM25Simple


def run_examples():
    print('--- Linear search ---')
    arr = [10, 20, 30, 40]
    print('linear_search(arr,30) ->', linear_search(arr, 30))

    print('\n--- Binary search ---')
    sorted_arr = [1,2,3,4,5,6]
    print('binary_search(sorted_arr,4) ->', binary_search(sorted_arr, 4))

    print('\n--- Trie ---')
    t = Trie()
    for w in ['hello', 'helium', 'help', 'hero']:
        t.insert(w)
    print("starts_with('he') ->", t.starts_with('he'))

    print('\n--- Inverted index ---')
    ii = InvertedIndex()
    ii.add_document('d1', 'the quick brown fox')
    ii.add_document('d2', 'quick brown jumps')
    print('OR search quick fox ->', ii.search_or('quick fox'))
    print('AND search quick fox ->', ii.search_and('quick fox'))

    print('\n--- BM25 simple ---')
    docs = ['the quick brown fox', 'quick brown quick', 'lazy dog brown']
    bm25 = BM25Simple(docs)
    print('bm25 query quick brown ->', bm25.query('quick brown'))


if __name__ == '__main__':
    run_examples()
