# UNIX I/O (System call)

## C Recipes

```c
#include <fcntl.h>
#include <errno.h>

int fd;
const char *pathname = "x.txt";
char *buf[1024];
ssize_t n;

/* r */
if ((fd = open(pathname, O_RDONLY, 0)) != -1)
{
    // read
    while (true) {
        n = read(fd, buf, sizeof(buf));
        if (n == -1 && errno == EINTR) {
            continue;
        }
        break;
    }

    if (n == -1) {
        // handle errors
    }

    else if (n == 0) {
        // handle EOF
    }

    else {
        // handle buffer
    }

    close(fd);
}

/* w */
if ((fd = open(pathname, O_WRONLY, 0)) != -1)
{
    // write
    write(fd, buf, buf_size);
    close(fd);
}

/* a */
if ((fd = open(pathname, O_WRONLY|O_APPEND, 0)) != -1)
{
    // append
    write(fd, buf, buf_size);
    close(fd);
}

/* r+ */
if ((fd = open(pathname, O_RDWR, 0)) != -1)
{
    // read & write
    read(fd, buf, buf_size);
    write(fd, buf, buf_size);
    close(fd);
}
```

## System Call Prototype

### `stdin`, `stdout`, `stderr`

```c
#include <unistd.h>

const int STDIN_FILENO = 0
const int STDOUT_FILENO = 1
const int STDERR_FILENO = 2
```

### `open()`, `create()`, `openat()`

```c
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

/**
    `flags`:
        basic:
            - O_RDONLY
            - O_WRONLY
            - O_RDWR
        additional:
            - O_CREAT
            - O_TRUNC
            - O_APPEND

    `mode`: 0
 */
int open(const char *pathname, int flags);
int open(char *pathname, int flags, mode_t mode);

/* open(pathname, O_WRONLY|O_CREAT|O_TRUNC, mode); */
int creat(const char *pathname, mode_t mode);

#define _POSIX_C_SOURCE >= 200809L  // glibc 2.10+
#define _ATFILE_SOURCE              // glibc 2.10-
int openat(int dirfd, const char *pathname, int flags);
int openat(int dirfd, const char *pathname, int flags, mode_t mode);
```

### `openat2()`

```c
#include <fcntl.h>          /* Definition of O_* and S_* constants */
#include <linux/openat2.h>  /* Definition of RESOLVE_* constants */
#include <sys/syscall.h>    /* Definition of SYS_* constants */
#include <unistd.h>

/**
openat() extension.

This system call is Linux-specific, since Linux 5.6.
*/
struct open_how how = { .flags = O_RDWR,
                        .resolve = RESOLVE_IN_ROOT };
long syscall(SYS_openat2, int dirfd, const char *pathname,
             struct open_how *how, size_t size);
```

### `close()`

```c
#include <unistd.h>

int close(int fd);
```

### `read()`

```c
#include <unistd.h>

/**
copies at most `n` bytes from the current file position of `fd`
to memory location `buf`.

returns
    - -1: error
    - 0: EOF
    - others: number of bytes transferred

On Linux, read() (and similar system calls) will transfer
at most 0x7ffff000 (2,147,479,552) bytes,
returning the number of bytes actually transferred.
(This is true on both 32-bit and 64-bit systems.)
*/
ssize_t read(int fd, void *buf, size_t n);
```

### `write()`

```c
#include <unistd.h>

/**
copies at most `n` bytes from memory location `buf`
to the current file position of `fd`.
 */
ssize_t write(int fd, const void *buf, size_t n);
```

### `lseek()`

```c
#define _FILE_OFFSET_BITS 64

#include <sys/types.h>
#include <unistd.h>

/**
reposition read/write file offset

whence:
    - SEEK_SET
    - SEEK_CUR
    - SEEK_END

    _GNU_SOURCE:
    - SEEK_DATA
    - SEEK_HOLE

        supported filesystems:
        - Btrfs (since Linux 3.1)
        - OCFS (since Linux 3.2)
        - XFS (since Linux 3.5)
        - ext4 (since Linux 3.8)
        - tmpfs(5) (since Linux 3.8)
        - NFS (since Linux 3.18)
        - FUSE (since Linux 4.5)
        - GFS2 (since Linux 4.15)

On Linux, using `lseek()` on a terminal device fails with the error `ESPIPE`.
 */
off_t lseek(int fd, off_t offset, int whence);

#define _LARGEFILE64_SOURCE
off64_t lseek64(int fd, off64_t offset, int whence);
```

## Python APIs

### `sys.stdin`, `sys.stdout`, `sys.stderr`

```python
import sys

sys.stdin
sys.stdout
sys.stderr
```

### `os.open()`, `os.fdopen()`, `os.close()`, `os.closerange()`

```python
import os
from pathlib import Path

os.open(path: Path | str, flags, mode=0o777, *, dir_fd: int | None = None)

os.close(fd: int)
os.closerange(fd_low: int, fd_high: int, /)
```

### `os.read()`, `os.write()`, `os.readv()`, `os.writev()`, `os.lseek()`

```python
import os
from collection.abc import Sequence
from typing import Literal

os.read(fd: int, n: int, /) -> bytes
os.write(fd: int, buf: bytes, /) -> int

# os.sysconf('SC_IOV_MAX') to set a limit on the number of buffers.
os.readv(fd: int, buffers: Sequence[bytes], /) -> int
os.writev(fd: int, buffers: Sequence[bytes], /) -> int

os.lseek(fd: int, pos: int, how: Literal[os.SEEK_SET, os.SEEK_CUR, os.SEEK_END], /)
```

## References

- Book: *Computer Systems: A Programmer's Perspective, Third Edition* (2016)
- [`open`, `create`, `openat`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/open.2.en.html)
- [`openat2`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/openat2.2.en.html)
- [`close`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/close.2.en.html)
- [`read`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/read.2.en.html)
- [`write`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/write.2.en.html)
- [`lseek`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/lseek.2.en.html)
- [`lseek64`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/lseek64.3.en.html)
- [`os.open()` - Python](https://docs.python.org/3/library/os.html#os.open)
- [`os.fdopen()` - Python](https://docs.python.org/3/library/os.html#os.fdopen)
- [`os.close()` - Python](https://docs.python.org/3/library/os.html#os.close)
- [`os.closerange()` - Python](https://docs.python.org/3/library/os.html#os.closerange)
- [`os.read()` - Python](https://docs.python.org/3/library/os.html#os.read)
- [`os.write()` - Python](https://docs.python.org/3/library/os.html#os.write)
- [`os.readv()` - Python](https://docs.python.org/3/library/os.html#os.readv)
- [`os.writev()` - Python](https://docs.python.org/3/library/os.html#os.writev)
- [`os.lseek()` - Python](https://docs.python.org/3/library/os.html#os.lseek)
