#!/usr/bin/env python3

import pycomplex

comp = pycomplex.Complex(1, 1).exp()
print(comp.i, comp.r)

c = pycomplex.Complex()
c = c.parser("10+10i")
print(c.r, c.i)
