# Unicode

## Introduction

**Unicode** is an *information technology standard* for the consistent encoding, representation,
and handling of text expressed in most of the world's writing systems.
It is also called **Universal Coded Character Set**.
The standard is maintained by the **Unicode Consortium**, and as of March 2020,
it has a total of 143,859 characters,
with Unicode 13.0 (these characters consist of 143,696 graphic characters
and 163 format characters) covering 154 modern and historic scripts,
as well as multiple symbol sets and emoji.

The **Unicode Standard** consists of a set of code charts for visual reference,
an encoding method and set of standard character encodings, a set of reference data files,
and a number of related items, such as character properties,
rules for normalization, decomposition, collation, rendering,
and bidirectional text display order (for the correct display of text containing both right-to-left scripts,
such as Arabic and Hebrew, and left-to-right scripts).

## Encodings

The Unicode standard describes how characters are represented by **code points**.
A code point value is an integer in the range `0` to `0x10FFFF`.
In the standard,
a code point is written using the notation *`U+265E`* to mean the character with value `0x265e`
(`9,822` in decimal).

Unicode can be implemented by different **[character encodings](char_encoding)**.
The character repertoire, so called **character set**,
of the Unicode Standard is synchronized with **ISO/IEC 10646**,
each being code-for-code identical with the other.

The Unicode standard defines **Unicode Transformation Formats** (**UTF**): *UTF-8*, *UTF-16*,
and *UTF-32*, and several other encodings.
The *most* commonly used encoding is *[UTF-8](utf_8)*.

*GB 18030* is standardized in China and implements Unicode fully, while not an official Unicode standard.

Mix languages in the same data would cause *Mojibake*.

## Byte Order Mark, BOM

The **byte order mark** (**BOM**) is a particular usage of the special Unicode character,
**`U+FEFF`** (**BYTE ORDER MARK**),
whose appearance as a *magic number* at the start of a text stream
can signal several things to a program reading the text.

- The byte order, or *[endianness](../net/endianness)*,
of the text stream in the cases of 16-bit and 32-bit encodings;
- The fact that the text stream's encoding is Unicode, to a high level of confidence;
- Which Unicode character encoding is used.

### Byte order marks by encoding

BOM use of UTF-8 is *optional*.

- *UTF-8 with BOM*: *`EF BB BF`*
- *UTF-16 LE*: *`FF FE`*
- *UTF-16 BE*: *`FE FF`*
- *UTF-32 LE*: *`FF FE 00 00`*
- *UTF-32 BE*: *`00 00 FE FF`*
- *GB 18030*: *`84 31 95 33`*

## References

- *[The Unicode Standard, Version 14.0](https://www.unicode.org/versions/Unicode14.0.0/)* (2021)
- [The Unicode Standard: A Technical Introduction](https://www.unicode.org/standard/principles.html)
