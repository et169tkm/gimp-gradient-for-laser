#!/usr/bin/python

from gimpfu import *

def gradient_for_laser(img, layer, howmuch):
    pass

register(
    "python_fu_gradient_for_laser",
    "Gradient for laser", "Gradient for laser",
    "Eric Tang", "Eric Tang", "2015",
    "Gradient for laser",
    "RGB*",
    [ (PF_INT, "amt", "How much?", 50) ],
    [],       # return vals, seldom used
    gradient_for_laser,
    menu = "<Image>/Filters/Enhance"
)

main()
