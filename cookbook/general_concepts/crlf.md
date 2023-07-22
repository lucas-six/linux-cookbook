# CRLF

**CRLF**, `/ker'l*f/`, sometimes `/kru'l*f/` or `/C-R-L-F/`,
a **carriage return** (**CR**, ASCII `13`) followed by a **line feed** (**LF**, ASCII `10`).
CR and LF are control characters or bytecode that can be used to mark a line break in a text file.

- **CR** = **Carriage Return** (**`\r`**, *`0x0D`* in hexadecimal, *`13`* in decimal) —
moves the cursor to the beginning of the line without advancing to the next line.

- **LF** = **Line Feed** (**`\n`**, *`0x0A`* in hexadecimal, *`10`* in decimal) —
moves the cursor down to the next line without returning to the beginning of the line.

- **CRLF** = A *CR* immediately followed by a *LF* (**`\r\n`**, *`0x0D0A`*) -
moves the cursor down to the next line and then to the beginning of the line.

Unix/Linux uses just **line feed** (**CR**) as its line terminator.
While Windows and DOS uses **CRLF** to indicate the end-of-line (end-of-paragraph).
