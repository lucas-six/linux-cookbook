# UTF-8

**UTF-8** is a *variable-width* **[character encoding](char_encoding)** used for electronic communication.
Defined by the *[Unicode Standard](unicode)*, the name is derived from
**Unicode Transformation Format** – 8-bit.

UTF-8 is by far the most common encoding for the *World Wide Web*,
accounting for over 96% of all web pages, and up to 100% for some languages, as of 2021.
**UTF-8** is the recommendation from the WHATWG for HTML and DOM specifications,
and the Internet Mail Consortium recommends that all e-mail programs be able to display and
create mail using UTF-8.

## Encoding Rules

UTF-8 uses *1* ~ *4* bytes to encode each character,
and can represent any standard [Unicode](unicode) character:

- Backward-compatible with [ASCII](ascii),
the first *128* UTF-8 characters precisely match the first *128* ASCII characters (numbered `0`-`127`),
meaning that existing ASCII text is already valid UTF-8.
A ASCII character only needs *1* byte encoding (Unicode range is from `U+0000` ~ `U+007F`)
- Latin, Greek, Cyrillic, Armenian, Hebrew, Arabic, Syrian and other letters with umlauts require *2*
  byte encoding (Unicode range from `U+0080` ~ `U+07FF`)
- Characters in other languages (including Chinese, Japanese, Korean, Southeast Asian, Middle Eastern,
  etc.) contain most of the commonly used characters, using *3* byte encoding
- Other rarely used language characters use *4* byte encoding

UTF-8 encoding rules: if there is only one byte, the most significant bit is `0`; if it is multi-byte,
the first byte starts from the most significant bit, and the number of consecutive binary bits is `1`.
The number of bytes it encodes. The remaining bytes begin with `10`.

The layout of UTF-8 byte sequences:

| Number of bytes | First code point | Last code point | Byte 1 | Byte 2 | Byte 3 | Byte 4 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `U+0000` | `U+007F` | 0xxxxxxx | - | - | - |
| 2 | `U+0080` | `U+07FF` | 110xxxxx | 10xxxxxx | - | - |
| 3 | `U+0800` | `U+FFFF` | 1110xxxx | 10xxxxxx | 10xxxxxx | - |
| 4 | `U+10000` | `U+10FFFF` | 11110xxx | 10xxxxxx | 10xxxxxx | 10xxxxxx |

## More

<!-- markdownlint-disable line-length -->

- *[RFC 3629 - UTF-8, a transformation format of ISO 10646](https://www.rfc-editor.org/rfc/rfc3629.html)* (2003-11), which establishes UTF-8 as a standard Internet protocol element
- *[RFC 5198 - Unicode Format for Network Interchange](https://www.rfc-editor.org/rfc/rfc5198.html)* (2008-03), defines UTF-8 NFC for Network Interchange (2008-03)
- *[ISO/IEC 10646:2020 - Information technology — Universal coded character set (UCS)](https://www.iso.org/standard/76835.html)* (2020-12)

<!-- markdownlint-enable line-length -->
