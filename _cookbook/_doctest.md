The `howto_doctest` module
========

Using `func_1`, `func_2`, `func_3`, `func_4`.

This file is written in Markdown format.

First import functions from `howto_doctest` module:

```python

    >>> from _doctest import func_1, func_2, func_3, func_4

```

Now use them:

```python

    >>> func_1()
    

    >>> func_2()
    <BLANKLINE>

    >>> func_3('Hello')
    Hello

    >>> func_4()
    Traceback (most recent call last):
        ...
    ValueError: error description
	
	>>> def func_5():
	...    print('func_5')
	>>> func_5()
	func_5

```
