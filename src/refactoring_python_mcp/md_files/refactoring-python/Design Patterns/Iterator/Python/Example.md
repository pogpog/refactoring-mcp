---
tags: [design-patterns]
date_created: 2026-05-20
status: seed
---

# Iteratorin Python

 **Iterator** is a behavioral design pattern that allows sequential traversal through a complex data structure without exposing its internal details. Thanks to the Iterator, clients can go over elements of different collections in a similar fashion using a single iterator interface. [Learn more about Iterator](../../Iterator.md) Navigation [Intro](#) [Conceptual Example](#) [main](#) [Output](#) **Complexity:** **Popularity:** **Usage examples:** The pattern is very common in Python code. Many frameworks and libraries use it to provide a standard way for traversing their collections. **Identification:** Iterator is easy to recognize by the navigation methods (such as `next` , `previous` and others). Client code that uses iterators might not have direct access to the collection being traversed. 
## Conceptual Example
 This example illustrates the structure of the **Iterator** design pattern. It focuses on answering these questions: - What classes does it consist of? - What roles do these classes play? - In what way the elements of the pattern are related? 
#### main.py:Conceptual example
 
```
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any

"""
To create an iterator in Python, there are two abstract classes from the built-
in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in theiterator.
"""

class AlphabeticalOrderIterator(Iterator):
 """
 Concrete Iterators implement various traversal algorithms. These classes
 store the current traversal position at all times.
 """

 """
 `_position` attribute stores the current traversal position. An iterator may
 have a lot of other fields for storing iteration state, especially when it
 is supposed to work with a particular kind of collection.
 """
 _position: int = None

 """
 This attribute indicates the traversal direction.
 """
 _reverse: bool = False

 def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
 self._collection = collection
 self._reverse = reverse
 self._sorted_items = None # Will be set on first __next__ call
 self._position = 0

 def __next__(self) -> Any:
 """
 Optimization: sorting happens only when the first items is actually
 requested.
 """
 if self._sorted_items is None:
 self._sorted_items = sorted(self._collection._collection)
 if self._reverse:
 self._sorted_items = list(reversed(self._sorted_items))

 """
 The __next__() method must return the next item in the sequence. On
 reaching the end, and in subsequent calls, it must raise StopIteration.
 """
 if self._position >= len(self._sorted_items):
 raise StopIteration()
 value = self._sorted_items[self._position]
 self._position += 1
 return value

class WordsCollection(Iterable):
 """
 Concrete Collections provide one or several methods for retrieving fresh
 iterator instances, compatible with the collection class.
 """

 def __init__(self, collection: list[Any] | None = None) -> None:
 self._collection = collection or []

 def __getitem__(self, index: int) -> Any:
 return self._collection[index]

 def __iter__(self) -> AlphabeticalOrderIterator:
 """
 The __iter__() method returns the iterator object itself, by default we
 return the iterator in ascending order.
 """
 return AlphabeticalOrderIterator(self)

 def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
 return AlphabeticalOrderIterator(self, True)

 def add_item(self, item: Any) -> None:
 self._collection.append(item)

if __name__ == "__main__":
 # The client code may or may not know about the Concrete Iterator or
 # Collection classes, depending on the level of indirection you want to keep
 # in your program.
 collection = WordsCollection()
 collection.add_item("B")
 collection.add_item("A")
 collection.add_item("C")

 print("Straight traversal:")
 print("\n".join(collection))
 print("")

 print("Reverse traversal:")
 print("\n".join(collection.get_reverse_iterator()), end="")
```
 
#### Output.txt:Execution result
 
```
Straight traversal:
A
B
C

Reverse traversal:
C
B
A
```

