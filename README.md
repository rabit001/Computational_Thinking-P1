Computational_Thinking-P1

Task 1: Identity Investigation

 Objective:
To check how memory IDs change when variables are modified.

 Action:
Created a file `identity_rabit_mansuri.py` and printed IDs before and after changing values.

 Observation:
- Integer, String, Tuple → ID changes  
- List → ID remains same  

 Conclusion:
Immutable types create new memory, while mutable types modify existing memory.

 Task 2: Nature of Commit History

 Action:
Created a repository and made multiple commits like "Version 1" and "Version 2".

 Question:
Does "Version 2" still exist?

 Answer:
Yes, both versions exist in Git history.

Explanation:
Git does not overwrite commits. Instead, it creates new commits for every change, preserving all versions.

 Conclusion:
Git stores all versions permanently, proving commits are immutable.

 Task 3: Shallow Copy Behavior

Action:
Created a nested list and copied it using `list()`, then modified the copied list.

 Observation:
The original list also changed.

 Explanation:
Shallow copy shares inner references, so changes affect both lists.

Conclusion:
Deep copy should be used to avoid this issue.
Task 4: Commit Immutability

 Action:
Created a commit, noted its hash, then modified the commit message using `git commit --amend`.

 Observation:
The commit hash changed.

Explanation:
Commit hash depends on content and metadata, so any change creates a new commit.

 Conclusion:
Git commits are immutable and cannot be changed once created.