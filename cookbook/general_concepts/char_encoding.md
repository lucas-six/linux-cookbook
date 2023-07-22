# Character Encoding

In computing, data storage, and data transmission,
**character encoding** is used to represent a repertoire of [characters](char)
by some kind of encoding system that assigns a
number to each character for digital representation. Depending on the abstraction level and
context, corresponding code points
and the resulting code space may be regarded as bit patterns,
octets, natural numbers, electrical pulses, etc.
A character encoding is used in computation, data storage, and transmission of textual data.
"*Character set*", "*character map*", "*codeset*" and "*code page*" are related, but not identical, terms.

Early character codes associated with the optical or electrical telegraph
could only represent a subset of the characters used in written languages,
sometimes restricted to upper case letters,
numerals and some punctuation only.
The low cost of digital representation of data in modern computer systems
allows more elaborate character codes (such as *[Unicode](unicode)*) which represent most of
the characters used in many written languages.
Character encoding using internationally accepted standards
permits worldwide interchange of text in electronic form.

An **encoding** defines a mapping between **bytes** and **text**.
A sequence of bytes allows for different textual interpretations.
By specifying a particular encoding (such as *UTF-8*),
we specify how the sequence of bytes is to be interpreted.

## Character Set

A **character set** is an encoding system to let computer know how to recognize
*[character](char)*, including letters, numbers, punctuation marks, and
whitespace.

In earlier times, countries developed their own character sets due to their different languages
used, such as "[ASCII](ascii)" for English,  "Kanji JIS" codes (e.g. "Shift-JIS", "EUC-JP", etc.) for
Japanese, "Big5" for traditional Chinese, and "KOI8-R" for Russian.
However, *[Unicode](unicode)* gradually become most acceptable character set
for its universal languages support.
*UTF-8* is the most common character set and includes the graphemes of the most popular human languages.

If character set used incorrectly (For example, Unicode for article encoded in Big5),
you may seen nothing but broken characters, which called [Mojibake](Mojibake).
