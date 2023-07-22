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

## C References

```c
#include <stdio.h>

NULL  // null pointer
EOF   // end of file
FILE  // file data structure
int BUFSIZ;
int OPEN_MAX;

FILE *stdin;   // std in, fd=0
FILE *stdout;  // std out, fd=1
FILE *stderr;  // std error, fd=2

FILE *fopen(char *name, char *mode);             // open
int flose(FILE *fp);                             // close

char getc(FILE *fp);                             // read a char
int putc(char c, FILE* fp);                      // write a char

char *fgets(char *line, int maxline, FILE *fp);  // read a line
int fputs(char *line, FILE *fp);                 // write a line

int fileno(FILE *fp);                            // file descriptor

int ferror(FILE *fp);  // return non-zero when error occured
int feof(FILE *fp);    // return non-zero when end of file

int fflush(FILE *fp);                                     // flush buffer, flush(NULL) flush all streams (fp)
int setvbuf(FILE *fp, char *buf, int mode, size_t size);  // set stream buffering
void setbuf(FILE *fp, char *buf);                         // = (void) setvbuf(fp, buf, _IOFBF, BUFSIZ)
```

## References Implementation

```c
#include <stdio.h>

#define NULL (0)  // null pointer
#define EOF (-1)  // end of file
#define BUFSIZ 1024  // standard I/O buffer size
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


#define stdin (&_iob[0])   // FILE *stdin,  fd=0
#define stdout (&_iob[1])  // FILE *stdout, fd=1
#define stderr (&_iob[2])  // FILE *stderr, fd=2


enum _flags {
    _READ = 01,  /* file open for reading */
    _WRITE = 02, /* file open for writing */
    _UNBUF = 04, /* file is unbuffered */
    _EOF = 010,  /* EOF has occurred on this file */
    _ERR = 020   /* error occurred on this file */
};


int _fillbuf(FILE *);
int _flushbuf(int, FILE *);


#define feof(p) ((p)->flag & _EOF) != 0)
#define ferror(p) ((p)->flag & _ERR) != 0)
#define fileno(p) ((p)->fd)


#define getc(p) (--(p)->cnt >= 0 \
    ? (unsigned char) *(p)->ptr++ : _fillbuf(p))
#define putc(x,p) (--(p)->cnt >= 0 \
    ? *(p)->ptr++ = (x) : _flushbuf((x),p))

#define getchar() getc(stdin)
#define putcher(x) putc((x), stdout)
```

### `open()`

```c
#include <stdio.h>
#include <fcntl.h>
#define PERMS 0666  /* RW for owner, group, others */

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

### `fgets()`

```c
/** Reference implementations of `fgets()`. */

#include <stdio.h>

/** get a line, at most `n` chars, from file `fp`. */
char *fgets(char *s, int n, FILE *fp)
{
    register int c;
    register char *cs;

    cs = s;
    while (--n > 0 && (c = getc(fp)) != EOF)
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

/** put string `s` on file `fp`. */
int fputs(char *s, FILE *fp)
{
    int c;

    while (c = *s++)
        putc(c, fp);
    return ferror(fp) ? EOF : 0;
}
```

## References

- Book: *The C Programming Language, Second Edition* (1989)
