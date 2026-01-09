# HashMap (From Scratch)

This project is a from-scratch implementation of a hash map in Python, created to better understand how hash tables work under the hood.

Rather than relying on Python’s built-in `dict`, this implementation explicitly handles hashing, array indexing, and collision resolution.

---

## Overview

The `HashMap` class supports:
- Key–value assignment
- Value retrieval
- Collision handling using **open addressing with linear probing**

The backing array is initialized with `None` to clearly represent empty buckets.

---

## Design Decisions

### Backing Array Initialization

The backing array is pre-filled with `None` values rather than being left empty or filled with placeholder data.

This is important because:
- An empty list would not provide valid indices for insertion
- Using a value like `0` would be ambiguous, as it could represent legitimate data
- `None` acts as a clear sentinel value indicating an unused bucket

This distinction allows for:
- Reliable empty-slot detection
- Correct collision handling
- Predictable retrieval behavior

---

## Collision Handling

When two keys hash to the same index, the hash map resolves collisions using **linear probing**:

- The original hash value is incremented by a collision count
- The new hash is re-compressed into the array size
- The process repeats until an empty slot or matching key is found

Both insertion and retrieval follow the same probing sequence, ensuring consistency.

---

## Goals Moving Forward

- Add resizing based on load factor
- Improve hash distribution
- Compare performance against Python’s built-in dictionary
- Add unit tests

---

## Why This Project Exists

This project is meant as a learning exercise to understand:
- How hash functions work
- Why backing arrays require sentinel values
- How collisions affect performance
- What tradeoffs exist in hash map design
