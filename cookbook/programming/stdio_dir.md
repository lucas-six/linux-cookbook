# Standard I/O (Standard C Library): Directory

## C Recipes

```c
#include <sys/types.h>
#include <dirent.h>
#include <libgen.h>
#include <errno.h>
#include <stdlib.h>

int main(void)
{
    DIR *dir;
    struct dirent *dp;

    if ((dir = opendir(".")) == NULL) {
        perror("Cannot open .");
        exit(1);
    }

    /*
    If the end of the directory stream is reached,
    NULL is returned and errno is not changed.
    If an error occurs,
    NULL is returned and errno is set to indicate the error.
    To distinguish end of stream from an error,
    set errno to zero before calling readdir()
    and then check the value of errno if NULL is returned.
    */
    errno = 0
    while ((dp = readdir(dir)) != NULL) {
        printf("found file: %s\n", dp->d_name);
    }
    if (errno != 0) {
        perror("read failed");
        exit(1);
    }

    closedir(dir);
    exit(0);
}
```

### `scandir()` Recipe

```c
#define _DEFAULT_SOURCE
#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    struct dirent **namelist;
    int n;

    n = scandir(".", &namelist, NULL, alphasort);
    if (n == -1) {
        perror("scandir");
        printf("%s\n", namelist[n]->d_name);
        free(namelist[n]);
    }

    free(namelist);
    exit(EXIT_SUCCESS);
}
```

## C Function Prototype

### `opendir()`, `fdopendir()`, `DIR`

```c
#include <sys/types.h>
#include <dirent.h>

DIR *opendir(const char *pathname);

/**
glibc 2.10+: `_POSIX_C_SOURCE >= 200809L`
glibc 2.4-2.9: `_GNU_SOURCE`
 */
DIR *fdopendir(int fd);
```

### `closedir()`

```c
#include <sys/types.h>
#include <dirent.h>

int closedir(DIR *dirp);
```

### `readdir()`

```c
#include <dirent.h>

/**
On success, `readdir()` returns a pointer to a dirent structure.
(This structure may be statically allocated; do not attempt to `free()` it.)
 */
struct dirent *readdir(DIR *dirp);
```

```c
/* glibc implementation of `dirent` */
struct dirent {
    ino_t          d_ino;       /* Inode number */
    off_t          d_off;       /* Not an offset; see below */
    unsigned short d_reclen;    /* Length of this record */
    unsigned char  d_type;      /* Type of file; not supported
                                   by all filesystem types */
    char           d_name[256]; /* Null-terminated filename */
};
```

### `scanndir()`

```c
#include <dirent.h>

/* glibc 2.10+: `_POSIX_C_SOURCE >= 200809L` */
int scandir(const char *restrict dirp,
            struct dirent ***restrict namelist,
            int (*filter)(const struct dirent *),
            int (*compar)(const struct dirent **,
                          const struct dirent **));

/* glibc 2.10+: `_POSIX_C_SOURCE >= 200809L` */
int alphasort(const struct dirent **a, const struct dirent **b);

/* _GNU_SOURCE */
int versionsort(const struct dirent **a, const struct dirent **b);
```

### `scandirat()`

```c
#include <fcntl.h>          /* Definition of AT_* constants */
#include <dirent.h>

/* _GNU_SOURCE */
int scandirat(int dirfd, const char *restrict dirp,
            struct dirent ***restrict namelist,
            int (*filter)(const struct dirent *),
            int (*compar)(const struct dirent **,
                          const struct dirent **));
```

### `seekdir()`

```c
#include <dirent.h>

/* glibc 2.19: _DEFAULT_SOURCE */
void seekdir(DIR *dirp, long loc);
```

### `telldir()`

```c
#include <dirent.h>

/* glibc 2.19: _DEFAULT_SOURCE */
long telldir(DIR *dirp);
```

## Python APIs

### `os.scandir()`, `os.DirEntry`

```python
import os
from pathlib import Path

os.scandir(path: Path | bytes | str) -> os.DirEntry

with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(f'file: {entry.name}')
        elif entry.is_dir():
            print(f'dir: {entry.name}')
```

## References

- Book: *Computer Systems: A Programmer's Perspective, Third Edition* (2016)
- [`opendir`, `fdopendir`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/opendir.3.en.html)
- [`readdir`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/readdir.3.en.html)
- [`scandir`, `alphasort`, `versionsort`, `scandirat`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/scandir.3.en.html)
- [`seekdir`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/seekdir.3.en.html)
- [`telldir`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/telldir.3.en.html)
- [`os.scandir()` - Python](https://docs.python.org/3/library/os.html#os.scandir)
- [`os.DirEntry()` - Python](https://docs.python.org/3/library/os.html#os.DirEntry)
