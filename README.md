# Data Structures using Python — Lab Record

[![Language](https://img.shields.io/badge/language-Python-3776AB.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Dependencies](https://img.shields.io/badge/dependencies-standard%20library%20only-orange.svg)](https://docs.python.org/3/library/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](#prerequisites)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A complete, self-contained collection of Python programs written for the **Data Structures
using Python Laboratory** (II B.Tech — Semester I). Every program is a single script with its
own driver code, depends only on the Python standard library, and can be executed
independently.

---

## Table of Contents

- [Data Structures using Python — Lab Record](#data-structures-using-python--lab-record)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Repository Structure](#repository-structure)
  - [Prerequisites](#prerequisites)
  - [Running the Programs](#running-the-programs)
  - [Program Reference](#program-reference)
    - [1 — Flower Class](#1--flower-class)
    - [2 — Inheritance and Abstract Base Classes](#2--inheritance-and-abstract-base-classes)
    - [3 — Polymorphism: Overloading and Overriding](#3--polymorphism-overloading-and-overriding)
    - [4 — Comprehensions](#4--comprehensions)
    - [5 — Combinations of *n* Distinct Objects](#5--combinations-of-n-distinct-objects)
    - [6 — Searching: Linear and Binary](#6--searching-linear-and-binary)
    - [7 — Sorting: Bubble and Selection](#7--sorting-bubble-and-selection)
  - [Complexity Summary](#complexity-summary)
  - [Known Issues](#known-issues)
  - [Coding Conventions](#coding-conventions)
  - [Author(s)](#authors)
  - [License](#license)

---

## Overview

The programs in this repository cover the object-oriented foundations taught in the course,
together with the Pythonic constructs and classical algorithms built on top of them:

| Theme                       | Experiments                                                        |
| :-------------------------- | :----------------------------------------------------------------- |
| Encapsulation               | Class definition with accessor and mutator methods                 |
| Abstraction and inheritance | Abstract base class with a three-way polygon hierarchy             |
| Polymorphism                | Method overloading via `*args`, method overriding via subclassing  |
| Comprehensions              | List, dictionary, set and generator comprehensions                 |
| Combinatorics               | Combinations of `n` distinct objects taken `r` at a time           |
| Searching                   | Linear search on unsorted data, binary search on sorted data       |
| Sorting                     | Bubble sort with early exit, selection sort                        |

## Repository Structure

```
dsp_2-1/
├── 1_flower.py                   # Class definition: constructor, getters, setters
├── 2_inheritance.py              # Abstract base class: triangle, quadrilateral, pentagon
├── 3a_overloading.py             # Method overloading via variadic arguments
├── 3b_overriding.py              # Method overriding and dynamic dispatch
├── 4a_list_comp.py               # List comprehension: map and filter
├── 4b_dict_comp.py               # Dictionary comprehension: characters to ASCII codes
├── 4c_set_comp.py                # Set comprehension: unique squares
├── 4d_gen_comp.py                # Generator expressions and lazy evaluation
├── 5_n_object_comb.py            # Combinations of n distinct objects
├── 6a_linear_search.py           # Linear (sequential) search
├── 6b_binary_search.py           # Binary search over a sorted array
├── 7a_bubble_sort.py             # Bubble sort with early-exit optimisation
├── 7b_selection_sort.py          # Selection sort
├── LICENSE
└── README.md
```

> **Note on numbering:** file names follow the experiment numbers in the lab manual. The
> `a`/`b`/`c`/`d` suffixes denote the parts of a single experiment — experiment 3 has two
> parts, experiment 4 has four.

## Prerequisites

| Requirement          | Details                                                                                     |
| :------------------- | :------------------------------------------------------------------------------------------ |
| **Interpreter**      | CPython 3.8 or newer — developed and tested on CPython 3.14                                 |
| **Standard library** | `abc`, `math` and `itertools` only — no third-party dependencies                            |
| **Tooling**          | None required; no build step, no virtual environment, no `requirements.txt`                 |

Verify your interpreter:

```bash
python --version
```

Windows users can obtain Python from [python.org](https://www.python.org/downloads/) or the
Microsoft Store. On most Linux and macOS systems the interpreter is invoked as `python3`
rather than `python`.

## Running the Programs

Run a single program:

```bash
# Linux / macOS
python3 1_flower.py
```

```powershell
# Windows (PowerShell)
python .\1_flower.py
```

Run every non-interactive program in sequence:

```bash
# Linux / macOS
for src in 1_*.py 3?_*.py 4?_*.py 5_*.py 7?_*.py; do
    echo "===== $src ====="
    python3 "$src"
done
```

```powershell
# Windows (PowerShell)
Get-ChildItem 1_*.py, 3?_*.py, 4?_*.py, 5_*.py, 7?_*.py | ForEach-Object {
    Write-Host "===== $($_.Name) ====="
    python $_.Name
}
```

The globs above deliberately exclude experiments 2, 6a and 6b, which read from standard
input. Run those three from an interactive terminal rather than from an editor's output-only
pane, or they will fail on an empty read. All thirteen programs run cleanly under CPython
3.14 with no warnings.

---

## Program Reference

### 1 — Flower Class

**File:** [`1_flower.py`](1_flower.py) · **Input:** none — values hard-coded in the driver

A `Flower` class holding `name`, `num_petals` and `price`, with a getter and a setter for
each attribute. The driver creates an object, prints its initial state, mutates every
attribute through the setters, then prints the updated state. The point of the experiment is
encapsulation: state is read and written only through the class interface, never by touching
the attributes directly.

```text
Flower Name: Rose
Number of Petals: 32
Price: 10.5

After updating:
Flower Name: Lily
Number of Petals: 6
Price: 15.75
```

### 2 — Inheritance and Abstract Base Classes

**File:** [`2_inheritance.py`](2_inheritance.py) · **Input:** interactive menu

An abstract class `Polygon` declares `area()` and `perimeter()` with the `@abstractmethod`
decorator from the `abc` module, so `Polygon` itself cannot be instantiated and every
subclass is forced to supply both methods. Three concrete subclasses implement them:

| Class                       | Area                                    | Perimeter            |
| :-------------------------- | :-------------------------------------- | :------------------- |
| `Triangle`                  | Heron's formula, `√(s(s−a)(s−b)(s−c))`  | `a + b + c`          |
| `Quadrilateral` (rectangle) | `length × width`                        | `2 × (length + width)` |
| `Pentagon` (regular)        | `¼ · √(5(5 + 2√5)) · side²`             | `5 × side`           |

`Quadrilateral` is restricted to rectangles, as noted in the source; a general quadrilateral
is not determined by its side lengths alone. Menu options: `1` Triangle · `2` Quadrilateral ·
`3` Regular pentagon · `4` Exit. The loop repeats until `4` is chosen.

```text
Choose Polygon Type:
1. Triangle
2. Quadrilateral (Rectangle)
3. Regular Pentagon
4. Exit
Enter choice: 1
Enter side a: 3
Enter side b: 4
Enter side c: 5
Area: 6.00
Perimeter: 12.00
```

> See [Known Issues](#known-issues) before entering triangle sides.

### 3 — Polymorphism: Overloading and Overriding

**Files:** [`3a_overloading.py`](3a_overloading.py), [`3b_overriding.py`](3b_overriding.py) ·
**Input:** none

**3a — Method overloading.** Python does not support signature-based overloading the way C++
and Java do; a second `def` with the same name simply replaces the first. The equivalent
behaviour comes from the variadic `*args` parameter, so one `Calculator.add()` accepts any
number of operands.

```text
Sum of 2 and 3:- 5
Sum of 2, 3 and 4:- 9
Sum of 5, 10, 15, and 20:- 50
```

**3b — Method overriding.** A base class `Vehicle` defines `description()`, which the derived
classes `Car` and `Bike` each redefine. Which implementation runs is decided by the type of
the object at run time, not by the type of the reference — this is dynamic dispatch.

```text
This is a vehicle
This is a car
This is a bike
```

### 4 — Comprehensions

**Files:** [`4a_list_comp.py`](4a_list_comp.py), [`4b_dict_comp.py`](4b_dict_comp.py),
[`4c_set_comp.py`](4c_set_comp.py), [`4d_gen_comp.py`](4d_gen_comp.py) · **Input:** none

The four parts introduce each comprehension form in turn, over the same underlying idea of
building a collection from an iterable in a single expression:

| Part | Construct                          | Demonstrates                                                          |
| :--- | :--------------------------------- | :-------------------------------------------------------------------- |
| `4a` | `[expr for x in iterable if cond]` | Squares of 1–10, evens of 1–20, per-character case conversion         |
| `4b` | `{key: value for x in iterable}`   | Mapping each character of `"HELLO"` to its ASCII code with `ord()`    |
| `4c` | `{expr for x in iterable}`         | Unique squares from a list containing duplicates                      |
| `4d` | `(expr for x in iterable)`         | Lazy evaluation, `next()`, and aggregation with no intermediate list  |

Part `4d` is the substantial one. It contrasts a list comprehension, which materialises every
element at once, against a generator expression, which produces values on demand — and shows
that a partially consumed generator resumes from where `next()` left it rather than restarting.

```text
Type of squares_gen: <class 'generator'>
First two values via next(): 1 4
Remaining squares: [9, 16, 25, 36, 49, 64, 81, 100]
Even squares up to 20: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
Sum of cubes 1..5: 225
Any multiple of 7 in 10..19?: True
Are all numbers < 50 in 10..19?: True
Word lengths: [9, 11, 3, 6, 9, 3, 4]
List comp (materialized): [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Gen comp (lazy, not materialized): <generator object <genexpr> at 0x...>
Materialize generator on demand: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Note that the generator object prints as a repr rather than its contents, and that
`list(gen_comp)` on the following line is what finally forces evaluation.

### 5 — Combinations of *n* Distinct Objects

**File:** [`5_n_object_comb.py`](5_n_object_comb.py) · **Input:** none — list set in source

Uses `itertools.combinations` to generate every selection of `r` items from a list of `n`
distinct objects, where order does not matter and no item repeats. With `n = 9` and `r = 2`
the program emits all C(9, 2) = 36 pairs in lexicographic order. Change `r` in the source to
explore other combination sizes.

```text
Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Combinations of 2 distinct objects:
[1, 2]
[1, 3]
...
[8, 9]
```

`combinations` returns an iterator, not a list, so the pairs are produced lazily as the loop
consumes them — the same lazy-evaluation idea introduced in experiment `4d`.

### 6 — Searching: Linear and Binary

**Files:** [`6a_linear_search.py`](6a_linear_search.py),
[`6b_binary_search.py`](6b_binary_search.py) · **Input:** interactive — one integer key

The same task under two strategies, so the cost difference is directly comparable. Both
return the index of the key, or `-1` when it is absent.

**6a — Linear search** scans from the first element onwards and stops at the first match. It
places no requirement on the data, so it runs on the unsorted array `[34, 7, 23, 32, 5, 62]`.

```text
Enter the element to search: 32
Element found at index 3
```

**6b — Binary search** repeatedly halves the interval by comparing the key against the middle
element. **The array must be sorted in ascending order** or the result is meaningless, so the
script operates on the pre-sorted `[5, 7, 23, 32, 34, 62]`.

```text
Enter the element to search: 23
Element found at index 2
```

That precondition is the trade-off being taught: binary search is exponentially faster, but
only over data someone has already paid to sort.

### 7 — Sorting: Bubble and Selection

**Files:** [`7a_bubble_sort.py`](7a_bubble_sort.py),
[`7b_selection_sort.py`](7b_selection_sort.py) · **Input:** none — arrays set in source

**7a — Bubble sort** compares adjacent elements and swaps them when out of order, so the
largest unsorted element bubbles to its final position on each pass. A `swapped` flag breaks
out of the loop when a pass makes no exchanges, which is what gives the algorithm its `O(n)`
best case on already-sorted input. Both programs sort the list in place and return `None`.

```text
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]
```

**7b — Selection sort** finds the minimum of the unsorted portion on each pass and swaps it
into place, performing at most `n − 1` swaps in total — far fewer writes than bubble sort,
though the comparison count stays quadratic in every case. Bubble sort is stable; selection
sort, because of the long-range swap, is not.

```text
Original array: [29, 10, 14, 37, 13]
Sorted array: [10, 13, 14, 29, 37]
```

---

## Complexity Summary

| #        | Operation                        | Concept              | Time                            | Space          |
| :------- | :------------------------------- | :------------------- | :------------------------------ | :------------- |
| 1        | Getter / setter call             | Encapsulation        | `O(1)`                          | `O(1)`         |
| 2        | `area()` / `perimeter()`         | Abstraction          | `O(1)`                          | `O(1)`         |
| 3a       | Variadic `add(*args)`            | Overloading          | `Θ(n)` over the arguments       | `O(n)` tuple   |
| 3b       | Overridden `description()`       | Overriding           | `O(1)` dispatch                 | `O(1)`         |
| 4a–4c    | List / dict / set comprehension  | Eager iteration      | `Θ(n)`                          | `Θ(n)`         |
| 4d       | Generator expression             | Lazy iteration       | `Θ(n)` fully consumed           | `O(1)`         |
| 5        | `combinations(n, r)`             | Combinatorics        | `Θ(C(n, r) × r)` to enumerate   | `O(r)`         |
| 6a       | Linear search                    | Sequential search    | `O(n)`, `O(1)` best             | `O(1)`         |
| 6b       | Binary search                    | Divide and conquer   | `O(log n)`, `O(1)` best         | `O(1)`         |
| 7a       | Bubble sort                      | Comparison sort      | `O(n)` best, `O(n²)` otherwise  | `O(1)`         |
| 7b       | Selection sort                   | Comparison sort      | `Θ(n²)` in all cases            | `O(1)`         |

`n` = number of elements or arguments, `r` = combination size. Bubble sort reaches its `O(n)`
best case only because of the early-exit flag in `7a`; the textbook version without it is
`Θ(n²)` even on sorted input.

## Known Issues

These programs run correctly on their intended inputs but crash on inputs outside that range.
They are documented here rather than silently omitted.

| File                                       | Symptom                                                       | Cause                                                                                                                                                                    |
| :----------------------------------------- | :------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`2_inheritance.py`](2_inheritance.py)     | `ValueError: expected a nonnegative input` on sides `1 2 10`  | Heron's formula is applied without first checking the triangle inequality, so `s(s−a)(s−b)(s−c)` goes negative and `math.sqrt` rejects it. Valid triangles are unaffected. |
| [`2_inheritance.py`](2_inheritance.py), [`6a_linear_search.py`](6a_linear_search.py), [`6b_binary_search.py`](6b_binary_search.py) | Unhandled `ValueError` on non-numeric input | `int(input(...))` and `float(input(...))` are called without a `try`/`except`, so any non-numeric entry propagates a traceback instead of re-prompting. |

Fixes for any of these are welcome.

## Coding Conventions

- **Version:** Python 3, run as `python <file>.py` with no flags.
- **Style:** [PEP 8](https://peps.python.org/pep-0008/) — four-space indentation,
  `snake_case` for functions and variables, `PascalCase` for classes.
- **Structure:** class and function definitions first, followed by driver code under a
  `# Main Program` comment; experiment 2 wraps its driver in `main()` behind an
  `if __name__ == "__main__":` guard.
- **Dependencies:** standard library only — every file runs with a single `python` command.
- **Documentation:** each file opens with a comment naming the concept it demonstrates, and
  numbered step comments mark the stages of the shorter scripts.

## Author(s)

- **Mrs. A. Rama Madhuri** — II-I B.Tech, Data Structures & Algorithms Faculty.
- **Mrs. N. Anusha** — II-I B.Tech, Data Structures & Algorithms Faculty.
- **Mr. Joshua Udaya Teja** — Dr C.R. Rao Laboratory Assistant (Lab: 109).

## License

Released under the [MIT License](LICENSE). These programs are lab coursework, published for
reference and study.
