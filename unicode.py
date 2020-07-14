#! python
# unicode.py - Loads unicode text to the user's clipboard based on the
# code passed into the program.

import pyperclip
import sys
import re

code_regex = re.compile(r"^[0-9a-f]{1,8}$")

if len(sys.argv) == 2 and code_regex.search(sys.argv[1].lower()) != None:
    exec(f"pyperclip.copy(chr(int(0x{sys.argv[1]})))")
else:
    pyperclip.copy("Usage: <win+r> unicode {code}")