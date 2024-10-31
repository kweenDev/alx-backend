# 0x00 Pagination Project

## Project Overview

This project focuses on implementing different pagination techniques to manage and display large datasets efficiently. Pagination is crucial for improving data access and user experience in applications dealing with extensive data. Here, we explore three primary pagination strategies:

1. **Simple Pagination** using basic page and page_size parameters.
2. **Hypermedia Pagination** with metadata for additional information.
3. **Deletion-Resilient Pagination** to handle data inconsistencies from deleted records.

---

## Learning Objectives

By the end of this project, you should be able to:

- Implement pagination using page and page_size parameters.
- Add hypermedia metadata to pagination responses.
- Create a pagination system that remains consistent even when items are deleted from the dataset.

---

## Project Requirements

- All code is compatible with **Ubuntu 18.04 LTS** and **Python 3.7**.
- Files must end with a new line.
- First line of each file: `#!/usr/bin/env python3`.
- **README.md** file in the project root is mandatory.
- Code styling must adhere to **pycodestyle** (version 2.5.\*).
- Files are tested for length using `wc`.
- Each module and function must be documented thoroughly with its purpose and usage.
- Type annotations are mandatory for all functions and coroutines.

---

## Project Setup

The project uses the **Popular_Baby_Names.csv** dataset. Ensure this CSV file is in the project directory to allow code access to sample data for pagination.

---

## Directory Structure

The project is structured as follows:

```plaintext
.
├── 0x00-pagination
│   ├── Popular_Baby_Names.csv
│   ├── 0-simple_helper_function.py
│   ├── 1-simple_pagination.py
│   ├── 2-hypermedia_pagination.py
│   ├── 3-hypermedia_del_pagination.py
│   └── README.md
```

---

## Tasks

### Task 0: Simple Helper Function

- **File**: `0-simple_helper_function.py`
- **Function**: `index_range(page: int, page_size: int) -> Tuple[int, int]`
- **Description**: Returns a tuple containing the start and end indexes for paginated data based on `page` and `page_size`.

- Example usage:

    ```python
    res = index_range(1, 7)
    print(res) # Output: (0, 7)
    ```

### Task 1: Simple Pagination

- **File**: `1-simple_pagination.py`
- **Class**: `Server`
- **Method**: `get_page(page: int = 1, page_size: int = 10) -> List[List]`
- **Description**: Implements pagination based on page and page_size values, using the `Popular_Baby_Names.csv` dataset.

- Example usage:

    ```python
    server = Server()
    page_data = server.get_page(1, 3)
    print(page_data)
    ```

### Task 2: Hypermedia Pagination

- **File**: `2-hypermedia_pagination.py`
- **Method**: `get_hyper(page: int = 1, page_size: int = 10) -> Dict`
- **Description**: Adds hypermedia metadata to the paginated data, including the current page number, total pages, previous and next pages.

- Example usage:

    ```python
    server = Server()
    hyper_data = server.get_hyper(1, 2)
    print(hyper_data)
    ```

### Task 3: Deletion-Resilient Hypermedia Pagination

- **File**: `3-hypermedia_del_pagination.py`
- **Method**: `get_hyper_index(index: int, page_size: int = 10) -> Dict`
- **Description**: Provides a deletion-resilient pagination mechanism that maintains data consistency, even when items are removed from the dataset.

- Example usage:

    ```python
    server = Server()
    resilient_page = server.get_hyper_index(3, 2)
    print(resilient_page)
    ```

---

## Testing

Each task file contains main test scripts to validate functionality. For example, you can run `0-main.py` through `3-main.py` to test each pagination implementation.

---

## Resources

- **Python Documentation**: Type Hints, Pycodestyle
- **Dataset**: Popular Baby Names Dataset

---

## Author

- **Author**: Refiloe Radebe
- **Date Created**: 2024-10-31
