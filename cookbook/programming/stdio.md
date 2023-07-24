# Standard I/O

## C Recipes

```c
#include <stdio.h>

#define BUF_SIZE 4096
#define MAX_CHARS_ONE_LINE 1024

char *buf[BUF_SIZE] = "";

FILE *fp;
char *filename = "xxx.txt";

if (fp = fopen(filename, "r") != NULL) {
    fgets(buf, MAX_CHARS_ONE_LINE, fp);
    fclose(fp);
}

if (fp = fopen(filename, "w") != NULL) {
    fputs(buf, fp);
    fclose(fp);
}
```

## C Function Signature

```c
#include <stdio.h>

NULL  // null pointer
EOF   // end of file
FILE  // file data structure
const int BUFSIZ;
const int OPEN_MAX;  /* max #files open at once */

const FILE *stdin;   // std in, fd=0
const FILE *stdout;  // std out, fd=1
const FILE *stderr;  // std error, fd=2

FILE *fopen(char *name, char *mode);             // open
int flose(FILE *stream);                         // close

char getc(FILE *stream);                         // read a char
int putc(char c, FILE* stream);                  // write a char

char *fgets(char *line, int maxline, FILE *stream);  // read a line
int fputs(char *line, FILE *stream);                 // write a line

int fileno(FILE *stream);  // file descriptor, `_POSIX_C_SOURCE` for glibc

int ferror(FILE *stream);  // return non-zero when error occured
int feof(FILE *stream);    // return non-zero when end of file
void clearerr(FILE *stream);

char *gets(char *s);  // obsolescent in POSIX.1-2008 and `_ISOC11_SOURCE` for glibc
```

### reposition a stream

```c
#include <stdio.h>

int fseek(FILE *stream, long offset, int whence);
long ftell(FILE *stream);

void rewind(FILE *stream);  // = (void)fseek(stream, 0L, SEEK_SET)
int fgetpos(FILE *stream, fpos_t *pos);
int fsetpos(FILE *stream, const fpos_t *pos);

/* long -> off_t */
/* `_FILE_OFFSET_BITS == 64 || _POSIX_C_SOURCE >= 200112L` */
int fseeko(FILE *stream, off_t offset, int whence);
off_t ftello(FILE *stream);
```

### stream buffering operations

```c
#include <stdio.h>

int fflush(FILE *stream);  // flush buffer, flush(NULL) flush all streams

int setvbuf(FILE *stream, char *buf, int mode, size_t size);  // set stream buffering

void setbuf(FILE *stream, char *buf);                   // = (void)setvbuf(stream, buf, _IOFBF, BUFSIZ)
void setbuffer(FILE *stream, char *buf, size_t size);   // = (void)setvbuf(stream, buf, _IOFBF, size), `_DEFAULT_SOURCE` since glibc 2.19
void setlinebuf(FILE *stream);                          // = (void)setvbuf(stream, NULL, _IOLBF, 0),  `_DEFAULT_SOURCE` since glibc 2.19
```

### binary stream input/output

```c
#include <stdio.h>

/* binary stream input/output */
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);
```

## References Implementation

```c
#include <stdio.h>

#define NULL (0)  // null pointer
#define EOF (-1)  // end of file
#define BUFSIZ 1024  // standard I/O buffer size
```

### `FILE`

```c
#include <unistd.h>

#define OPEN_MAX 20  /* max #files open at once */

/* file data structure */
typedef struct _iobuf {
    int cnt;    /* characters left */
    char *ptr;  /* next character position */
    char *base; /* location of buffer */
    int flag;   /* mode of file access */
    int fd;     /* file descriptor */
} FILE;
extern FILE _iob[OPEN_MAX];

#define stdin (&_iob[STDIN_FILENO])   // FILE *stdin,  fd=0 (STDIN_FILENO)
#define stdout (&_iob[STDIN_FILENO])  // FILE *stdout, fd=1 (STDOU_FILENO)
#define stderr (&_iob[STDIN_FILENO])  // FILE *stderr, fd=2 (STDERR_FILENO)
```

### `fopen()`

