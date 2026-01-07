# HashMap

Building my own hash map class to better understand how hash maps work under the hood.

## Motivation

Python provides dictionaries, but this project focuses on understanding how hash maps work internally, including hashing, indexing, and storage.

## Current Implementation

### Commit 1: Initial HashMap Structure

- Implemented the `HashMap` class
- Added a constructor with a fixed-size backing array
- Implemented a basic hash function

## Design Decisions

### Empty Bucket Representation

The backing array is pre-filled with `None` to explicitly represent empty buckets.

- Leaving the array empty would prevent indexed insertion
- Using values like `0` would be ambiguous, since they could represent valid data
- `None` acts as a sentinel value representing an unused bucket

This distinction is critical for detecting empty slots, handling collisions, and performing reliable lookups.

## Goals Moving Forward

- Implement key-value insertion
- Handle collisions
- Add retrieval functionality
- Improve hash distribution
- Compare behavior to Python’s built-in dictionary
