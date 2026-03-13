import pytest
from strintmap import StrIntMap


def test_put_new_key():
    m = StrIntMap()
    m.put("cat", 10)
    assert m.get("cat") == 10

def test_put_update_existing_key():
    m = StrIntMap()
    m.put("cat", 10)
    m.put("cat", 99)
    assert m.get("cat") == 99

def test_get_existing_key():
    m = StrIntMap()
    m.put("dog", 7)
    assert m.get("dog") == 7

def test_get_missing_key_returns_none():
    m = StrIntMap()
    assert m.get("squirrel") is None

def test_remove_existing_key():
    m = StrIntMap()
    m.put("key", 5)
    m.remove("key")
    assert m.get("key") is None

def test_remove_missing_key_no_error():
    m = StrIntMap()
    m.remove("ghost")

def test_remove_decreases_size():
    m = StrIntMap()
    m.put("a", 1)
    m.put("b", 2)
    m.remove("a")
    assert m.size() == 1

def test_contains_existing_key():
    m = StrIntMap()
    m.put("hello", 1)
    assert m.contains("hello") is True

def test_contains_missing_key():
    m = StrIntMap()
    assert m.contains("world") is False

def test_contains_after_remove():
    m = StrIntMap()
    m.put("hi", 5)
    m.remove("hi")
    assert m.contains("hi") is False

def test_size_empty():
    m = StrIntMap()
    assert m.size() == 0

def test_size_after_puts():
    m = StrIntMap()
    m.put("a", 1)
    m.put("b", 2)
    assert m.size() == 2

def test_size_no_duplicate_count():
    m = StrIntMap()
    m.put("a", 1)
    m.put("a", 2)
    assert m.size() == 1

def test_keys_empty():
    m = StrIntMap()
    assert m.keys() == []

def test_keys_contains_all():
    m = StrIntMap()
    m.put("cat", 1)
    m.put("dog", 2)
    k = m.keys()
    assert "cat" in k and "dog" in k

def test_keys_length_matches_size():
    m = StrIntMap()
    m.put("a", 1)
    m.put("b", 2)
    m.put("c", 3)
    assert len(m.keys()) == m.size()

def test_rehash_doubles_capacity():
    m = StrIntMap()
    old_cap = m.capacity
    m.rehash()
    assert m.capacity == old_cap * 2

def test_rehash_preserves_data():
    m = StrIntMap()
    m.put("mouse", 11)
    m.put("cat", 10)
    m.rehash()
    assert m.get("mouse") == 11
    assert m.get("cat") == 10

def test_rehash_preserves_size():
    m = StrIntMap()
    m.put("a", 1)
    m.put("b", 2)
    m.rehash()
    assert m.size() == 2
