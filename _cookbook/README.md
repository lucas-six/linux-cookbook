cookbook
==================

Cookbook

- [Linux User Guide](#linux-user-guide)
- [Bash Guide](#bash-guide)
- [Regular Expression](#regular-expression)
- [Python Coding Style](#python-coding-style)
- [Doxygen Guide](#doxygen-guide)
- [PyUnit](#pyunit)

## Linux User Guide

```bash
sudo shutdown -h|-r now

# Package Management on Debian/Ubuntu
sudo apt-get update
sudo apt-get install <pkg>
sudo apt-get remove/purge <pkg>

cd [~|-|..|<dir>]
pwd
ls [-l|-a|-r]
less <text-file>
ln -s <src> <sym-link>
cp|mv [-r|-u]
rm [-r|-f]
mkdir [-p]

which|man <cmd>

# New User/Group
#
# NOTE: `useradd` and `groupadd` are low-level utilities. On Debian, `adduser`
# and `addgroup` should be used instead.
#
# By default, each normal user in Debian is given a corresponding group with
# the same name, and the system users are placed in the `nogroup` group.
sudo [--system] adduser <user>
sudo passwd <user>
sudo [--system] addgroup <group>

# Add existing user to group (re-login required)
sudo adduser <user> <group>  # for Debian
sudo gpasswd -a <user> <group>  # for all Linux, as well as Debian

# Change file ownership
sudo chown <owner>[:<group>] <file> ...
```

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
 

## Python Coding Style

- Use 4-space indentation, and avoid tabs. ( `-t` option )

- Limit lines to a maximum of *79* characters, and docstrings/comments to *72*.

- Separate top-level function and class definitions with two blank lines, and
  method definitions inside a class are separated by a single blank line.

- Code should always use **UTF-8**.

- When possible, put comments on a line of their own.

- Always make a priority of keeping the comments up-to-date when the code
  changes!

- Using docstrings.

- Use spaces around operators and after commas, but not directly inside
  bracketing constructs. eg. `a = f(a, b)`

- Name your classes and functions consistently; the convention is to use
  `CamelCase` for classes and `lower_case_with_underscores` for functions and
  methods.

- Avoid using underscores to begin variable, function or class names.

> Generally, a variable name `_xxx` is considered "private" and should not be
> used outside that module or class. It's good practice to use `_xxx` to
> denote when a variable is private. Since variables named `__xxx__` often
> mean special things to Python, you should avoid using naming normal
> variables this way.

- Avoid recalculation of the same value.

- Avoid numeric indexing.

- Avoid numeric constants.

> You should name the constants, since it's much easier to read the code and
> therefore easier to get right and to modify later.

- Don't use fancy encodings if your code is meant to be used in international
  environments. Plain **ASCII** works best in any case.

- Absolute imports are recommended, as they are usually more readable and tend
  to be better behaved (or at least give better error messages) if the import
  system is incorrectly configured.

- Imports should usually be on separate lines.

- Module ordering for import statements.

> It is recommended that all module imports happen at the top of Python
> modules. Futhermore, imports should follow this ordering:
>
>      - Standard Library Modules
>      - Third-Party Modules
>      - Application-Specific Modules
>
> Seperate these groups with an empty line between the imports of these three
> types of modules.

- Restrict wildcard imports ( `from module import *` ).

> In practice, using `from module import *` is considered poor style because
> it "pollutes" the current namespace and has the potential of overriding
> names in the current namespace; however, it is extremely convenient if a
> module has many variables that are often accessed, or if the module has a
> very long name.

- Keep user interaction outside of functions.

> The functions should be kept "clean", meaning they shoule silently be used
> purely to take parameters and provide return values. More importantly, it is
> good practice to seperate functions into two categories: those that do
> things (i.e., interactive with users or set variables) and those that
> calculate things (usually returning results).

- Easier to ask for forgiveness than permission (EAFP).

> This common Python coding style assumes the existence of valid keys or
> attributes and catches exceptions if the assumption proves false. This clean
> and fast style is characterized by the presence of many `try` and `except`
> statements. The technique contrasts with the **LBYL** style common to many
> other languages such as C.
>
>     LBYL = (L)ook (B)efore (Y)ou (L)eap:
>
> This coding style explicitly tests for pre-conditions before making calls or
> lookups. This style contrasts with the EAFP approach and is characterized by
> the presence of many if statements.
>
> In a multi-threaded environment, the **LBYL** approach can risk introducing
> a race condition between “the looking” and “the leaping”. For example, the
> code, if key in mapping: return mapping[key] can fail if another thread
> removes key from mapping after the test, but before the lookup. This issue
> can be solved with locks or by using the **EAFP** approach.

- Use local variables to subtitute for module attributes.

> Names like `os.linesep` require the interpreter to do two lookups: 1) lookup
> `os` to find that it is a module, and 2) loopup the `linesep` attribute of
> that module. Because modules are also global variables, we pay another
> penalty. If you use an attribute like this oftern in a function, it's
> recommended that you alias it to a single local variable. Lookups are much
> faster -- local variables are always searched first before globals, and no
> attribute needs to be lookuped either. This is one of the tricks in making
> your program faster: replace often-used (and name-lengthy) module attributes
> with local references, your code runs fasters and has less clutter with a
> shorter name.


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

## PyUnit Guide

```python
import <module>
import unittest

class <Module>TestCase(unittest.TestCase):

    def setUp(self):
        # initialization

    def tearDown(self):
        # Clean up

    @unittest.skip("<reason>")
    @unittest.skipIf(<condition>, "<reason>")
    @unittest.skipUnless(<condition>, "<reason>")
    @unittest.expectedFailure() 
    def test_<method_or_func>(self):
        # Testing
        #
        # self.assertTrue(a)               a
        # self.assertFalse(a)              not a
        # self.assertIs(a, b)              a is b
        # self.assertIsNot(a, b)           a is not b
        # self.assertIsNone(a)             a is None
        # self.assertIsNotNone(a)          a is not None
        # self.assertIn(a, b)              a in b
        # self.assertNotIn(a, b)           a not in b
        # self.assertIsInstance(a, b)      isinstance(a, b)
        # self.assertNotIsInstance(a, b)   not isinstance(a, b)
        # self.assertEqual(a, b)           a == b
        # self.assertNotEqual(a, b)        a != b
        # self.assertGreater(a, b)         a > b
        # self.assertLess(a ,b)            a < b
        # self.assertGreaterEqual(a, b)    a >= b
        # self.assertLessEqual(a, b)       a <= b
        #
        # with self.assertRaises(Error):   raise Error
        #     func(a, b)
        
if __name__ == '__main__':
    unittest.main()
```
