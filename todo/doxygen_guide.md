# Doxygen Guide

More details on Doxygen, please refer to the on-line manual:

<http://www.stack.nl/~dimitri/doxygen/manual/>

## STEP 1: Doc code

```python
## <function-or-method-description>.
#
# @param <param-name> <param-description>
# @return <return-name> <return-description>
# @exception <exception-name> <exception-description>
# @warning <warning-messages>
# @todo <things to be done>
# @deprecated
# @see <reference to others>
# @since <version>
def func_or_method():
    """<function-or-method-description>.
    """
    # func or method definition
    pass
```

## STEP 2: Generate Doxygen configuration file

```bash
doxygen -g Doxyfile
```

## STEP 3: Update Doxygen configuration file

```ini
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

## STEP 4: Generate documentation

```bash
doxygen Doxyfile
```
