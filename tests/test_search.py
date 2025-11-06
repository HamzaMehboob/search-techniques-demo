import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from linear_search import linear_search
from binary_search import binary_search
from trie import Trie
from inverted_index import InvertedIndex
from bm25_simple import BM25Simple


def test_linear_search():
    assert linear_search([1,2,3], 2) == 1
    assert linear_search([], 1) == -1


def test_binary_search():
    assert binary_search([1,2,3,4], 3) == 2
    assert binary_search([1,2,3], 5) == -1


def test_trie():
    t = Trie()
    t.insert('abc')
    assert t.search('abc') is True
    assert t.search('ab') is False
    assert 'abc' in t.starts_with('a')


def test_inverted_index():
    ii = InvertedIndex()
    ii.add_document('d1', 'hello world')
    ii.add_document('d2', 'hello python')
    or_res = ii.search_or('hello')
    assert set(or_res) == {'d1', 'd2'}
    and_res = ii.search_and('hello python')
    assert and_res == ['d2'] or set(and_res) == {'d2'}


def test_bm25():
    docs = ['a b c', 'a a b']
    bm25 = BM25Simple(docs)
    res = bm25.query('a b', top_k=2)
    assert len(res) == 2
