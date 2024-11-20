
# Caching System Project (0x01-caching)

## Project Overview

This project focuses on implementing various caching algorithms as a fundamental part of backend development. Caching systems are critical for optimizing the performance of web applications by temporarily storing frequently accessed data. In this project, multiple caching techniques are explored, including FIFO, LIFO, LRU, MRU, and LFU. Each caching strategy serves unique use cases, which are implemented here to give a practical understanding of when and how to apply them.

## Learning Objectives

By the end of this project, you will be able to:

- Understand what a caching system is and why it is crucial for performance optimization.
- Explain and implement different caching strategies:
  - **FIFO (First-In, First-Out)**
  - **LIFO (Last-In, First-Out)**
  - **LRU (Least Recently Used)**
  - **MRU (Most Recently Used)**
  - **LFU (Least Frequently Used)**
- Identify the limitations of caching systems and design considerations.

## Project Structure

### Base Class

- **`BaseCaching`**:
  - Contains a dictionary, `cache_data`, where all cached items are stored.
  - Sets a constant limit for the cache size with `MAX_ITEMS` (default is 4).
  - Contains placeholders for `put` and `get` methods, which each caching strategy class must implement.

### Cache Algorithms

Each of these caching classes inherits from `BaseCaching` and implements a specific caching strategy:

- **`BasicCache`**: No limit on cache size.
- **`FIFOCache`**: Discards the oldest item when the cache limit is exceeded.
- **`LIFOCache`**: Discards the most recently added item when the cache limit is exceeded.
- **`LRUCache`**: Discards the least recently used item when the cache limit is exceeded.
- **`MRUCache`**: Discards the most recently used item when the cache limit is exceeded.
- **`LFUCache`**: Discards the least frequently used item when the cache limit is exceeded.

## Requirements

- **Python Version**: 3.7
- **Code Style**: Follows `pycodestyle` (version 2.5)
- **Execution**: All files must be executable (`chmod +x <filename>`).
- **Documentation**: All modules, classes, and functions must include docstrings.

## Project Directory Structure

```bash
0x01-caching/ 
    ├── base_caching.py # Base class for caching 
    ├── 0-basic_cache.py # Basic cache implementation 
    ├── 1-fifo_cache.py # FIFO cache implementation 
    ├── 2-lifo_cache.py # LIFO cache implementation 
    ├── 3-lru_cache.py # LRU cache implementation 
    ├── 4-mru_cache.py # MRU cache implementation 
    ├── 5-lfu_cache.py # LFU cache implementation 
    └── README.md # Project README file
```

## Usage

To use any of the caching classes, simply import them and use the `put` and `get` methods as shown in each task's example.

Example usage of `BasicCache`:

```python
from 0-basic_cache import BasicCache

cache = BasicCache()
cache.put("A", "Hello")
cache.put("B", "World")
print(cache.get("A"))  # Output: Hello
print(cache.get("B"))  # Output: World
print(cache.get("C"))  # Output: None
```

### Examples of Caching Strategies

1. **FIFO (First-In, First-Out):** Adds items in sequence and removes the oldest when exceeding capacity.
2. **LIFO (Last-In, First-Out):** Adds items in sequence but removes the last item when exceeding capacity.
3. **LRU (Least Recently Used):** Removes the least recently accessed item when exceeding capacity.
4. **MRU (Most Recently Used):** Removes the most recently accessed item when exceeding capacity.
5. **LFU (Least Frequently Used):** Removes the least accessed item when exceeding capacity.

## Author

This project was created by Refiloe Radebe (*kweenDev*), as part of the ALX Backend Specialization program.
