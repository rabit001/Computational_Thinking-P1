Old Commit Hash: ccd937c9edd849e39ccf596e853bbc60b02213f7 

New Commit Hash: 5be3853b0d8f28f66fbfbbf0ff7fd7861cc30a40

Observation:
After updating the commit message, the commit hash was different from the previous one.

Reason:
In Git, a commit hash is created using the commit’s data, including its content, message, and metadata like author and time. When the commit message was changed, Git did not modify the existing commit but generated a completely new commit with a new hash.

This demonstrates that Git commits are immutable, meaning they cannot be altered once created, and any change results in a new commit.