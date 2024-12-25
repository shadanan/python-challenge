from typing import cast

import pandas as pd
from PIL.Image import Image


def hex_table(bstr: bytes):
    data = bstr.hex(" ").split()
    return pd.DataFrame(
        [data[i : i + 16] for i in range(0, len(data), 16)],
        columns=[hex(i)[2:] for i in range(16)],
        index=[hex(i)[2:] for i in range(0, len(data), 16)],
    ).fillna("+")


def get_pixel(img: Image, xy: tuple[int, int]) -> tuple[int, int]:
    return cast(tuple[int, int], img.getpixel(xy))
