# coding: utf-8

import pandas as pd
from SOFASonix import SOFAFile


def view_info(filename):
    try:
        sofa = SOFAFile.load(filename)
    except FileNotFoundError:
        return "requested resource not found"
    except Exception as e:
        return f"error occurred: {e}"

    cols = ["Shorthand", "Type", "Value", "RO", "M", "Dims"]

    rows = []
    params = sofa.flatten()
    for i in params:
        pi = params[i]
        value = "{} Array".format(pi.value.shape) if \
            (pi.isType("double") or pi.isType("string")) else pi.value
        rows.append([".{}".format(pi.getShorthandName()),
                     pi.type[0].upper(),
                     value,
                     pi.isReadOnly(),
                     pi.isRequired(),
                     str(pi.dimensions) if pi.dimensions else "_"])
    pd.set_option('display.max_colwidth', 40)
    pd.set_option('display.expand_frame_repr', False)

    df = pd.DataFrame(rows, columns=cols)
    # print(df)
    info = f"{df}"

    return info
