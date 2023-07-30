# Date & Time: `date` (GNU `coreutils`)

## Recipes

```bash
date <+format>
    %% - '%'
    %H - hour (00-23)
    %I - hour (01-12)
    %M - minute (00-59)
    %S - second (00-59)
    %T - %H:%M:%S
    %R - %H:%M
    %y - year (00-99)
    %Y - year (0000-9999)
    %m - month (01-12)
    %d - day of month (01-31)
    %D - %m/%d/%y
    %u - day of week (1-7, 1=Monday)
    %w - day of week (0-6, 0=Sunday)
    %n - newline ('\n')
    %t - tab ('\t')
```

## Date & Time Format

- [Representation of Date & Time - ISO 8601 Format](../general_concepts/datetime_fmt_iso_8601)
- [Representation of Date & Time - RFC 3339 Format](../general_concepts/datetime_fmt_rfc_3339)

## References

- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/html_node/index.html)
- [Coreutils - Debian Wiki](https://wiki.debian.org/coreutils)
