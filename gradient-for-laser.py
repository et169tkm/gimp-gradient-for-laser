#!/usr/bin/python

from gimpfu import *

def gradient_for_laser(img, drawable):
    pdb.gimp_message("hello")
    
    return

register(
    "python_fu_gradient_for_laser",
    "Gradient for laser", "Gradient for laser",
    "Eric Tang", "Eric Tang", "2015",
    "Gradient for laser",
    "RGB*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None),
    ],
    [],       # return vals, seldom used
    gradient_for_laser,
    menu = "<Image>/Eric"
)

main()
