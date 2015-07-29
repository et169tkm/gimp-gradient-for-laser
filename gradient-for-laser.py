#!/usr/bin/python

from gimpfu import *

def get_color(x, y, intensity):
    intensity_map = [
        [ # 0
            [  0,   0,   0,   0],
            [  0,   0,   0,   0],
            [  0,   0,   0,   0],
            [  0,   0,   0,   0],
        ],
        [ # 1
            [255,   0,   0,   0],
            [  0,   0,   0,   0],
            [  0,   0,   0,   0],
            [  0,   0,   0,   0],
        ],
        [ # 2
            [255,   0,   0,   0],
            [  0,   0,   0,   0],
            [  0,   0, 255,   0],
            [  0,   0,   0,   0],
        ],
        [ # 3
            [255,   0,   0,   0],
            [  0,   0, 255,   0],
            [  0,   0,   0,   0],
            [  0, 255,   0,   0],
        ],
        [ # 4
            [255,   0, 255,   0],
            [  0,   0,   0,   0],
            [255,   0, 255,   0],
            [  0,   0,   0,   0],
        ],
        [ # 5
            [255,   0,   0,   0],
            [  0,   0, 255,   0],
            [255,   0,   0, 255],
            [  0, 255,   0,   0],
        ],
        [ # 6
            [255,   0, 255,   0],
            [  0, 255,   0,   0],
            [  0,   0, 255,   0],
            [  0, 255,   0, 255],
        ],
        [ # 7
            [255,   0, 255,   0],
            [  0,   0,   0, 255],
            [  0, 255, 255,   0],
            [255,   0,   0, 255],
        ],
        [ # 8
            [255,   0, 255,   0],
            [  0, 255,   0, 255],
            [255,   0, 255,   0],
            [  0, 255,   0, 255],
        ],
        [ # 9
            [  0, 255,   0, 255],
            [255, 255, 255,   0],
            [255,   0,   0, 255],
            [  0, 255, 255,   0],
        ],
        [ # 10
            [  0, 255,   0, 255],
            [255,   0, 255, 255],
            [255, 255,   0, 255],
            [255,   0, 255,   0],
        ],
        [ # 11
            [  0, 255, 255, 255],
            [255, 255,   0, 255],
            [  0, 255, 255,   0],
            [255,   0, 255, 255],
        ],
        [ # 12
            [  0, 255,   0, 255],
            [255, 255, 255, 255],
            [  0, 255,   0, 255],
            [255, 255, 255, 255],
        ],
        [ # 13
            [  0, 255, 255, 255],
            [255, 255,   0, 255],
            [255, 255, 255, 255],
            [255,   0, 255, 255],
        ],
        [ # 14
            [  0, 255, 255, 255],
            [255, 255, 255, 255],
            [255, 255,   0, 255],
            [255, 255, 255, 255],
        ],
        [ # 15
            [  0, 255, 255, 255],
            [255, 255, 255, 255],
            [255, 255, 255, 255],
            [255, 255, 255, 255],
        ],
        [ # 16
            [255, 255, 255, 255],
            [255, 255, 255, 255],
            [255, 255, 255, 255],
            [255, 255, 255, 255],
        ],
    ]
    return intensity_map[intensity][x%4][y%4]

def gradient_for_laser(img, drawable):
    pdb.gimp_message("begin")
    
    # Set up an undo group, so the operation will be undone in one step.
    pdb.gimp_undo_push_group_start(img)
    
    destDrawable = gimp.Layer(img, "new layer", drawable.width, drawable.height, drawable.type, drawable.opacity, drawable.mode);
    img.add_layer(destDrawable, 0)
    dest_rgn = destDrawable.get_pixel_rgn(0, 0, drawable.width, drawable.height, True, True)

    gimp.progress_init("running")
    for y in range(0, destDrawable.height):
        for x in range(0, 16):
            dest_rgn[x, y] = chr(255) + '\0\0'# + chr(255)
        gimp.progress_update(float(y) / destDrawable.height)

    destDrawable.flush()
    destDrawable.merge_shadow(True)
    destDrawable.update(0, 0, destDrawable.width, destDrawable.height)

    # Close the undo group.
    pdb.gimp_undo_push_group_end(img)

    pdb.gimp_message("done")
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
