# Search Files: `find`

## Recipes

```bash
find <dir> <text-expr> [<logic-opertor ...>] <act>
    -name <file-pattern>
    -type f|d|l|b|c
    -size <N>c|k|M|G
    -empty
    -usr <user-name>
    -uid <uid>
    -cmin [-|+]<N-min>
    -ctime [-|+]<N-day>
    -inum <inode>

    -and
    -or
    -not
    ()

    -print
    -printf <fmt>
    -fprintf <file> <fmt>
    -delete
    -ls
    -exec <cmd> '{}' ';'|+
```
