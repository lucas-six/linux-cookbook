cookbook
==================

Cookbook

- [Bash Guide](#bash-guide)
- [Regular Expression](#regular-expression)
- [Doxygen Guide](#doxygen-guide)
- [Git Workflow](#git-workflow)
- [Git Server](#git-server)

## Bash Guide

### Key Bindings

- `Tab` - Completion
- `Ctrl+D` - `exit` or EOF
- `Ctrl+C` - SIGTERM
- `Ctrl+A` / `Ctrl+E` - GoTo beginning/end of command line
- `Ctrl+U` / `Ctrl+K` - Cut from current position to beginning/end of commands
- `Ctrl+Y` - Paste
- `Ctrl+L` - `clear`
- `Ctrl+R` - History Search, `Ctrl+C` to quit
- `Ctrl+Z` - SIGSTP

### Expansion

```bash
$ echo text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER
text /home/ly/a.txt a b A B C a 2 ly

$ echo "text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER"
text ~/*.txt {a,b} {A..C} a 2 ly

$ echo 'text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER'
text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER
```

### I/O Redirection

```bash
# Redirect stderr
ls -l /bin/usr 2> ls-error.log

# Redirect stdout and stderr to one file
ls -l /bin/usr > ls.log 2>&1
```

In bash v4.0+, a more streamlined method for performing this combined
redirection:


```bash
ls -l /bin/usr &> ls.log
```

Sometimes "silence is golden", and we don't want output from a command.

```bash
ls -l /bin/usr > /dev/null 2>ls.log
```

### File Testing Operator

```
-e exist
-s NOT empty
-f regular file
-d directory
-S socket
-p named pipe
-h symbolic link
-r readable
-w writable
-nt newer than
-ot older than
-ef hard link
```

### Text Processing

```bash
# Substitute
str="a-b-c"
echo ${str/-/_}_d # a_b-c_d
echo ${str//-/_}_d # a_b_c_d

# Substring
str="abcdef"
echo ${str:1} # a
echo ${str:2:2} # bc

# Testing Operator
-z empty
-n NOT empty
```

## Regular Expression

 - `*` - Any numbers of characters
 - `?` - Any single of character
 - `[abc]` - Any character in set of `abc`
 - `[!abc]` - Any character NOT in set of `abc`
 - `[:alpha:]` - Any letter
 - `[:lower:]` - Any lower-case letter
 - `[:upper:]` - Any upper-case letter
 - `[:digit:]` - Any digit
 - `[:alnum:]` - Any letter or digit
 - `[:word:]` - `[:alnum:]` + `_`
 - `[:blank:]` - `Space` + `Tab`
 - `^abc` - Any line starting with `abc`
 - `abc$` - Any line ending with `abc`
 - `+` - More than once
 - `{n}`, `{n,m}` - from (n) to (m) times


## Doxygen Guide

More details on Doxygen, please refer to the on-line manual:

    http://www.stack.nl/~dimitri/doxygen/manual/

**STEP 1**: Doc code

```python
# Python code
## <function-or-method-description>.
#
# @param <param-name> <param-description>
# @return <return-name> <return-description>
# @exception <exception-name> <exception-description>
def func_or_method():
	'''<function-or-method-description>.
	'''
	# func or method definition
'''
@warning <warning-messages>
@todo <things to be done>
@deprecated
@see <reference to others>
@since <version>
'''
```

**STEP 2**: Generate Doxygen configuration file

```bash
doxygen -g Doxyfile
```

**STEP 3**: Update Doxygen configuration file

```
PROJECT_NAME =
PROJECT_NUMBER =
PROJECT_BRIEF =
PROJECT_LOGO =
OUTPUT_DIRECTORY = doc
CREATE_SUBDIRS = YES
OPTIMIZE_OUTPUT_FOR_C = YES                 # for C
OPTIMIZE_OUTPUT_JAVA = YES                  # for Python/Java
BUILTIN_STL_SUPPORT = YES                   # for C++
TYPEDEF_HIDES_STRUCT = YES                  # for C/C++
SKIP_FUNCTION_MACROS = NO                   # for C/C++
EXTRACT_ALL = YES
EXTRACT_PRIVATE = YES
EXTRACT_STATIC = YES
INPUT =
FILE_PATTERNS = *.py                        # for Python
FILE_PATTERNS = *.c *.h                     # for C
FILE_PATTERNS = *.cc *.cpp *.hh             # for C++
RECURSIVE = YES
SOURCE_BROWSER = YES
EXCLUDE_PATTERNS = */test/*
USE_MDFILE_AS_MAINPAGE = YES                # for GitHub
HTML_TIMESTAMP = YES
HTML_DYNAMIC_SECTIONS = YES
GENERATE_MAN = YES
MAN_LINKS = YES
```

**STEP 4**: Generate documentation

```bash
doxygen Doxyfile
```

## Git Workflow

See [GitHub Flow](http://scottchacon.com/2011/08/31/github-flow.html)

### Start

```bash
git clone <git-url>
git init
```

### Mainstream

Branch `master` contains codes only for official releases with some version
tags.

```bash
git checkout master
git pull --rebase
git merge --no-ff dev
git tag -a <tag> -m '<tag-comment>' # e.g., git tag -a 'v0.1' -m 'v0.1 - Initial version'

git push
git push --tag
```

### Bugfix for Mainstream

```bash
git checkout -b <bugfix-A> master
# ... (git add/rm)
git diff [--cached] <path ...>
# ... (git commit -m)
git diff <bugfix-A>..master

git checkout master
git pull --rebase
git rebase <bugfix-A>
git branch -d <bugfix-A>
```

### Features/Topics

```bash
git checkout <feature-A> dev
git pull --rebase
# ... (git add/rm)
git diff [--cached] <path ...>
# ... (git commit)
git diff <feature-A>..dev

git checkout dev
git pull --rebase
git merge --no-ff <feature-A>
```

### Bugfix for Features/Topics

```bash
git checkout <feature-A>
git pull --rebase

git checkout -b <feature-A-bugfix>
# ... (git add/rm)
git diff [--cached] <path ...>
# ... (git commit)
git diff <feature-A>..<feature-A-bugfix>

git checkout <feature-A>
git pull --rebase
git rebase <feature-A-bugfix>
git branch -d <feature-A-bugfix>
```

## Git Server

```bash
git clone --bare <project-dir> <git-repo>.git
scp -r <git-repo>.git <user>@<git-server>:/<path-to-git-repo>

# On Git Server
sudo adduer git
sudo passwd git
ssh <user>@<git-server>
sudo adduser git
sudo passwd git
sudo chown git:git  /<path-to-git-repo>
gpasswd -a <user> git
```
