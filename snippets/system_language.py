#!/usr/bin/env python
# Description: "Small script to detect the system language and the character encoding"

import locale
from langcodes import *  # pip install langcodes language-data


lang = locale.getdefaultlocale()

print(f"Language:  \"{Language.get(lang[0]).display_name(lang[0])}\" \n"
      f"Lang-Code: \"{lang[0]}\" \n"
      f"Encoding:  \"{lang[1]}\"")
