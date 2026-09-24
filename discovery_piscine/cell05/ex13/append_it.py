#!/usr/bin/env python3

import sys

[print(s if s.endswith("ism") else s + "ism") for s in sys.argv[1:]] or print("none" if len(sys.argv) < 2 else "", end="\n")