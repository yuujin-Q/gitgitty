# gitgitty
## Implementation
Gitgitty is implemented using Python. For version control, gitgitty uses snapshots for a simpler implementation at the cost of storage.

When a repository is created, a folder `.gitgitty` is created with the following structure
```
.gitgitty
└───snapshots/
└───log
└───head

```