#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()
programpath = 'G:\\Data\\Lambda\\CS\\Computer-Architecture\\ls8\examples\\call.ls8'
cpu.load(programpath)
cpu.run()
