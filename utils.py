from typing import cast
from xmlrpc.client import Transport

from PIL.Image import Image


class GZipDisabled(Transport):
    accept_gzip_encoding = False


def get_pixel(img: Image, xy: tuple[int, int]) -> tuple[int, int]:
    return cast(tuple[int, int], img.getpixel(xy))
