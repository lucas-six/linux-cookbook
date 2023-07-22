# Mojibake

**Mojibake** is the *garbled text* that is the result of text being decoded using an unintended
*[[character encoding]]*. The result is a systematic replacement of symbols with completely
unrelated ones, often from a different writing system.

This display may include the generic replacement character ("�") in places where the binary
representation is considered invalid. A replacement can also involve multiple consecutive
symbols, as viewed in one encoding, when the same binary code constitutes one symbol in the
other encoding. This is either because of differing constant length encoding (as in Asian
16-bit encodings vs European 8-bit encodings), or the use of variable length encodings
(notably UTF-8 and UTF-16).

Failed rendering of glyphs due to either missing fonts or missing glyphs in a font is a
different issue that is not to be confused with mojibake. Symptoms of this failed rendering
include blocks with the code point displayed in hexadecimal or using the generic replacement
character. Importantly, these replacements are valid and are the result of correct error
handling by the software.
