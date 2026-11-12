# Computational Thinking – Practical Exercises

A collection of practical exercises exploring Python object identity, mutability, shallow copying, and Git commit history.

This repository records observations and conclusions from the Computational Thinking coursework.

## Exercises

### 1. Identity Investigation

**Objective:** Observe how object identity changes when values are modified.

**Activity:** Created `identity_rabit_mansuri.py` and printed object IDs before and after changing values.

**Recorded observations:**
- Integer, string, and tuple: the ID changed after reassignment.
- List: the ID remained the same when its contents were modified.

**Conclusion:** The exercise illustrates the difference between immutable and mutable objects. Reassignment of an immutable value can refer to a new object, while modifying a list in place preserves the list object's identity.

### 2. Understanding Git Commit History

**Activity:** Created a repository and made multiple commits, including commits named "Version 1" and "Version 2".

**Question:** Does "Version 2" replace "Version 1"?

**Observation:** Both commits remain available in the repository's reachable Git history.

**Conclusion:** Git records changes as new commits rather than overwriting earlier commits. This makes it possible to inspect and compare previous versions.

### 3. Shallow Copy Behaviour

**Activity:** Created a nested list, copied it using Python's `list()` constructor, and then modified the copied list.

**Observation:** A change to a nested object through the copied list was also visible through the original list.

**Conclusion:** A shallow copy creates a new outer list but keeps references to the same nested objects. A deep copy is useful when independent copies of nested objects are required.

### 4. Commit Immutability

**Activity:** Created a commit, noted its hash, and then changed its commit message using `git commit --amend`.

**Observation:** The amended commit had a different hash.

**Conclusion:** A commit hash is calculated from the commit's content and metadata. Amending a commit creates a new commit object with a new hash.

## Concepts Covered

- Python object identity
- Mutable and immutable data types
- Shallow and deep copying
- Git commits and version history
- Commit hashes and `git commit --amend`

## Tools

- Python
- Git
- GitHub

---

**Author:** [Rabit Mansuri](https://github.com/rabit001)
