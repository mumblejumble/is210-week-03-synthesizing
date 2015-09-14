#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
DL = 'Spanish'
print len(DL)
print inquisition.SPANISH.index('Spanish')
FLEMISH = inquisition.SPANISH[0:19] + 'Flemish' + inquisition.SPANISH[26:]
print FLEMISH