```c
#include <fcntl.h>
#define OPEN_MAX 20  /* max #files open at once */
#define PERMS 0666  /* RW for owner, group, others */

enum _flags {
    _READ = 01,  /* file open for reading */
    _WRITE = 02, /* file open for writing */
    _UNBUF = 04, /* file is unbuffered */
    _EOF = 010,  /* EOF has occurred on this file */
    _ERR = 020   /* error occurred on this file */
};

FILE *fopen(char *name, char *mode)
{
    int fd;
    FILE *fp;

    if (*mode != 'r' && *mode != 'w' && *mode != 'a')
        return NULL;

    for (fp = _iob; fp < _iob + OPEN_MAX; fp++)
        if ((fp->flag & (_READ | _WRITE)) == 0)
            break; /* found free slot */

    if (fp >= _iob + OPEN_MAX)  /* no free slots */
        return NULL;

    if (*mode == 'w')
        fd = creat(name, PERMS);
    else if (*mode == 'a') {
        if ((fd = open(name, O_WRONLY, 0)) == -1)
            fd = creat(name, PERMS);
        lseek(fd, 0L, 2);
    } else
        fd = open(name, O_RDONLY, 0);

    if (fd == -1) /* couldn't access name */
        return NULL;

    fp->fd = fd;
    fp->cnt = 0;
    fp->base = NULL;
    fp->flag = (*mode == 'r') ? _READ : _WRITE;
    return fp;
}
```

### `ferror()`, `feof()`, `fileno()`

```c
enum _flags {
    _READ = 01,  /* file open for reading */
    _WRITE = 02, /* file open for writing */
    _UNBUF = 04, /* file is unbuffered */
    _EOF = 010,  /* EOF has occurred on this file */
    _ERR = 020   /* error occurred on this file */
};

#define feof(p) ((p)->flag & _EOF) != 0)
#define ferror(p) ((p)->flag & _ERR) != 0)
#define fileno(p) ((p)->fd)
```

### `getc()` / `putc()` / `getchar()` / `putchar()`

```c
#include <stdio.h>

unsigned char _fillbuf(FILE *);
int _flushbuf(int, FILE *);


#define getc(p) (--(p)->cnt >= 0 \
    ? (unsigned char) *(p)->ptr++ : _fillbuf(p))
#define putc(x,p) (--(p)->cnt >= 0 \
    ? *(p)->ptr++ = (x) : _flushbuf((x),p))


#define getchar() getc(stdin)
#define putcher(x) putc((x), stdout)
```

### `fgets()`

```c
/** Reference implementations of `fgets()`. */

#include <stdio.h>

/** get a line, at most `n` chars, from file `stream`. */
char *fgets(char *s, int n, FILE *stream)
{
    register int c;
    register char *cs;

    cs = s;
    while (--n > 0 && (c = getc(stream)) != EOF)
        if ((*cs++ = c) == '\n')
            break;
    *cs = '\0';
    return (c == EOF && cs == s) ? NULL : s;
}
```

### `fputs()`

```c
/** Reference implementations of `fputs()`. */

#include <stdio.h>

/** put string `s` on file `stream`. */
int fputs(char *s, FILE *stream)
{
    int c;

    while (c = *s++)
        putc(c, stream);
    return ferror(stream) ? EOF : 0;
}
```

## More

- [UNIX I/O (System Call I/O)](syscall_io)

## References

- Book: *The C Programming Language, Second Edition* (1989)
- [`stdio`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/stdio.3.en.html)
- [`fopen`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/fopen.3.en.html)
- [`fclose`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/fclose.3.en.html)
- [`fflush`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/fflush.3.en.html)
- [`feof`, `ferror`, `clearerr`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/feof.3.en.html)
- [`fgets`, `fgetc`, `getc`, `getchat`, `ungetc`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/fgets.3.en.html)
- [`gets`(3) - Debian Manpages (obsoleted)](https://manpages.debian.org/bookworm/manpages-dev/fgets.3.en.html)
- [`fputs`, `fputc`, `putc`, `putchar`, `puts`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/fputs.3.en.html)
- [`fseek`, `ftell`, `rewind`, `fgetpos`, `fsetpos`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/fseek.3.en.html)
- [`fseek0`, `ftell0`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/fseeko.3.en.html)
- [`setvbuf`, `setbuf`, `setbuffer`, `setlinebuf`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/setvbuf.3.en.html)
- [`fread`, `fwrite`(3) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/fread.3.en.html)
