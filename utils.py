import pandas as pd


def hex_table(bstr: bytes):
    data = bstr.hex(" ").split()
    return pd.DataFrame(
        [data[i : i + 16] for i in range(0, len(data), 16)],
        columns=[hex(i)[2:] for i in range(16)],
        index=[hex(i)[2:] for i in range(0, len(data), 16)],
    ).fillna("+")
