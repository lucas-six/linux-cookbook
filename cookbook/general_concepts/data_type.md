# Data Type

In computer science and computer programming, a **data type** or simply **type** is an
attribute of data which tells the compiler or interpreter how the programmer intends
to use the data. Most programming languages support basic data types of *integer numbers*
(of varying sizes), *floating-point numbers* (which approximate real numbers), *characters* and *Booleans*.
A data type constrains the values that an expression, such as a variable
or a function, might take. This data type defines the operations that can be done on the data,
the meaning of the data, and the way values of that type can be stored. A data type provides a
set of values from which an expression (i.e. variable, function, etc.) may take its values.
A value's data type also affects which operations are valid on that value.
For example, an integer can be multiplied by an integer, but not by a string.

Almost all programming languages explicitly include the notion of data type,
though different languages may use different terminology.

Common data types include:

- Integer
- Floating-point number
- [Character](char)
- [String](str)
- Boolean

## Static Typing

A **statically-typed** language is a language (such as *Java*, *C*, or *C++*) where variable
types are known at **compile time** by **compiler**.
In most of these languages, types must be
expressly indicated by the programmer; in other cases (such as *OCaml*),
type inference allows the programmer to not indicate their variable types.

## Dynamic Typing

**Dynamically-typed** languages
are those (like *Python*, *JavaScript*) where the **interpreter** assigns variables
a type at **runtime** based on the variable's value at the time.

## Primitive

The **primitive** (**primitive value**, **primitive data type**) is data that is
not an object and has no methods.

Most of the time, a primitive value is represented directly at **the lowest level of the language implementation**.

All primitives are **immutable**, i.e., they cannot be altered. It is important not to
confuse a primitive itself with a variable assigned a primitive value. The variable may
be reassigned a new value, but the existing value can not be changed in the ways that
objects, arrays, and functions can be altered.

## Type Conversion

**Type conversion** (or **typecasting**) means transfer of data from one data type to another.
*Implicit conversion* happens when the compiler automatically assigns data types,
but the source code can also explicitly require a conversion to take place.
For example, given the instruction `5 + 2.0`,
the floating point `2.0` is implicitly typecasted into an integer, but given the instruction
`Number("0x11")`,
the string `"0x11"` is explicitly typecasted as the number `17`.

## Type Coercion

**Type coercion** is the *automatic* or *implicit* **conversion** of values from one data type to another
(such as *strings* to *numbers*). Type conversion is similar to type coercion because they both
convert values from one data type to another with one key difference —
**type coercion is implicit whereas type conversion can be either implicit or explicit.**

For example,

```javascript
const value1 = '5';
const value2 = 9;
let sum = value1 + value2;

console.log(sum);
```

In the above example, JavaScript has coerced the `9` from a number into a string and then concatenated
the two values together, resulting in a string of `"59"`. JavaScript had a choice between a string or
a number and decided to use a string.

The compiler could have coerced the `5` into a number and returned a sum of `14`, but it did not.
To return this result, you'd have to explicitly convert the `5` to a number using the `Number()` method:

```javascript
sum = Number(value1) + value2;
```
