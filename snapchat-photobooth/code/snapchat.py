from PIL import Image
from glob import glob
from textwrap import dedent
from time import gmtime, strftime
from itertools import cycle
import os

overlays_dir = os.path.join(os.path.dirname(__file__), 'overlays')
overlays = [
    img.split('/')[-1].split('.')[0]
    for img in glob('{}/*'.format(overlays_dir))
]

def _get_overlay_image(overlay):
    """
    Given the name of an overlay (without file extension), return the
    corresponding Image object
    """
    return Image.open('{}/{}.png'.format(overlays_dir, overlay))

def _pad(resolution, width=32, height=16):
    # A little utility routine which pads the specified resolution
    # up to the nearest multiple of *width* and *height*; this is
    # needed because overlays require padding to the camera's
    # block size (32x16)
    return (
        ((resolution[0] + (width - 1)) // width) * width,
        ((resolution[1] + (height - 1)) // height) * height,
    )

def remove_overlays(camera):
    """
    Remove all overlays from the camera preview
    """
    [camera.remove_overlay(o) for o in camera.overlays]

def gen_filename():
    """
    Generates a filename with a timestamp
    """
    filename = strftime("/home/pi/snapchat-%d-%m %H:%M.png", gmtime())
    return filename


def preview_overlay(camera=None, overlay=None):
    """
    Given the PiCamera object and an image overlay, add the overlay to the
    camera preview
    """

    if camera is None or overlay is None:
        raise ValueError(dedent("""
        Missing argument

        Usage:

        >>> preview_overlay(camera, overlay)
        """))

    if overlay not in overlays:
        raise ValueError(dedent("""
        Overlay not available

        Available overlays: {}
        """.format(', '.join(o for o in overlays))))

    remove_overlays(camera)

    overlay_img = _get_overlay_image(overlay)
    pad = Image.new('RGB', _pad(camera.resolution))
    pad.paste(overlay_img, (0, 0))
    camera.add_overlay(pad.tobytes(), alpha=128, layer=3)

def output_overlay(output=None, overlay=None):
    """
    Given an image overlay and a captured photo, add the overlay to the photo
    and save the new image in its place
    """

    if overlay is None or output is None:
        raise ValueError(dedent("""
        Missing argument

        Usage:

        >>> output_overlay(output, overlay)

        or:

        >>> output_overlay(output, overlay, caption)
        """))

    overlay_img = _get_overlay_image(overlay)
    output_img = Image.open(output).convert('RGBA')
    new_output = Image.alpha_composite(output_img, overlay_img)
    new_output.save(output)

all_overlays = cycle(overlays)
