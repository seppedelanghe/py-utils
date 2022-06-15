import numpy as np
from typing import List

'''
    Make a heatmap from a list of coordinates
'''
def make_heatmap(positions: List[tuple], precision: tuple = (50, 100)):
    heat = np.zeros(precision)

    for (x, y) in positions:
        x = int(x * precision[1])
        y = int(y * precision[0])

        x = x if x >= 0 else 0
        y = y if y >= 0 else 0

        if x > precision[1] - 1:
            x = precision[1] - 1

        if y > precision[0] - 1:
            y = precision[0] - 1

        heat[y, x] += 1

    heatmap = np.rint(heat / np.max(heat) * 100)
    return heatmap, np.max(heat)