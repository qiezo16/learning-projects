# Learning-Projects
A collection of personal projects exploring data structures, algorithms, and Python implementations, including linked lists, hash maps, stacks, queues, and more.

## Tower-of-Hanoi
My attempt at making a tower of Hanoi game ( made after learning how to complete LinkedList, DoublyLinkedList, Nodes and Stacks

I made this after learning the above in a week with some direction. I got stuck multiple times espcially in the get_input function where the options would infinetely repeat and never actually save moves,
Still got to work on some syntax practice because i mainly think too fast and forget to run functions as an action and getting the return value rather than just calling back functions without the parenthesis.

Jesus christ finally, i spent all afternoon trying to figure out why it wouldnt save my moves, i knew there was something wrong with my get_input function. I combined lines 35, 36, 37 into one because fuck all that.
I also removed the choices[i] in my intial get input line 39 beacause it was checking substring membership and not lsit membership. Added a statement in case an incorrect input was inputted. Lastly in in 58 - 61 my disk comparison logic was wrong.# HashMap (From Scratch)

This project is a from-scratch implementation of a hash map in Python, created to better understand how hash tables work under the hood.

Rather than relying on Python’s built-in `dict`, this implementation explicitly handles hashing, array indexing, and collision resolution.

---

## Hashmap

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

