# -*- coding: utf-8 -*-
"""

"""
# not working

from PIL import ImageEnhance

enhancer = ImageEnhance.Sharpness("blur1.png")

for i in range(8):
    factor = i / 4.0
    enhancer.enhance(factor).show("Sharpness %f" % factor)
