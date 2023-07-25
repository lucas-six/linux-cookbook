# File Metadata

## C Recipes

```c
#include <sys/stat.h>

struct stat stat;
const char *pathname = "x.txt";

stat(pathname, &stat);

if (S_ISREG(stat.st_mode)) {
    // is a regular file
} else if (S_ISDIR(stat.st_mode)) {
    // is a directory
}

if (stat.st_mode & S_IRUSR) {
    // user can read
}
```

## System Call Signature

### `stat`

```c
#include <sys/stat.h>

/* Metadata returned by the stat and fstat functions */
struct stat {
    dev_t           st_dev; /* Device */
    ino_t           st_ino; /* inode */
    mode_t          st_mode; /* Protection and file type */
    nlink_t         st_nlink; /* Number of hard links */
    uid_t           st_uid; /* User ID of owner */
    gid_t           st_gid; /* Group ID of owner */
    dev_t           st_rdev; /* Device type (if inode device) */
    off_t           st_size; /* Total size, in bytes */
    unsigned long   st_blksize; /* Blocksize for filesystem I/O */
    unsigned long   st_blocks; /* Number of blocks allocated */
    time_t          st_atime; /* Time of last access */
    time_t          st_mtime; /* Time of last modification */
    time_t          st_ctime; /* Time of last change */
};
```

### `stat()`, `fstat()`, `lstat()`

```c
#include <sys/stat.h>

S_ISREG()  // Is this a regular file?
S_ISDIR()  // Is this a directory file?
S_ISSOCK() // Is this a network socket?


int stat(const char *restrict pathname,
         struct stat *restrict statbuf);
int fstat(int fd, struct stat *statbuf);


/**
for symbolic link itself.

glibc 2.20+: `_DEFAULT_SOURCE`
glibc 2.10+: `_POSIX_C_SOURCE >= 200112L`
glibc 2.19-: `_BSD_SOURCE`
 */
int lstat(const char *restrict pathname,
         struct stat *restrict statbuf);
```

### `fstatat()`

```c
/**
glibc 2.10+: `_POSIX_C_SOURCE >= 200809L`
glibc 2.10-: `_ATFILE_SOURCE`
 */

#include <fcntl.h>           /* Definition of AT_* constants */
#include <sys/stat.h>

int fstatat(int dirfd, const char *restrict pathname,
            struct stat *restrict statbuf, int flags);
```

## Python APIs

### `os.stat()`, `os.fstat()`, `os.lstat()`

```python
import os
from pathlib import Path

os.stat(path: str | bytes | Path,
        *,
        dir_fd: int | None = None,
        follow_symlinks: bool = True) -> os.stat_result
# os.fstat()
# os.lstat()
```

## References

- Book: *Computer Systems: A Programmer's Perspective, Third Edition* (2016)
- [`stat`, `fstat`, `lstat`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/stat.2.en.html)
- [`fstatat`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/fstatat.2.en.html)
- [`os.stat()` - Python](https://docs.python.org/3/library/os.html#os.stat)
- [`os.fstat()` - Python](https://docs.python.org/3/library/os.html#os.fstat)
- [`os.lstat()` - Python](https://docs.python.org/3/library/os.html#os.lstat)
- [`os.stat_result` - Python](https://docs.python.org/3/library/os.html#os.stat_result)
