# Environment Variables

```bash
echo $SHELL  # current shell
echo $PWD   # current directory
echo $USER  # current user name
echo $HOME  # home directory of current user
echo $PATH  # system path
```

## Permenant Setting

`~/.bashrc` or `~/.bash_profile`:

```bash
export X="xxx"
export PATH="xxx:$PATH"
```

Run:

```bash
. ~/.bashrc
```

or

```bash
source ~/.bashrc
```

## Temporary Disable

```bash
unset XXX
```

## GNU comformance to POSIX

### `POSIXLY_CORRECT`

GNU utility conformance to POSIX Std.

```bash
export POSIXLY_CORRECT=true
```

### Different POSIX Std version

```bash
# POSIX 1003.1-2001
export _POSIX2_VERSION=200112

# POSIX 1003.2-1992
export _POSIX2_VERSION=199209
```
